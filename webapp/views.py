from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound


from webapp.models import To_do_list, STATUS_CHOICES


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
        return render(request, "create.html", {'status': STATUS_CHOICES})
    else:
        description = request.POST.get("description")
        text = request.POST.get("text")
        status = request.POST.get("status")
        date_of_completion = request.POST.get("date_of_completion")
        if not date_of_completion:
            date_of_completion = None
        new_des = To_do_list.objects.create(description=description, status=status,
                                            date_of_completion=date_of_completion, text=text)
        new_des.save()
        return redirect("list_view", pk=new_des.pk)


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
        return render(request, "update.html", {'list': list})
    elif request.method == 'POST':
        list.description = request.POST.get("description")
        list.text = request.POST.get("text")
        list.status = request.POST.get("status")
        list.date_of_completion = request.POST.get("date_of_completion")
        # if not list.date_of_completion:
        #     list.date_of_completion = None
        list.save()
        return redirect("list_view", pk=list.pk)