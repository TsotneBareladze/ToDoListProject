from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<str:pk>', views.deleteTask, name='delete'),
    path('update_task/<str:pk>', views.updateTask, name='update_task'),
    path('delete_task/<str:pk>', views.deleteTask, name='delete_task'),
    path('search_task', views.searchTask, name='search_task'),
]