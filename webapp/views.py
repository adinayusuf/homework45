from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound
from django.views import View
from django.views.generic import TemplateView

from .forms import ListForm
from webapp.models import ToDoList

class IndexView(View):
    def get(self, request, *args, **kwargs):
        to_do_list = ToDoList.objects.order_by('-update')
        context = {'to_do_list': to_do_list}
        return render(request, 'index.html', context)


class ListView(TemplateView):

    def get_template_names(self):
        return "ditail_view.html"

    def get_context_data(self, **kwargs):
        try:
            pk = kwargs.get('pk')
            to_do_list = get_object_or_404(ToDoList, pk=pk)
            kwargs['to_do_list'] = to_do_list
        except ToDoList.DoesNotExist:
            return HttpResponseNotFound("Page not find")
        return super().get_context_data(**kwargs)


def create_task(request):
    if request.method == "GET":
        form = ListForm()
        return render(request, "create.html", {'form': form})
    else:
        form = ListForm(data=request.POST)
        if form.is_valid():
            description = form.cleaned_data.get("description")
            text = form.cleaned_data.get("text")
            status = form.cleaned_data.get("status")
            date_of_completion = form.cleaned_data.get("date_of_completion", None)
        if not date_of_completion:
            date_of_completion = None
        new_des = ToDoList.objects.create(description=description, status=status,
                                          date_of_completion=date_of_completion, text=text)
        new_des.save()
        return redirect("list_view", pk=new_des.pk)


def delete_description(request, pk):
    list = get_object_or_404(ToDoList, pk=pk)
    if request.method == "GET":
        return render(request, "delete.html", {'list': list})
    else:
        list.delete()
        return redirect("index")


def update(request, pk):
    list = get_object_or_404(ToDoList, pk=pk)
    if request.method == "GET":
        form = ListForm(initial={
            'description': list.description,
            'text': list.text,
            'status': list.status,
            'date_of_completion': list.date_of_completion
        })
        return render(request, "update.html", {'form': form})
    else:
        form = ListForm(data=request.POST)
        if form.is_valid():
            list.description = form.cleaned_data.get("description")
            list.text = form.cleaned_data.get("text")
            list.status = form.cleaned_data.get("status")
            list.date_of_completion = form.cleaned_data.get("date_of_completion", None)
            list.save()
            return redirect("list_view", pk=list.pk)
        return render(request, "update.html", {'form': form})
