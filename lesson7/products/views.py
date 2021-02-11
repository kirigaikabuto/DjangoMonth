from django.shortcuts import render
from .models import Product


def list(request):
    products = Product.objects.all()
    for i in products:
        print(i.name, i.price)
    d = {
        "products": products,
    }
    return render(request, "products/list.html", context=d)
