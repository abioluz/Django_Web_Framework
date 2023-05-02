from .test_recipe_base import RecipeTestBase
from django.core.exceptions import ValidationError


class RecipeCategoryModelTest(RecipeTestBase):
    '''
    Não testar o Models do Django.
    Testar somente a lógica do modelo criado
    '''

    def setUp(self) -> None:
        self.category = self.make_category(
            name='Category Testing'
        )
        return super().setUp()

    def test_recipe_category_model_string_representation_is_name_field(self):

        self.assertEqual(
            str(self.category),
            self.category.name,
            msg=f'Recipe category string representation must be '
            f'"{self.category.name}" but "{str(self.category)}" was received.'
        )

    def test_recipe_category_model_name_max_leangth_is_65_chars(self):
        self.category.name = 'A' * 66
        with self.assertRaises(ValidationError):
            self.category.full_clean()
