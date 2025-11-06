from django.shortcuts import render, redirect
from .models import Todo

def index(request):
    todos = Todo.objects.all().order_by('-created')
    return render(request, 'todos/index.html', {'todos': todos})

def add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Todo.objects.create(title=title)
    return redirect('index')
