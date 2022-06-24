from django.urls import path
from webapp.views import index_view, create_description, list_view, delete_description

urlpatterns = [
    path('', index_view),
    path('to_do_lists/add/', create_description),
    path('to_do_lists/', list_view),
    path('delete/<int:pk>', delete_description)
]
