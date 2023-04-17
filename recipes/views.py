from django.shortcuts import render
from . import models


# Create your views here.
def home(request):
    recipes = models.Recipe.objects.filter(is_published=True).order_by('-id')

    return render(request,'recipes/pages/home.html',{
        'recipes' : recipes
    })

def category(request, category_id):
    recipes = models.Recipe.objects.filter(
        is_published=True, 
        category__id=category_id).order_by('-id')

    return render(request,'recipes/pages/category.html',{
        'recipes' : recipes
    })

def recipe(request, id):
    recipes = models.Recipe.objects.get(id=id)
    return render(request,'recipes/pages/recipe-view.html',{
        'recipe': recipes,
        'is_detail_page': True,
    })

