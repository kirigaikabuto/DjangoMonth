from django.shortcuts import render, HttpResponse
import random


def homePage(request):
    name = "Yerassyl"
    lastName = "Tleugazy"
    number = str(random.randint(0, 30))
    d = {
        "first_name": name,
        "last_name": lastName,
        "number": number,
    }
    return render(request, "frontend/index.html", context=d)


def formAction(request):
    username = request.POST["username"]
    print("data from form", username)
    return HttpResponse("Hello " + username)
