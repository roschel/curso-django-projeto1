from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(
        request=request,
        template_name="recipes/pages/home.html",
        context={"name": "João"},
    )


def recipe(request, id):
    return render(
        request=request,
        template_name="recipes/pages/home.html",
        context={"name": "João"},
    )
