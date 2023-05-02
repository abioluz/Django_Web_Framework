from .test_recipe_base import RecipeTestBase, Recipe
from django.core.exceptions import ValidationError
from parameterized import parameterized


class RecipeModelTest(RecipeTestBase):
    '''
    Não testar o Models do Django.
    Testar somente a lógica do modelo criado
    '''

    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    def make_recipe_no_defaults(self):
        recipe = Recipe(
            category=self.make_category(name='Test Default Category'),
            author=self.make_author(username='newuser'),
            title='Recipe Title',
            description='Recipe Description',
            slug='recipe-slug',
            preparation_time=10,
            preparation_time_unit='Minutos',
            servings=5,
            servings_unit='Porções',
            preparation_steps='Recipe Preparation Steps',
        )
        return recipe

    def test_recipe_title_raises_error_if_has_more_than_65_chars(self):
        self.recipe.title = 'a'*70

        with self.assertRaises(ValidationError):
            self.recipe.full_clean()  # Aqui a validação ocorre

    @parameterized.expand(
            [
                ('title', 65),
                ('description', 165),
                ('preparation_time_unit', 65),
                ('servings_unit', 65),
            ]
    )
    def test_recipe_max_length(self, field, max_lenght):
        '''pip install parameterized'''

        setattr(self.recipe, field, 'a'*(max_lenght+1))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()  # Aqui a validação ocorre

    def test_recipe_preparation_steps_is_html_is_false_by_default(self):
        recipe = self.make_recipe_no_defaults()
        recipe.full_clean()
        recipe.save()
        self.assertFalse(
            recipe.preparation_steps_is_html,
            msg='Recipe preparation_steps_is_html is not False ')

    def test_recipe_is_published_is_false_by_default(self):
        recipe = self.make_recipe_no_defaults()
        recipe.full_clean()
        recipe.save()
        self.assertFalse(
            recipe.is_published,
            msg='Recipe is_published is not False ')

    def test_recipe_string_representation(self):
        needed_title = 'Testing Representation'
        self.recipe.title = needed_title
        self.recipe.full_clean()
        self.recipe.save()
        self.assertEqual(
            str(self.recipe),
            needed_title,
            msg=f'Recipe string representation must be '
            f'"{needed_title}" but "{str(self.recipe)}" was received.'
        )
