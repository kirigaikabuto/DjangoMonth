from django.urls import path
from .views import *

urlpatterns = [
    path("list/", list, name="products_list"),
    path("get/<int:id>/", get, name="products_get"),
]
