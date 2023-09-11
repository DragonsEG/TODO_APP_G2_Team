from django import forms
from . models import *
from django.contrib.auth.forms import UserCreationForm

class ListForm(forms.ModelForm):

    class Meta:

        model = List
        fields = [
            'item',
            'status',
        ]


        widgets = {
            'item': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the item', }),
            'status': forms.Select(attrs={'class':'form-select mt-2',}),
        }

        labels = {
            'item':'',
            'status':'',
        }


class SignupForm(UserCreationForm):

    

    name = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control mb-3','placeholder':'Enter your name', }),
        label='Username',
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter your password'}),
        label="Password"
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Confirm password'}),
        label="Confirm Password"
    )

    class Meta:

        model = CustomUser

        fields = [
            'name',
            'email',
            'password1',
            'password2',
            'department',
            'Permission_user'
        ]


        widgets = {

            'email': forms.EmailInput(attrs={'class':'form-control mb-3','placeholder':'Enter your E-mail', }),


            'department': forms.Select(attrs={'class':'form-select mb-3',}),

            'Permission_user': forms.Select(attrs={'class':'form-select mb-3',}),
        }

        labels = {
            'Permission_user':'Permission'
        }



class LoginForm(forms.ModelForm):

    class Meta:

        model = CustomUser

        fields = [
            'email',
            'password',
        ]


        widgets = {
            'email': forms.EmailInput(attrs={'class':'form-control mb-3','placeholder':'Enter your E-mail', }),

            'password': forms.PasswordInput(attrs={'class':'form-control mb-3','placeholder':'Enter your password', }),
        }
