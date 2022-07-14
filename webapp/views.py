from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, FormView

from webapp.base_view import FormView as CustumerFormView
from .forms import ListForm
from webapp.models import ToDoList


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        kwargs['to_do_list'] = ToDoList.objects.all()
        return super().get_context_data(**kwargs)


class ListView(TemplateView):
    template_name = "ditail_view.html"

    def get_context_data(self, **kwargs):
        try:
            pk = kwargs.get('pk')
            to_do_list = get_object_or_404(ToDoList, pk=pk)
            kwargs['to_do_list'] = to_do_list
        except ToDoList.DoesNotExist:
            return HttpResponseNotFound("Page not find")
        return super().get_context_data(**kwargs)


class CreateTask(CustumerFormView):
    form_class = ListForm
    template_name = 'create.html'

    def form_valid(self, form):
        types = form.cleaned_data.pop('types')
        self.task = ToDoList.objects.create(**form.cleaned_data)
        self.task.types.set(types)
        return super().form_valid(form)

    def get_redirect_url(self):
        return redirect('detail_view', pk=self.task.pk)



class DeleteTask(View):

    def dispatch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        self.list = get_object_or_404(ToDoList, pk=pk)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, "delete.html", {'list': self.list})

    def post(self, request, *args, **kwargs):
        self.list.delete()
        return redirect("index")


class UpdateTask(FormView):
    form_class = ListForm
    template_name = "update.html"

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
