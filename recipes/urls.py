
from django.urls import path

from recipes.views import home
from recipes.views import contato
from recipes.views import sobre




urlpatterns = [

    path('', home),
    path('sobre/', sobre),
    path('contato', contato),]
