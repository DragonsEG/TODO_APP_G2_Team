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
    REQUIRED_FIELDS = []

    def get_user_id(self):
        return self.id

    class Meta:
        verbose_name = "Custom User"
        verbose_name_plural = "Custom Users"

    def __str__(self) -> str:
        return self.name


# Define related_name for groups and user_permissions fields to avoid conflicts
# CustomUser._meta.get_field("groups").remote_field.related_name = "customuser_set_groups"
# CustomUser._meta.get_field(
#     "user_permissions"
# ).remote_field.related_name = "customuser_set_permissions"





# class CustomUser(models.Model):
#     dep = [("HR", "HR"), ("Marketing", "Marketing")]

#     permissions = [("Admin", "Admin"), ("Manager", "Manager"), ("User", "User")]

#     name = models.CharField(max_length=50, unique=True)
#     email = models.EmailField(max_length=100, unique=True)
#     password = models.CharField(max_length=100)
#     department = models.CharField(choices=dep, max_length=50, default="HR")
#     permission = models.CharField(choices=permissions, max_length=50, default="User")


# # Define the REQUIRED_FIELDS attribute as a list of fields that are required for createsuperuser
# REQUIRED_FIELDS = ["name", "password"]

# # Define the field to be used as the username for authentication
# USERNAME_FIELD = "email"

# def __str__(self) -> str:
#     return self.name


# @classmethod
# def authenticate(self, request,email=None,password=None,**kwargs):
#     try:
#         user = self.get(email=email)
#         if user.check_password(password):
#             return user
#     except user.DoesNotExist:
#         return None


# @property
# def is_anonymous(self):
#     """
#     Return True if this user is anonymous. Always return False for
#     authenticated users.
#     """
#     return not self.is_authenticated

# @property
# def is_authenticated(self):
#     """
#     Return True if this user is authenticated, i.e., they have logged in.
#     Return False for anonymous users.
#     """
#     return True

# def get_by_natural_key(self, username):
#     # Retrieve a user instance by their natural key (e.g., username)
#     return self.get(username=username)

# def set_password(self, raw_password):
#     self.password = make_password(raw_password)


class List(models.Model):
    options = [
        ("In Progress", "In Progress"),
        ("Finished", "Finished"),
    ]

    item = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=options, default="In Progress")
    user_list = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self) -> str:
        return self.item
