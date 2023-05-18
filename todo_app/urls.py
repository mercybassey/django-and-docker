from django.urls import path
from . import views


urlpatterns = [
    path('todos/', views.todo_list, name='todo_list'),
    path('', views.todo_create, name='todo_create'),
    path('<int:pk>/update/', views.todo_update, name='todo_update'),
    path('<int:pk>/delete/', views.todo_delete, name='todo_delete'),
]
