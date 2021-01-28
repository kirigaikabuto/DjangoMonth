from django.shortcuts import render, HttpResponse
import random

users = [
    {
        "username": "yerassyl",
        "password": "passanya99",
        "first_name": "yerassyl",
        "last_name": "tleugazy",
        "age": 22,
    },
    {
        "username": "kirito",
        "password": "732110",
        "first_name": "kirigai",
        "last_name": "kabuto",
        "age": 16
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
        "users": users,
    }
    return render(request, "frontend/index.html", context=d)


def loginAction(request):
    username = request.POST["username"]
    password = request.POST['pass']
    isExist = False
    d = {}
    for i in users:
        if i["username"] == username and i["password"] == password:
            isExist = True
            d = i
            break

    message = "Incorrect username and password"
    if isExist:
        return render(request, "frontend/profile.html", context=d)

    return HttpResponse(message)


def loginPage(request):
    return render(request, "frontend/login.html")


def registerPage(request):
    return render(request, "frontend/register.html")
