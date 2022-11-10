from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index, name='home'),
      path('newline',views.newline, name='newline'),
       path('home',views.home, name='home'),
       path('contact',views.contact, name='contact')
]
