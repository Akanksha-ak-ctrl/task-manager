# views.py
from django.shortcuts import render, redirect
from .models import TodoList, TodoItem

def indexview(request):
    todo_lists = TodoList.objects.all()
    for t in todo_lists:
        print(t.todo_item)
    return render(request, 'index.html', {'todo_lists': todo_lists})

def add_todo_list_function(request):
    list_name = request.POST['list_name']
    todo_list = TodoList(name=list_name)
    todo_list.save()
    return redirect('indexname')

def add_todo_item(request):
    todo_list_id = request.POST['todo_list_id']
    text = request.POST['text']
    print(todo_list_id)
    print(text)
    todo_item = TodoItem(todo_list_id=todo_list_id, text=text)
    todo_item.save()
    print(todo_item.todo_list_id)
    return redirect('indexname')

def delete_todo_list(request):
    todo_list_id = request.POST['todo_list_id']
    todo_list = TodoList.objects.get(id=todo_list_id)
    todo_list.delete()
    return redirect('indexname')

def delete_todo_item(request):
    todo_item_id = request.POST['todo_item_id']
    todo_item = TodoItem.objects.get(id=todo_item_id)
    todo_item.delete()
    return redirect('indexname')