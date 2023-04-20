from django.test import TestCase
from django.urls import resolve
from recipes import views

# Create your tests here.
# pip install pytest pytest-django
# pip install pytest-watch
# ptw para ficar gerando o teste de forma automática


class RecipeViewsTest(TestCase):

    def test_recipe_home_views_function_is_correct(self):
        view = resolve('/')
        self.assertIs(view.func, views.home)

    def test_recipe_category_views_function_is_correct(self):
        view = resolve('/recipes/category/1/')
        self.assertIs(view.func, views.category)

    def test_recipe_recipes_views_function_is_correct(self):
        view = resolve('/recipes/1/')
        self.assertIs(view.func, views.recipe)
