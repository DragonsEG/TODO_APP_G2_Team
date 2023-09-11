from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password



# Create your views here.

@login_required(login_url='login')
def index(request, id):
    if request.user.id == id:
        main_user_id = id
        username = request.user
        dep = username.department
        active = True
        userslists = CustomUser.objects.filter(department=dep)
        search = List.objects.filter(user_list=username)
        search_title = None
        if 'search' in request.GET:
            search_title = request.GET['search']
            search_new = []
            for u in userslists:
                user_items = List.objects.filter(user_list=u)
                search_new.extend(user_items)
            # print(search_new)
            # print("="* 100)
            search_new =List.objects.filter(pk__in=[obj.pk for obj in search_new]) # convert it into query set
            # print(se-arch_new)
            search = search_new.filter(item__startswith = search_title)
            active = False
            

        if request.method == 'POST':
            add_item = ListForm(request.POST)
            if add_item.is_valid():
                # To set the field in the form
                # add_item.cleaned_data['user_list'] = f'{request.user}'
                add_item.save()
                userlist = List.objects.get(user_list=None)
                userlist.user_list = request.user
                userlist.save()

                # userlist = List.objects.filter(user_list__isnull=True)
                # list_id = userlist[0].id
                # userlist = List.objects.get(id=list_id)
                # userlist.user_list = username
                # userlist.save()

        # dep = username.department
        # userslists = User.objects.filter(department=dep)
        if active:
            search = []
            for u in userslists:
                user_items = List.objects.filter(user_list=u)
                search.extend(user_items)

        count = len(List.objects.all())
        count = range(1 , count+1)

        context = {
            'lists': zip(search,count),
            'form' : ListForm,
            'userslists':userslists,
            'id':id,
            'main_user_id':main_user_id,
            'permission': request.user.Permission_user,
        }

        return render(request, 'index.html',context)
    else:
        return redirect('login')


def delete(request,main_user_id, id):

    item_id = get_object_or_404(List, id=id)
    item_id.delete()
    return redirect('index',main_user_id)


def finish(request,main_user_id, id):
    item_id = get_object_or_404(List, id=id)
    item_id.status = 'Finished'
    item_id.save()
    return redirect('index',main_user_id)


def signup(request):

    check_error = True
    if request.method == 'POST':
        user = SignupForm(request.POST)
        email = request.POST.get('email')
        perm = request.POST.get('Permission_user')
        print(user)
        if user.is_valid():
            user.save()
            user = CustomUser.objects.get(email=email)
            if perm == 'Admin':
                user.is_superuser = True
                user.is_staff = True
                user.save()
            elif perm == 'Manger':
                user.is_staff = True
                user.save()
            return redirect('login')
        else:
            check_error = False
    
    context = {
        'SignupForm': SignupForm,
        'check_error': check_error,
    }
    return render(request, 'signup.html',context)



def custom_login(request):

    if request.user.is_authenticated:
        return redirect('index',request.user.id)
    
    check = True
    if request.method == 'POST':
        user_pass = request.POST.get('password')
        email = request.POST.get('email')
        user = authenticate(request,email=email,password=user_pass)
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect('index',user.id)
        else:
            check = False
        
        

        # if email in user_emails:
        #     user = User.objects.filter(email__exact=email).filter(password=user_pass)
        #     if user.exists():
        #         user_id = User.objects.get(email=email)
        #         id = user_id.id
        #         return redirect('index',id)
        #     else:
        #         check = False

    context = {
        'LoginForm':LoginForm,
        'check' : check,
    }
    return render(request,'login.html',context)


def custom_logout(request):
    logout(request)
    return redirect('login')