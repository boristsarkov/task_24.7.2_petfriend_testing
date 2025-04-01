import pytest

from api import PetFriends

from settings import valid_email, valid_password

pf = PetFriends()

def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    """Проверяем что запрос api ключа возвращает статус 200 и содержит сам ключ"""
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_all_pets_with_valid_key(filter=''):
    """Проверяем что запрос на получение всех питомцев возвращает статус 200 и что ответ содержит в себе
    список питомцев"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0

def test_add_new_pets_with_valid_key(name='Bob', animal_type='cat', age=3, pet_photo='images/1.jpg'):
    """Проверяем что запрос на добавление нового питомца с валидным ключом возвращает статус 200
    и в резултате содержится информация о добавленном питомце"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, pet_photo, name, animal_type, age)
    assert status == 200
    assert len(result) > 0

def test_del_of_pet(pet_id='4c4aab48-66e1-438d-ac9b-891f12e604cb'):
    """Проверяем что запрос на удаление питомца по его id возвращает статус 200 и результат стал нулевым"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.del_pet(auth_key, pet_id)
    assert status == 200
    assert len(result) == 0

def test_update_of_pet(pet_id='723a0ae0-a41f-4de7-9a5f-9b3ec7b8ed8b', name='POOOOP', animal_type='dog', age=99):
    """Проверяем что запрос на изменение питомца возвращает статус 200 и что результат равен новому имени"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.update_pet(auth_key, pet_id, name, animal_type, age)
    assert status == 200
    assert result['name'] == name

def test_add_photo_of_pet(pet_id='723a0ae0-a41f-4de7-9a5f-9b3ec7b8ed8b', pet_photo='images/1.jpg'):
    """Проверяем что запрос на добавление фото возвращает статус 200 и что в ключе pet_photo появился бинарный код
    означающий что фотография добавлена"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_photo_of_pets(auth_key, pet_photo, pet_id)
    assert status == 200
    assert len(result['pet_photo']) > 0

def test_create_pet_simple(name='Jude', animal_type='beawer', age=17):
    """Проверяем что запрос возвращает статус 200 и результат содержит данные о добавлении"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.create_pet_simple(auth_key, name, animal_type, age)
    assert status == 200
    assert len(result) > 0

def test_get_api_key_for_invalid_user(email=valid_email, password=valid_password):
    """Проверяем что запрос api ключа возвращает ошибку валидности данных пользователя"""
    status, result = pf.get_api_key(email, password)
    with pytest.raises(AssertionError):
        assert status == 200
        assert 'key' in result