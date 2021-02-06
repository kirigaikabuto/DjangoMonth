from django.shortcuts import render

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


def list(request):
    d = {
        "products": products,
    }
    return render(request, "products/list.html", context=d)


def get(request, id):
    product = {}
    for i in products:
        if i["id"] == id:
            product = i
    d = {
        "product": product,
    }
    return render(request, "products/get.html", context=d)
