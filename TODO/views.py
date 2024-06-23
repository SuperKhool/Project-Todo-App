from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import Task

def addtask(request):
    addtasks=request.POST['task']
    Task.objects.create(task=addtasks )
    return  redirect('home')