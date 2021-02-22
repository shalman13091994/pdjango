from django.urls import path
from .views import homepage,welcome,password

urlpatterns=[
    path('',homepage,name='home'),
    path('welcome',welcome,name='welcom'),
    path('password',password,name='password'),
]