from random import randint

from faker import Faker


def rand_ratio():
    return randint(840, 900), randint(473, 573)


fake = Faker("pt_BR")
# print(signature(fake.random_number))


def make_recipe():
    return {
        "title": fake.sentence(nb_words=6),
        "description": fake.sentence(nb_words=12),
        "slug": "slug-teste",
        "preparation_time": fake.random_number(digits=2, fix_len=True),
        "preparation_time_unit": "Minutos",
        "servings": fake.random_number(digits=2, fix_len=True),
        "servings_unit": "Porção",
        "preparation_steps": fake.text(3000),
        "created_at": fake.date_time(),
        "category": {"name": fake.word()},
    }


if __name__ == "__main__":
    from pprint import pprint

    pprint(make_recipe())

# from random import randint

# from recipes.models import Category, Recipe
# from utils.recipes.factory import make_recipe

# categories = Category.objects.all()
# for _ in range(20):
#     recipe = make_recipe()
#     recipe["category"] = categories[randint(0, len(categories))]
#     Recipe(**recipe).save()
