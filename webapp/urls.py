from django.urls import path

from .views.projects import ProjectListView, ProjectCreateView, ProjectDetailView, ProjectDelete
from webapp.views import IndexView, CreateTask, ListTaskView, DeleteTask, UpdateTask

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('to_do_lists/add/', CreateTask.as_view(), name="create_task"),
    path('detail/<int:pk>/', ListTaskView.as_view(), name="detail_view"),
    path('delete/<int:pk>/', DeleteTask.as_view(), name="delete_description"),
    path('to_do_lists/<int:pk>/update', UpdateTask.as_view(), name="update"),

    path('projects/<int:pk>/', ProjectListView.as_view(), name='project_view'),
    path('new_projects/<int:pk>/', ProjectCreateView.as_view(), name='project_create'),
    path('project_view/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('project/<int:pk>/delete', ProjectDelete.as_view(), name= 'project_delate'),

]
