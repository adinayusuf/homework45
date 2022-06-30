from django.urls import path
from webapp.views import index_view, create_task, list_view, delete_description, update

urlpatterns = [
    path('', index_view, name="index"),
    path('to_do_lists/add/', create_task, name ="create_task"),
    path('to_do_lists/<int:pk>/', list_view, name="list_view"),
    path('delete/<int:pk>/', delete_description, name="delete_description"),
    path('to_do_lists/<int:pk>/update', update, name="update")
]
