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

products = [
    {
        "id": 1,
        "name": "product1",
        "description": "it is good product1",
        "price": 300,
    },
    {
        "id": 2,
        "name": "product2",
        "description": "it is good product2",
        "price": 400,
    },
    {
        "id": 3,
        "name": "product3",
        "description": "it is good product3",
        "price": 500,
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
        "products": products,
    }
    return render(request, "frontend/index.html", context=d)


def loginAction(request):
    username = request.POST["username"]
    password = request.POST['pass']
    if len(username) == 0:
        return HttpResponse("Please write your username")
    if len(password) == 0:
        return HttpResponse("Please write your password")
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


def registerAction(request):
    username = request.POST["username"]
    password = request.POST['pass']
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    age = int(request.POST["age"])
    d = {
        "username": username,
        "password": password,
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
    }
    users.append(d)
    return HttpResponse("OK")


def productDetail(request, id):
    product = {}
    for i in products:
        if i["id"] == id:
            product = i
            break
    d = {
        "product": product,
    }
    return render(request, "frontend/detail.html", context=d)
