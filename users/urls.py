from django.contrib import admin
from django.urls import path
from .views import register, index

urlpatterns = [
    path('register/', register, name='register'),
    # path('login/', login, name='login'),
    path('', index),
]
