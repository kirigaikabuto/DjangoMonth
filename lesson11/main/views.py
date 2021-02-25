from django.shortcuts import render
from products.models import Product


def main_page(request):
    products = Product.objects.all()
    d = {
        "products": products,
    }
    return render(request, "main/index.html", context=d)
