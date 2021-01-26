from django.shortcuts import render


def indexPage(request):
    name = "Hello from index Page"
    d = {
        "name": name,
    }
    return render(request, "temp/index.html", context=d)


def aboutPage(request):
    someData = "some data from about page"
    d = {
        "data": someData,
        "age": 15,
    }
    return render(request, "temp/about.html", context=d)


def contactsPage(request):
    return render(request, "temp/contacts.html")
