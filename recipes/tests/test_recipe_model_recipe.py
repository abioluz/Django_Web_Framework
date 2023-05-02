from .test_recipe_base import RecipeTestBase


class RecipeModelTest(RecipeTestBase):
    '''
    Não testar o Models do Django.
    Testar somente a lógica do modelo criado
    '''
    
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    def test_the_test(self):
        recipe = self.recipe
        ...