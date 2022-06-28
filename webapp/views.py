from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponseNotFound
# Create your views here.
from django.urls import reverse

from webapp.models import To_do_list, STATUS_CHOICES


def index_view(request):
    to_do_list = To_do_list.objects.order_by('-date_of_completion')
    context = {'to_do_list': to_do_list}
    return render(request, 'index.html', context)



def list_view(request, pk):
    # pk = request.GET.get("pk")
    try:
        to_do_list = To_do_list.objects.get(pk=pk)
    except To_do_list.DoesNotExist:
        return HttpResponseNotFound("Page not find")
    return render(request, "ditail_view.html", {'to_do_list': to_do_list})
    # return redirect("ditail_view.html", pk=to_do_list.pk)


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
        # return HttpResponseRedirect(f"/to_do_lists/{new_des.pk}")
        # return HttpResponseRedirect(reverse("list_view", kwargs={"pk": new_des.pk}))
        return redirect("list_view", pk=new_des.pk)


def delete_description(request, pk):
    to_do_list = To_do_list.objects.get(pk=pk)
    to_do_list.delete()
    return redirect("delete_description", pk=to_do_list.pk)
