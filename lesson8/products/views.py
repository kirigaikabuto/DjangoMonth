from django.shortcuts import render
from .models import Product


def list(request):
    products = Product.objects.all()  # [Product1,Product2,Product]
    d = {
        "products": products,
    }
    return render(request, "products/list.html", context=d)


def get(request, id):
    product = Product.objects.get(pk=id)  # Product1 or Product2
    d = {
        "product": product,
    }
    return render(request, "products/get.html", context=d)
