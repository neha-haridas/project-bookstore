from django.urls import path
from . import views

urlpatterns = [
    path('login/login/register/',views.register,name='register'),
    # path('login/login/register/register/reg',views.reg,name='reg'),
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('logout/', views.logout, name='logout'),
    path('changepassword/', views.changepassword, name='changepassword'),
    # path('base/', views.base, name='base'),
]
