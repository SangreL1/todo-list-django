from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_view, name= 'list-view' ),
    path('create/', views.create_view, name='task_create'),
    path('edit/<int:pk>/', views.edit_view, name='task_update'),
    path('complete/<int:pk>/', views.mark_completed, name='task_complete'),
    path('delete/<int:pk>/', views.delete_view, name='task_delete'),
    path('uncomplete/<int:pk>/', views.unmark_completed, name='task_uncomplete'),
]
