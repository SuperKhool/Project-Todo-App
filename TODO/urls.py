from . import views
from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    #Add Task
    path('addtask/',views.addtask,name='addtask'),
    #Make Task Done
    path('mark_as_done/<int:pk>/',views.mark_as_done,name='mark_as_done'),
    #Make Task Undone
    path('mark_as_undone/<int:pk>/',views.mark_as_undone,name='mark_as_undone'),
    #Edit Task
    path('edit_task/<int:pk>/',views.edit_task,name='edit_task')
]
