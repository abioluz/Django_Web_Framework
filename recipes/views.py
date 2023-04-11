from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'recipes/pages/home.html',{
        'name':'Abioluz Robson'
    })

def recipe(request, id):
    return render(request,'recipes/pages/home.html',{
        'name':'Abioluz Robson'
    })

#