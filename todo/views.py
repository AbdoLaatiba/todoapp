from django.shortcuts import render
from .models import Todo
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

def todoView(request):
    if request.method == "POST":
        todo_title = request.POST.get('todo_title')
        t = Todo(title=todo_title)
        t.save()
        return redirect('home')
    todos = Todo.objects.all()
    context = {'todos': todos}
    return render(request, 'todo/todos.html', context)


def deleteTodo(request, id):
    t = Todo.objects.get(pk=id)
    t.delete()
    return HttpResponseRedirect(reverse('home'))



