from django.contrib import admin
from django.urls import path
from .views import indexPage, aboutPage, contactsPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", indexPage, name="home"),
    path("about/", aboutPage, name="about"),
    path("contacts/", contactsPage, name="contacts"),
]
