from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'recipes/home.html',{
        'name':'Abioluz Robson'
    })

def sobre(request):
    return HttpResponse('Sobre'.upper())

def contato(request):
    return HttpResponse('contato'.upper())