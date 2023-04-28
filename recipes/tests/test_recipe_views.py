from django.test import TestCase
from django.urls import reverse
from django.urls import resolve
from recipes import views
from recipes.models import Category, Recipe
from django.contrib.auth.models import User


# Create your tests here.
# pip install pytest pytest-django
# pip install pytest-watch
# ptw para ficar gerando o teste de forma automática
# https://pt.linkedin.com/pulse/todos-os-atalhos-do-vs-code-mateus-barbosa

class RecipeViewsTest(TestCase):

    def test_recipe_home_views_function_is_correct(self):
        # view = resolve('/')
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn('No Recipes found here 😓', response.content.decode(
                                                                    'utf-8'))
        
    def test_recipe_home_template_loads_recipes(self):
        '''Para este teste é necessário criar receitas para o teste
           use o shift+end para selecionar até no fim da linha '''

        category = Category.objects.create(name='Category')

        author = User.objects.create_user(
            first_name='user',
            last_name='name',
            username='username',
            password='123456',
            email='username@email.com')

        recipe = Recipe.objects.create( # noqa: F841,E261
            category=category,
            author=author,
            title='Recipe Title',
            description='Recipe Description',
            slug='recipe-slug',
            preparation_time=10,
            preparation_time_unit='Minutos',
            servings=5,
            servings_unit='Porções',
            preparation_steps='Recipe Preparation Steps',
            preparation_steps_is_html=False,
            is_published=True)

        response = self.client.get(reverse('recipes:home'))
        response_recipes = response.context['recipes']

        content = response.content.decode('utf-8')

        self.assertEqual(len(response_recipes), 1)
        self.assertEqual(response_recipes.first().title, 'Recipe Title')
        self.assertIn('Recipe Title', content)
        self.assertIn('10 Minutos', content)
        self.assertIn('5 Porções', content)

    def test_recipe_category_views_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id':
                                                           1000}))
        self.assertIs(view.func, views.category)

    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(reverse('recipes:category',
                                           kwargs={'category_id': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_recipes_views_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)

    def test_recipe_detail_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 100}))
        self.assertEqual(response.status_code, 404)