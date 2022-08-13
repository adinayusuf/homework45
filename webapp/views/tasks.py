from django.contrib.auth.mixins import PermissionRequiredMixin

from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.views.base_view import DetailView
from webapp.forms import ListForm
from webapp.models import ToDoList


# class IndexView(ListView):
#     model = ToDoList
#     template_name = 'tasks/index.html'
#     context_object_name = 'to_do_list'
#     ordering = '-updated_at'
#     paginate_by = 10
#     paginate_orphans = 1
#
#     def get(self, request, *args, **kwargs):
#         self.form = self.get_search_form()
#         self.search_value = self.get_search_value()
#         return super().get(request, *args, **kwargs)
#
#     def get_queryset(self):
#         if self.search_value:
#             return ToDoList.objects.filter(
#                 Q(summary__icontains=self.search_value) | Q(description__icontains=self.search_value))
#         return ToDoList.objects.all()
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(object_list=object_list, **kwargs)
#         context['form'] = self.form
#         if self.search_value:
#             query = urlencode({'search': self.search_value})
#             context['query'] = query
#             context['search'] = self.search_value
#         return context
#
#     def get_search_form(self):
#         return SearchForm(self.request.GET)
#
#     def get_search_value(self):
#         if self.form.is_valid():
#             return self.form.cleaned_data.get('search')


class ListTaskView(DetailView):
    template_name = "tasks/ditail_view.html"
    model = ToDoList


class CreateTask(PermissionRequiredMixin, CreateView):
    form_class = ListForm
    template_name = 'tasks/create.html'
    model = ToDoList

    def get_success_url(self):
        return reverse("webapp:detail_view", kwargs={"pk": self.object.pk})


class DeleteTask(PermissionRequiredMixin, DeleteView):
    template_name = "tasks/delete.html"
    model = ToDoList
    context_object_name = 'to_do_list'
    success_url = reverse_lazy('webapp:index')

    def get_success_url(self):
        return reverse("webapp:project_detail", kwargs={"pk": self.object.project.pk})


class UpdateTask(PermissionRequiredMixin, UpdateView):
    form_class = ListForm
    template_name = "tasks/update.html"
    model = ToDoList
    context_object_name = 'to_do_list'

    def get_success_url(self):
        return reverse('webapp:detail_view', kwargs={'pk': self.object.project.pk})
