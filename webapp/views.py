from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound
from django.views import View
from django.views.generic import TemplateView

from .forms import ListForm
from webapp.models import ToDoList


class IndexView(View):
    def get(self, request, *args, **kwargs):
        to_do_list = ToDoList.objects.order_by('-updated_at')
        context = {'to_do_list': to_do_list}
        return render(request, 'index.html', context)


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


class CreateTask(View):

    def get(self, request, *args, **kwargs):
        self.form = ListForm()
        return render(request, "create.html", {'form': self.form})

    def post(self, request, *args, **kwargs):
        self.form = ListForm(data=request.POST)
        if self.form.is_valid():
            self.form.summary = self.form.cleaned_data.get("summary")
            self.form.description = self.form.cleaned_data.get("description")
            self.form.status = self.form.cleaned_data.get("status")
            self.form.created_at = self.form.cleaned_data.get("created_at", None)
            self.form.type = self.form.cleaned_data.get('type', None)
        if not self.form.created_at:
            self.form.created_at = None
        new_des = ToDoList.objects.create(summary=self.form.summary, status=self.form.status,
                                          created_at=self.form.created_at, description=self.form.description,
                                          type=self.form.type)
        new_des.save()
        return redirect("detail_view", pk=new_des.pk)


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




class UpdateTask(View):

    def dispatch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        self.list = get_object_or_404(ToDoList, pk=pk)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            form = ListForm(initial={
                'summary': self.list.summary,
                'description': self.list.description,
                'status': self.list.status,
                'type': self.list.type,
                'created_at': self.list.created_at
            })
            return render(request, "update.html", {'form': form})

    def post(self, request, *args, **kwargs):
        form = ListForm(data=request.POST)
        if form.is_valid():
            self.list.summary = form.cleaned_data.get("summary")
            self.list.description = form.cleaned_data.get("description")
            self.list.status = form.cleaned_data.get("status")
            self.list.created_at = form.cleaned_data.get("created_at", None)
            self.list.save()
            return redirect("detail_view", pk=self.list.pk)
        return render(request, "update.html", {'form': form})
