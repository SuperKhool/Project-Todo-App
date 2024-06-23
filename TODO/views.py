from django.shortcuts import render ,redirect ,get_object_or_404
from django.http import HttpResponse
from .models import Task

def addtask(request):
    addtasks=request.POST['task']
    Task.objects.create(task=addtasks )
    return  redirect('home')

def make_as_done(request,pk):
    task=get_object_or_404(Task,pk=pk)
    task.is_completed=True
    task.save() 
    return redirect('home')
    