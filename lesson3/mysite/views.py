from django.shortcuts import render


def homePage(request):
    name = "Yerassyl"
    lastName = "Tleugazy"
    d = {
        "first_name": name,
        "last_name": lastName,
    }
    return render(request, "frontend/index.html", context=d)
