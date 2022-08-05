from django.urls import path

from .views.projects import ProjectListView, ProjectCreateView, ProjectDetailView, ProjectDelete, ProjectUpdate
from webapp.views import CreateTask, ListTaskView, DeleteTask, UpdateTask

app_name = 'webapp'

urlpatterns = [
    path('', ProjectListView.as_view(), name="index"),
    path('to_do_lists/add/', CreateTask.as_view(), name="create_task"),
    path('detail/<int:pk>/', ListTaskView.as_view(), name="detail_view"),
    path('delete/<int:pk>/', DeleteTask.as_view(), name="delete_description"),
    path('to_do_lists/<int:pk>/update', UpdateTask.as_view(), name="update"),

    # path('projects/', ProjectListView.as_view(), name='project_view'),
    path('projects/add/', ProjectCreateView.as_view(), name='project_create'),
    path('projectdetailview/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('project/delete/<int:pk>/', ProjectDelete.as_view(), name='project_delete'),
    path('projects/update/<int:pk>/', ProjectUpdate.as_view(), name='project_update')
]
