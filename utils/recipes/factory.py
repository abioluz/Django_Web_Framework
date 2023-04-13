from random import randint
from faker import Faker
import re

def criar_slug(texto):
    # Converte para letras minúsculas
    texto = texto.lower()
    # Remove caracteres especiais e substitui por traço
    texto = re.sub(r'[^a-z0-9]+', '-', texto)
    # Remove traços duplicados
    texto = re.sub(r'--+', '-', texto)
    # Remove traços do início e do fim
    texto = texto.strip('-')
    return texto


def rand_ratio():
    return randint(840, 900), randint(473, 573)

fake = Faker('pt_BR')

# print(signature(fake.random_number))

def make_recipe():
    return {
        'id': fake.random_number(digits=2, fix_len=True),
        'title': fake.sentence(nb_words=6),
        'description': fake.sentence(nb_words=12),
        'preparation_time': fake.random_number(digits=2, fix_len=True),
        'preparation_time_unit': 'Minutos',
        'servings': fake.random_number(digits=2, fix_len=True),
        'servings_unit': 'Porção',
        'preparation_steps': fake.text(3000),
        'created_at': fake.date_time(),
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        },
        'category': {
            'name': fake.word()
        },
        'cover': {
            'url': 'https://loremflickr.com/%s/%s/food,cook' % rand_ratio(),
        }
    }

def make_recipe_user(new_recipe,categories):


    titulo = fake.sentence(nb_words=65)
    new_recipe.title = titulo
    new_recipe.description = fake.sentence(nb_words=165)
    new_recipe.slug = criar_slug(titulo)
    new_recipe.preparation_time = fake.random_number(digits=2, fix_len=True)
    new_recipe.preparation_time_unit = 'Minutos'
    new_recipe.servings = fake.random_number(digits=2, fix_len=True)
    new_recipe.servings_unit = 'Porção'
    new_recipe.preparation_steps = fake.text(3000)
    new_recipe.preparation_steps_is_html = False
    new_recipe.created_at = fake.date_time()
    new_recipe.updated_at = fake.date_time()
    new_recipe.is_published = False
    new_recipe.cover = 'https://loremflickr.com/%s/%s/food,cook' % rand_ratio()
    new_recipe.category_id = 1
    new_recipe.author_id = 1

    new_recipe.save()
    # return new_recipe


if __name__ == '__main__':
    from pprint import pprint
    pprint(make_recipe())