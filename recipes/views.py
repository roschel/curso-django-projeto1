from django.http import HttpResponse
from django.shortcuts import render

from utils.recipes.factory import make_recipe


# Create your views here.
def home(request):
    return render(
        request=request,
        template_name="recipes/pages/home.html",
        context={"recipes": [make_recipe() for _ in range(10)]},
    )


def recipe(request, id):
    return render(
        request=request,
        template_name="recipes/pages/recipe_view.html",
        context={"recipes": make_recipe()},
    )
