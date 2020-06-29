from django.urls import path
from . import views


urlpatterns = [
    path('', views.todoView, name='home'),
    path('todo/<int:id>', views.deleteTodo, name='delete_todo')
]
