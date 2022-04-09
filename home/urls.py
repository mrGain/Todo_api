from django.urls import path 
from . import views
urlpatterns = [
    path("", views.api, name="api"),
    path("add-todo-item/",views.add_todo_item,name="add_todo_item"),
    path("list-all-todo-item/",views.list_all_todo_item,name="list_all_todo_item"),
    path("update-todo-item/",views.patch_todo,name="update_todo_item"),
]
