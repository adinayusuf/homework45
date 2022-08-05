from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode
from django.views.generic import DetailView, ListView, CreateView, FormView, DeleteView, UpdateView

from webapp.forms import ProjectForm, SearchForm
from webapp.models import Project


class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'
    ordering = 'title'
    template_name = 'projects/project_view.html'

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        if self.search_value:
            return Project.objects.filter(
                Q(title__icontains=self.search_value) | Q(description__icontains=self.search_value))
        return Project.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            query = urlencode({'search': self.search_value})
            context['query'] = query
            context['search'] = self.search_value
        return context

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get('search')


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
    success_url = reverse_lazy('webapp:index')

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class ProjectUpdate(UpdateView):
    form_class = ProjectForm
    template_name = "projects/project_update.html"
    model = Project
    context_object_name = 'project'

    def get_success_url(self):
        return reverse('webapp:project_detail', kwargs={'pk': self.object.pk})


class SearchView(ListView):
    model = Project
    form_class = SearchForm
    context_object_name = 'project'
    tasks = []

    def get_queryset(self):
        form = self.form_class(self.request.GET)
        if form.is_valid():
            return Project.objects.filter(title__icontains=form.cleaned_data['title'])
        return Project.objects.all()
