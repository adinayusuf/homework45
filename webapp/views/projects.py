from datetime import datetime

from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView, ListView, CreateView, FormView

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
        return reverse('project_detail', kwargs={"pk": self.object.pk})


class ProjectDelete(View):
    def dispatch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        self.project = get_object_or_404(Project, pk=pk)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, "projects/project_delete.html", {'project': self.project})

    def post(self, request, *args, **kwargs):
        self.project.delete()
        return redirect("project_view")


class ProjectUpdate(FormView):
    form_class = ProjectForm
    template_name = "projects/project_update.html"
    model = Project

    def get_context_data(self, **kwargs):
        kwargs['project'] = self.project
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.project.pk})

    def dispatch(self, request, *args, **kwargs):
        self.project = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Project, pk=self.kwargs.get('pk'))

    def get_initial(self):
        initial = {}
        for key in 'title', 'description', 'data_begin', 'data_end':
            initial[key] = getattr(self.project, key)
        return initial

    def form_valid(self, form):
        for key, value in form.cleaned_data.items():
            if value is not None:
                setattr(self.project, key, value)
        self.project.save()
        return super().form_valid(form)
