from django.shortcuts import render, redirect
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


def add_page(request):
    return render(request, "products/add.html")


def add_action(request):
    name = request.POST["name"]
    price = int(request.POST["price"])
    description = request.POST["description"]
    user = request.user
    product = Product(author=user, name=name, price=price, description=description)
    product.save()
    return redirect("product_list")
