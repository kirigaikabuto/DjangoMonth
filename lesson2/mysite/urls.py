from django.contrib import admin
from django.urls import path
from .views import indexPage, aboutPage, contactsPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", indexPage),
    path("about/", aboutPage),
    path("contacts/", contactsPage),
]
