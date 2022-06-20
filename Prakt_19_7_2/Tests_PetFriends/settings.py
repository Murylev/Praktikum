# Валидные данные для авторизации
valid_email = 'mavrus@list.ru'
valid_password = '12345'
# ------------------------------------------------------------------------------------------------

# Не валидные данные для авторизации
invalid_email = 'mavrus@list.ru'
invalid_password = '11111'
invalid_auth_key = {
  "key": "ea738148a1f19838e1c3731380e733e877b0ae729"
}
rotten_auth_key = {
  "key": "6c6bd121eaa83f0f24c7a8bd658bcc08c56748d9fd55048f18eb9c33"
}
# -----------------------------------------------------------------------------------------------


# Данные для добавления питомца
add_name = 'Рыжик'
add_age = '4'
add_animal_type = 'Python'
add_pet_photo = 'images/cat1.jpg'
# -----------------------------------------------------------------------------------------------

# Данные для обновления информации о питомце
update_name = 'Генрих'
update_age = '12'
update_animal_type = 'Java'
update_pet_photo = 'images/cat2.jpg'
# ----------------------------------------------------------------------------------------------


def generate_string(num):
    return "x" * num


def russian_chars():
    return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def chinese_chars():
    return '的一是不了人我在有他这为之大来以个中上们'


def special_chars():
    return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'







