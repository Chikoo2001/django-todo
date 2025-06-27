from django.shortcuts import render
from todo.models import Task

def home(request):
    completedTasks = Task.objects.filter(is_completed=True).order_by('-updated_at')
    incompleteTasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    context = {
        "completedTasks": completedTasks,
        "incompleteTasks": incompleteTasks
    }
    return render(request, 'home-todo.html', context)