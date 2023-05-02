from .test_recipe_base import RecipeTestBase
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
