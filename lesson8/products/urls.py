from django.urls import path
from .views import *

urlpatterns = [
    path("list/", list, name="product_list"),
    path("get/<int:id>/", get, name="product_get"),
    path("add/", add_page, name="add_page"),
    path("add_action/", add_action, name="add_action"),
    path("remove/<int:id>/", remove, name="remove"),
]
