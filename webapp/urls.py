from django.urls import path
from webapp.views import IndexView, create_task, ListView, delete_description, update

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('to_do_lists/add/', create_task, name="create_task"),
    path('to_do_lists/<int:pk>/', ListView.as_view(), name="list_view"),
    path('delete/<int:pk>/', delete_description, name="delete_description"),
    path('to_do_lists/<int:pk>/update', update, name="update")
]
