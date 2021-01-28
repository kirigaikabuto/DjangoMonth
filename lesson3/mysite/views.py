from django.shortcuts import render, HttpResponse
import random

users = [
    {
        "username": "yerassyl",
        "password": "passanya99",
    },
    {
        "username": "kirito",
        "password": "732110",
    },
]


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
    password = request.POST['pass']
    isExist = False
    for i in users:
        if i["username"] == username and i["password"] == password:
            isExist = True

    message = "Incorrect username and password"
    if isExist:
        message = "Welcome to this page"

    return HttpResponse(message)
