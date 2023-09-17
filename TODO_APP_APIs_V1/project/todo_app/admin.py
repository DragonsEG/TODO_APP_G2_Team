from django.contrib import admin
from .models import CustomUser,ListItem

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(ListItem)
