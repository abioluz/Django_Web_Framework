from django.shortcuts import render
from . import models


# Create your views here.
def home(request):
    recipes = models.Recipe.objects.all().order_by('-id')

    return render(request,'recipes/pages/home.html',{
        'recipes' : recipes
    })

def categoy(request, category_id):
    recipes = models.Recipe.objects.filter(category__id=category_id).order_by('-id')

    return render(request,'recipes/pages/home.html',{
        'recipes' : recipes
    })

def recipe(request, id):
    recipes = models.Recipe.objects.get(id=id)
    return render(request,'recipes/pages/recipe-view.html',{
        'recipe': recipes,
        'is_detail_page': True,
    })

