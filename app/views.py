from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse

from django.contrib.auth import authenticate, login, logout
from decimal import Decimal
from django.conf import settings

import json
import datetime

from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm
from taggit.models import Tag

from .models import *
from .forms import *
from .models import *
from .filters import *

# Create your views here.

def landing(request):
    return render(request, 'app/landing.html', {})



def track(request):
    return render(request, 'app/track.html', {})

def task_admin(request):
    if not request.user.is_authenticated:
        return redirect("account:login")
    view = 'admin'

    tasks = Task.objects.all()
    name = "All Tasks"
    taskFilter = TaskFilter(request.GET, queryset=tasks)
    total_tasks = tasks.count()
    tasks = taskFilter.qs
    context = {'tasks': tasks, 'name': name, 'total_tasks': total_tasks, 'filter':taskFilter, 'view':view}
    return render(request, 'app/task_admin.html',context)


def tasks(request):
    if not request.user.is_authenticated:
        return redirect("account:login")
    view = 'tasks'

    tasks = Task.objects.all()
    name = "All Tasks"
    taskFilter = TaskFilter(request.GET, queryset=tasks)
    total_tasks = tasks.count()
    tasks = taskFilter.qs
    context = {'tasks': tasks, 'name': name, 'total_tasks': total_tasks, 'filter':taskFilter, 'view':view}
    return render(request, 'app/tasks.html',context)

def my_tasks(request):
    if not request.user.is_authenticated:
        return redirect("account:login")
    view = 'assigned'

    name = "My Tasks"
    tasks = Task.objects.filter(assignee=request.user.owner)
    taskFilter = TaskFilter(request.GET, queryset=tasks)
    total_tasks = tasks.count()
    tasks = taskFilter.qs
    context = {'tasks': tasks, 'name': name, 'total_tasks': total_tasks, 'filter':taskFilter, 'view':view}
    return render(request, 'app/tasks.html', context)

def created_tasks(request):
    if not request.user.is_authenticated:
        return redirect("account:login")
    view = 'created'
    name = "My Tasks"
    tasks = Task.objects.filter(creator=request.user.email)
    taskFilter = TaskFilter(request.GET, queryset=tasks)
    total_tasks = tasks.count()
    tasks = taskFilter.qs
    context = {'tasks': tasks, 'name': name, 'total_tasks': total_tasks, 'filter':taskFilter, 'view':view}
    return render(request, 'app/tasks.html', context)

def add_task(request):
    view = 'create'
    action = 'create'
    name = "Add Task"
    form = TaskForm( initial={'creator': request.user.email, 'owner':request.user.owner})
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app:tasks')

    context =  {'action':action, 'form':form, 'name':name , 'view':view }
    return render(request, 'app/add_task.html', context)

def update_task(request, pk):
    action = 'update'
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task, initial={'creator': task.creator, 'name': task.name,'description': task.description,'priority': task.priority,'notes': task.notes ,'status': task.status } )

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            # Without this next line the tags won't be saved.
            form.save()
            return redirect('app:tasks')

    context =  {'action':action, 'form':form,'task': task, }
    return render(request, 'app/update_task.html', context)

def view_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task, initial={'due_date': task.due_date,'name': task.name,'description': task.description,'priority': task.priority,'notes': task.notes ,'status': task.status } )
    context =  {'form':form,'task': task, }
    return render(request, 'app/view_task.html', context)


def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('app:tasks')

    return render(request, 'app/delete_item.html', {'item':task})
