# urls.py
from django.urls import path
from .views import indexview, add_todo_list_function, add_todo_item, delete_todo_list, delete_todo_item

urlpatterns = [
    path('', indexview, name='indexname'),
    path('add_todo_list/', add_todo_list_function, name='add_todo_list'),
    path('add_todo_item/', add_todo_item, name='add_todo_item'),
    path('delete_todo_list/', delete_todo_list, name='delete_todo_list'),
    path('delete_todo_item/', delete_todo_item, name='delete_todo_item'),
]