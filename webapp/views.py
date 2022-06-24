from django.shortcuts import render

# Create your views here.
from webapp.models import To_do_list, STATUS_CHOICES


def index_view(request):
    to_do_list = To_do_list.objects.order_by('-date_of_completion')
    context = {'to_do_list': to_do_list}
    return render(request, 'index.html', context)


def list_view(request):
    pk = request.GET.get("pk")
    to_do_list = To_do_list.objects.get(pk=pk)
    return render(request, "ditail_view.html", {'to_do_list': to_do_list})


def create_description(request):
    if request.method == "GET":
        return render(request, "create.html", {'status': STATUS_CHOICES})
    else:
        description = request.POST.get("description")
        status = request.POST.get("status")
        new_des = To_do_list.objects.create(description=description, status=status)
        context = {"to_do_list": new_des}
        return render(request, "ditail_view.html", context)


def delete_description(request, id):
    to_do_list = To_do_list.objects.get(pk=id)
    to_do_list.delete()
    return render(request, 'index.html')
