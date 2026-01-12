from django.urls import path
from .views import ( add_task , display_task , update_task , delete_task )

urlpatterns = [
    path('add_task/',add_task,name='add_task'),
    path('display_task/',display_task,name='display_task'),
    path('update_task/<int:pk>/',update_task,name='update_task'),
    path('delete_task/<int:pk>/',delete_task,name='delete_task'),
]