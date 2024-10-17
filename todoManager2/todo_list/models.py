# models.py
from django.db import models

class TodoList(models.Model):
    name = models.CharField(max_length=200)

class TodoItem(models.Model):
    todo_list = models.ForeignKey(TodoList, related_name='todo_item', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
