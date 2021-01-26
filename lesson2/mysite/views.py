from django.shortcuts import render


def indexPage(request):
    return render(request, "temp/index.html")


def aboutPage(request):
    return render(request, "temp/about.html")
