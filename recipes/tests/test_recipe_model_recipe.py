from .test_recipe_base import RecipeTestBase
from django.core.exceptions import ValidationError


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


