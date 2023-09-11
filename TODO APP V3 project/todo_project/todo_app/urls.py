from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.index , name='index'),
    path('delete/<int:main_user_id>/<int:id>', views.delete, name='delete'),
    path('finish/<int:main_user_id>/<int:id>', views.finish, name='finish'),
    path('signup', views.signup , name='signup'),
    path('', views.custom_login , name='login'),
    path('logout', views.custom_logout, name='logout'),

]