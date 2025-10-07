from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from .models import Task


# Create your views here.


def list_view(request):
    task = Task.objects.all().order_by('-created_at')
    return render (request, 'task/listView.html', {'task':task})


def create_view(request):
    form = TaskForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('list-view')
    return render(request, 'task/createView.html', {'form':form})


def edit_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(request.POST or None, instance=task)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('list-view')
    return render(request, 'task/createView.html', {'form':form, 'task':task})

def delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('list-view')
    return render(request, 'task/deleteView.html', {'task':task})

def mark_completed(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.completed = True
        task.save()
    return redirect('list-view') 

def unmark_completed(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.completed = False
        task.save()
    return redirect('list-view')