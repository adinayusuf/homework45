from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound

from forms import ListForm
from webapp.models import To_do_list, STATUS_CHOICES

STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]

def index_view(request):
    to_do_list = To_do_list.objects.order_by('-update')
    context = {'to_do_list': to_do_list}
    return render(request, 'index.html', context)


def list_view(request, pk):
    try:
        to_do_list = To_do_list.objects.get(pk=pk)
    except To_do_list.DoesNotExist:
        return HttpResponseNotFound("Page not find")
    return render(request, "ditail_view.html", {'to_do_list': to_do_list})


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
            date_of_completion = form.cleaned_data.get("date_of_completion")
        if not date_of_completion:
            date_of_completion = None
        new_des = To_do_list.objects.create(description=description, status=status,
                                            date_of_completion=date_of_completion, text=text)
        new_des.save()
        return redirect("create.html", {'form': form})


def delete_description(request, pk):
    list = get_object_or_404(To_do_list, pk=pk)
    if request.method == "GET":
        return render(request, "delete.html", {'list': list})
    else:
        list.delete()
        return redirect("index")

def update(request, pk):
    list = get_object_or_404(To_do_list, pk=pk)
    if request.method == "GET":
        form = ListForm(initial={
            'description': list.description,
            'text': list.text,
            'status': list.status,
        })
        return render(request, "update.html", {'form': form})
    else:
        form = ListForm(data=request.POST)
        if form.is_valid():
            list.description = form.cleaned_data.get("description")
            list.text = form.cleaned_data.get("text")
            list.status = form.cleaned_data.get("status")
            list.save()
            return redirect("list_view", pk=list.pk)
        return render(request, "update.html", {'form': form})
