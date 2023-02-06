from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(
        request=request, template_name="recipes/home.html", context={"name": "João"}
    )
