from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import *
from .form import *

# Create your views here.
# Create your views here.
# Create your views here.
def home(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request, 'home.html', {'tasks': tasks, 'form': form})



def deleteTask(request, pk):
    tasks = Task.objects.get(id=pk)
    tasks.delete()
    return redirect('/')

def updateTask(request, pk):
    tasks = Task.objects.get(id=pk)
    form = UpdateForm(instance=tasks)
    if request.method == "POST":
        form = UpdateForm(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'task': tasks, 'form': form}
    return render(request, 'update.html', context)


def deleteTask(request, pk):
    tasks = Task.objects.get(id=pk)
    if request.method == 'POST':
        tasks.delete()
        return redirect('/')
    context = {'task': tasks}
    return render(request, 'delete.html', context)

def searchTask(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        tasks = Task.objects.filter(title__contains=searched)

        context = {'searched': searched, 'tasks': tasks}
        return render(request, 'search.html', context)

    else:
        return render(request, 'search.html')




















