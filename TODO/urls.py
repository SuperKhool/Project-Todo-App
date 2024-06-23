from . import views
from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    
    path('addtask/',views.addtask,name='addtask'),
    path('make_as_done/<int:pk>/',views.make_as_done,name='make_as_done')
    
]
