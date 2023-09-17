from django.http import Http404
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import status,filters,generics,mixins,viewsets
from rest_framework.decorators import api_view
from .models import CustomUser,ListItem
from .serializers import CustomUserSerializer,ListItemSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.



# Get all the user items
def all_items_for_user(request,pk):
    try:
        user = CustomUser.objects.get(pk=pk)
    except CustomUser.DoesNotExist:
        raise Http404
    
    items = user.item.all()

    res = {
        'items': list(items.values('item','status')),
    }
    return JsonResponse(res)


# CBV
# CBV List
class get_add_items(APIView):
    def get(self,request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

# CBV PK
class get_update_del(APIView):
    def get_object(self,pk):
        try:
            return ListItem.objects.get(pk=pk)
        except ListItem.DoesNotExist:
            raise Http404


    def get(self,request,pk):
        item = self.get_object(pk)
        serializer = ListItemSerializer(item,many=False)
        return Response(serializer.data)
    
    def put(self,request,pk):
        item = self.get_object(pk)
        serializer = ListItemSerializer(item,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# GenericAPIView is used with mixins to response
class mixins_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = ListItem.objects.all()
    serializer_class = ListItemSerializer

    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)


class mixins_pk(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):

    queryset = ListItem.objects.all()
    serializer_class = ListItemSerializer

    def get(self,request,pk):
        return self.retrieve(request)
    
    def put(self,request,pk):
        return self.update(request)
    
    def delete(self,request,pk):
        return self.destroy(request)




# Generics is write the endpoint for you and its much easier than mixins
class generics_list(generics.ListCreateAPIView):
    queryset = ListItem.objects.all()
    serializer_class = ListItemSerializer

class generics_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset = ListItem.objects.all()
    serializer_class = ListItemSerializer


# viewsets
class viewsets_items(viewsets.ModelViewSet):
    queryset = ListItem.objects.all()
    serializer_class = ListItemSerializer

    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['status']
    search_fields = ['item']
