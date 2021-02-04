from django.contrib import admin
from django.urls import path
from .views import homePage, loginAction, loginPage, registerPage, registerAction

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", homePage, name="home_page"),

    path("loginAction/", loginAction, name="login_action"),
    path("loginPage/", loginPage, name="login_page"),

    path("registerPage/", registerPage, name="register_page"),
    path("registerAction/", registerAction, name="register_action"),
]
