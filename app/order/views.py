from django.shortcuts import render


def index(request):
    category = request.GET.get("category")


    return render(request, "order.html", {})
