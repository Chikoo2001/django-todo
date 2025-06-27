from django.urls import path
from . import views

urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
    path('markAsDone/<int:pk>/', views.markAsDone, name='markAsDone'),
    path('markAsUnDone/<int:pk>/', views.markAsUnDone, name='markAsUnDone'),
    path('editTask/<int:pk>/', views.editTask, name='editTask'),
    path('deleteTask/<int:pk>/', views.deleteTask, name='deleteTask'),
]
