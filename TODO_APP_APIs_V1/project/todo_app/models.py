from django.db import models
from django.contrib.auth.models import PermissionsMixin,Group,Permission
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import CustomUserManager

# Create your models here.

class CustomUser(AbstractBaseUser, PermissionsMixin):
    dep = [("HR", "HR"), ("Marketing", "Marketing")]
    permissions = [('Admin','Admin'),('Manger','Manger'),('User','User')]

    name = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    department = models.CharField(choices=dep, max_length=50, default="HR")
    Permission_user = models.CharField(choices=permissions, max_length=50, default="User")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name']

    def get_user_id(self):
        return self.id

    class Meta:
        verbose_name = "Custom User"
        verbose_name_plural = "Custom Users"

    def __str__(self) -> str:
        return self.name
    





class ListItem(models.Model):
    options = [
        ("In Progress", "In Progress"),
        ("Finished", "Finished"),
    ]

    item = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=options, default="In Progress")
    user_list = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, null=True, blank=True, related_name='item'
    )

    def __str__(self) -> str:
        return self.item
