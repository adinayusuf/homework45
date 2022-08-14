from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView

from webapp.forms import SearchForm, ProjectForm, MemberAddForm
from webapp.models import Project, ProjectUser, PROJECT_MANAGER


class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'
    ordering = 'title'
    template_name = 'projects/project_view.html'

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


class ProjectCreateView(PermissionRequiredMixin, CreateView):
    permission_required = "webapp.add_project"
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_create.html'


class ProjectDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'webapp.delete_project'
    template_name = 'projects/project_delete.html'
    model = Project
    context_object_name = 'project'
    success_url = reverse_lazy('webapp:index')

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class ProjectUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = "webapp.change_project"
    template_name = "projects/project_update.html"
    model = Project
    context_object_name = 'project'
    form_class = ProjectForm

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


class ProjectMembersAdd(PermissionRequiredMixin, CreateView):
    permission_required = "webapp.add_projectuser"
    model = Project
    template_name = 'projects/members_add.html'
    form_class = MemberAddForm

    def post(self, request, *args, **kwargs):
        project = self.get_object()
        form = self.get_form()
        if form.is_valid():
            pru = form.save(commit=False)
            pru.project = project
            pru.save()
            return redirect('webapp:index', pk=project.pk)
        else:
            return self.form_invalid(form)

    def get(self, request, *args, **kwargs):
        project = self.get_object()
        form = MemberAddForm(project_id=project.id)
        return render(request, self.template_name, {'form': form, 'project': project})

    def has_permission(self):
        project = self.get_object()
        user_id = self.request.POST.get('user_id')
        if ProjectUser.objects.filter(user=self.request.user, project=project).exists():
            member = ProjectUser.objects.get(user=self.request.user, project=project)
            return super().has_permission() and user_id != self.request.user.id and member.role
        else:
            return False


class ProjectMembersDelete(PermissionRequiredMixin, DeleteView):
    permission_required = "webapp.delete_projectuser"
    model = Project
    success_url = reverse_lazy('webapp:index')

    def post(self, request, *args, **kwargs):
        project = self.get_object()
        user_id = request.POST.get('user_id')
        project.participants.remove(user_id)
        return redirect('webapp:index', pk=project.pk)

    def has_permission(self):
        project = self.get_object()
        user_id = self.request.POST.get('user_id')
        if ProjectUser.objects.filter(user=self.request.user, project=project).exists():
            member = ProjectUser.objects.get(user=self.request.user, project=project)
            return super().has_permission() and int(
                user_id) != self.request.user.id and member.role == PROJECT_MANAGER
        else:
            return False
