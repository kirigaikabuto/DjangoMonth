from django.contrib import admin
from django.urls import path
from .views import homePage, formAction

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", homePage, name="home_page"),
    path("formAction/", formAction, name="form_action"),
]
