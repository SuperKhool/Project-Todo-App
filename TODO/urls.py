from . import views
from django.contrib import admin
from django.urls import path
from .views import addtask
urlpatterns = [
    
    path('addtask/',views.addtask,name='addtask')
    
]
