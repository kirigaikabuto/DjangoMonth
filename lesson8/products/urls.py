from django.urls import path
from .views import *

urlpatterns = [
    path("list/", list, name="product_list"),
    path("get/<int:id>/", get, name="product_get"),
]
