from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404,redirect
from .models import Todos
from nanoid import generate

def home(request):
    todos = Todos.objects.all().order_by('-id')
    return render(request,'index.html',context={'todos':todos})


def add_todo(request):
  if request.method == 'POST':
    #  id=generate(size=10)
     title=request.POST.get("title")
     desc=request.POST.get("description")
     todo=Todos(title=title,description=desc)
     todo.save() 
     return redirect('home') 
  return render(request,'addtodo.html')


def edit(request, id): 
    if request.method == 'POST':
       todo = get_object_or_404(Todos, id=id)
       todo.title = request.POST.get("title")
       todo.description = request.POST.get("description")
       todo.save()
       return redirect('home')
    else:
        todo = get_object_or_404(Todos, id=id)
        return render(request, 'edit.html', context={'todo': todo}) 

def delete(request, pk): 
    todo = get_object_or_404(Todos, pk=pk) 
    todo.delete()
    return redirect('home')   