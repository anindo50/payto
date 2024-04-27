from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path('api/users/', UserCreateView.as_view(), name='user-create'),
    path("login/",Loginvew.as_view(), name="login")
]