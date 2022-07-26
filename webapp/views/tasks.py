from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.http import urlencode
from django.views import View
from django.views.generic import TemplateView, FormView, ListView, DetailView, CreateView

from webapp.views.base_view import DetailView
from forms import ListForm, SearchForm
from webapp.models import ToDoList


class IndexView(ListView):
    model = ToDoList
    template_name = 'tasks/index.html'
    context_object_name = 'to_do_list'
    ordering = '-updated_at'
    paginate_by = 10
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        if self.search_value:
            return ToDoList.objects.filter(
                Q(summary__icontains=self.search_value) | Q(description__icontains=self.search_value))
        return ToDoList.objects.all()

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


class ListTaskView(DetailView):
    template_name = "tasks/ditail_view.html"
    model = ToDoList


class SearchView(ListView):
    model = ToDoList
    form_class = SearchForm
    context_object_name = 'to_do_list'
    tasks = []

    def get_queryset(self):
        form = self.form_class(self.request.GET)
        if form.is_valid():
            return ToDoList.objects.filter(summary__icontains=form.cleaned_data['summary'])
        return ToDoList.objects.all()


class CreateTask(CreateView):
    form_class = ListForm
    template_name = 'tasks/create.html'


class DeleteTask(View):

    def dispatch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        self.list = get_object_or_404(ToDoList, pk=pk)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, "tasks/delete.html", {'list': self.list})

    def post(self, request, *args, **kwargs):
        self.list.delete()
        return redirect("index")


class UpdateTask(FormView):
    form_class = ListForm
    template_name = "tasks/update.html"

    def get_success_url(self):
        return reverse('detail_view', kwargs={'pk': self.task.pk})

    def dispatch(self, request, *args, **kwargs):
        self.task = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(ToDoList, pk=self.kwargs.get('pk'))

    def get_initial(self):
        initial = {}
        for key in 'summary', 'description', 'status':
            initial[key] = getattr(self.task, key)
        initial['types'] = self.task.types.all()
        return initial

    def form_valid(self, form):
        types = form.cleaned_data.pop('types')
        for key, value in form.cleaned_data.items():
            if value is not None:
                setattr(self.task, key, value)
        self.task.save()
        self.task.types.set(types)
        return super().form_valid(form)
