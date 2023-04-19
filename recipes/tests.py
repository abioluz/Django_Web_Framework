from django.test import TestCase
from django.urls import reverse

# Create your tests here.
# pip install pytest pytest-django
# pip install pytest-watch
# ptw para ficar gerando o teste de forma automática


class RecipeURLsOK(TestCase):
    # def test_the_pytest_is_ok(self):
    #     print('olá mundo')
    #     assert  2 == 3

    def test_recipe_home_url_is_correct(self):
        url = reverse('recipes:home')
        self.assertEqual(url, '/')

    def test_recipe_category_url_is_correct(self):
        url = reverse('recipes:category', args=(1,))
        self.assertEqual(url, '/recipes/category/1/')

    def test_recipe_category_url_is_correct2(self):
        url = reverse('recipes:category', kwargs={'category_id': 1})
        self.assertEqual(url, '/recipes/category/1/')

    def test_recipe_detail_url_is_correct(self):
        url = reverse('recipes:recipe', kwargs={'id': 1})
        self.assertEqual(url, '/recipes/1/')
