from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request=request, template_name="recipes/home.html")


def contato(request):
    return HttpResponse("CONTATO")


def sobre(request):
    return HttpResponse("SOBRE")
