import os

from file_operations import VERSION
import file_operations
from faker import Faker
import random

fake = Faker("ru_RU")

ancient_font = {
    'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
    'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
    'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
    'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
    'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
    'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
    'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
    'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
    'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
    'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
    'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
    'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
    'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋'
}


def generate_n_skills(n):
    skills = ("Стремительный прыжок", "Электрический выстрел",
              "Ледяной удар", "Стремительный удар",
              "Кислотный взгляд", "Тайный побег",
              "Ледяной выстрел", "Огненный заряд")

    return random.sample(skills, n)


def convert_string_to_ancient_font(string):
    prepared_string = string

    for simple, ancient in ancient_font.items():
        prepared_string = prepared_string.replace(simple, ancient)

    return prepared_string


def generate_profile():
    three_random_skills = generate_n_skills(3)

    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "job": fake.job(),
        "town": fake.city(),
        "strength": random.randint(8, 14),
        "agility": random.randint(8, 14),
        "endurance": random.randint(8, 14),
        "intelligence": random.randint(8, 14),
        "luck": random.randint(8, 14),
        "skill_1": convert_string_to_ancient_font(three_random_skills[0]),
        "skill_2": convert_string_to_ancient_font(three_random_skills[1]),
        "skill_3": convert_string_to_ancient_font(three_random_skills[2]),
    }


def make_dir(name='profiles'):
    try:
        os.mkdir(name)
    except FileExistsError:
        pass


for number in range(10):
    make_dir()
    file_operations.render_template(
        template_path="charsheet.svg",
        output_path="profiles/charsheet-{}.svg".format(number),
        context=generate_profile(),
    )


