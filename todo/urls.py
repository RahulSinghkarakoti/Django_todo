from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('add-todo/', views.add_todo, name='ADD_TODO'),
    path('<int:id>/edit', views.edit, name='todo_edit'),
    path('<int:pk>/delete', views.delete, name='todo_delete'),


]