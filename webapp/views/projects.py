from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView, CreateView, FormView, DeleteView, UpdateView

from webapp.forms import ProjectForm
from webapp.models import Project


class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'
    ordering = 'title'
    template_name = 'projects/project_view.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset


class ProjectDetailView(DetailView):
    template_name = "projects/project_detailview.html"
    model = Project
    context_object_name = "project"


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_create.html'

    def get_success_url(self):
        return reverse('webapp:project_detail', kwargs={"pk": self.object.pk})


class ProjectDelete(DeleteView):
    template_name = 'projects/project_delete.html'
    model = Project
    context_object_name = 'project'
    success_url = reverse_lazy('project_view')

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class ProjectUpdate(UpdateView):
    form_class = ProjectForm
    template_name = "projects/project_update.html"
    model = Project
    context_object_name = 'project'

    def get_success_url(self):
        return reverse('webapp:project_detail', kwargs={'pk': self.object.pk})
