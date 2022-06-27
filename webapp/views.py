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
        text = request.POST.get("text")
        status = request.POST.get("status")
        date_of_completion = request.POST.get("date_of_completion")
        new_des = To_do_list.objects.create(description=description, status=status,
                                            date_of_completion=date_of_completion, text=text)
        new_des.save()
        context = {"to_do_list": new_des}
        print(context)
        return render(request, "ditail_view.html", context)


def delete_description(request, pk):
    to_do_list = To_do_list.objects.get(pk=pk)
    to_do_list.delete()
    return render(request, 'index.html')
