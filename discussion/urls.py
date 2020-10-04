from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *



app_name = 'disc'

urlpatterns = [
     path('', views.base, name='base'),
     path('blog/', views.blog, name='blog'),
     path('blog/<int:pk>/', views.posting, name='posting'),
     path('blog/new_post/', new_post),
     path('blog/<int:pk>/remove', remove_post),
    
]