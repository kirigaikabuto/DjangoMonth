from django.shortcuts import render, HttpResponse


# Create your views here.
def plusView(request, number1, number2):
    number1 = int(number1)
    number2 = int(number2)
    sumi = number1 + number2
    return HttpResponse(sumi)


def minusView(request, number1, number2):
    number1 = int(number1)
    number2 = int(number2)
    sumi = number1 - number2
    return HttpResponse(sumi)
