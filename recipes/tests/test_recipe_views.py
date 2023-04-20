from django.test import TestCase
from django.urls import reverse
from django.urls import resolve
from recipes import views

# Create your tests here.
# pip install pytest pytest-django
# pip install pytest-watch
# ptw para ficar gerando o teste de forma automática


class RecipeViewsTest(TestCase):

    def test_recipe_home_views_function_is_correct(self):
        # view = resolve('/')
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_category_views_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)

    def test_recipe_recipes_views_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)

    def test_recipe_home_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/pages/home.html')