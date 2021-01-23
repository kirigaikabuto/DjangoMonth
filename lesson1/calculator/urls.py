from django.urls import path
from .views import plusView, minusView

urlpatterns = [
    path("plus/<int:number1>/<int:number2>", plusView),
    path("minus/<int:number1>/<int:number2>", minusView),
]
