from django.shortcuts import render, get_list_or_404, get_object_or_404
from . import models



# Create your views here.
def home(request):
    recipes = models.Recipe.objects.filter(is_published=True).order_by('-id')

    return render(request,'recipes/pages/home.html',{
        'recipes' : recipes
    })

def category(request, category_id):
    # recipes = models.Recipe.objects.filter(
    #     is_published=True, 
    #     category__id=category_id).order_by('-id')
    # if not recipes:
    #     raise Http404 ('Not Found - Pena que não existe')

    recipes = get_list_or_404(
        models.Recipe.objects.filter(
        is_published=True, 
        category__id=category_id).order_by('-id')
    )

    return render(request,'recipes/pages/category.html',{
        'recipes' : recipes,
        'title': f'{recipes[0].category.name}  - Category |'
    })

def recipe(request, id):
    recipes = models.Recipe.objects.get(id=id)
    return render(request,'recipes/pages/recipe-view.html',{
        'recipe': recipes,
        'is_detail_page': True,
    })

