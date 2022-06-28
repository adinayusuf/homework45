from django.urls import path
from webapp.views import index_view, create_description, list_view, delete_description

urlpatterns = [
    path('', index_view, name="index"),
    path('to_do_lists/add/', create_description ,name ="create_description" ),
    path('to_do_lists/<int:pk>/', list_view, name ="list_view" ),
    path('delete/<int:pk>/', delete_description, name= "delete_description"),
]
