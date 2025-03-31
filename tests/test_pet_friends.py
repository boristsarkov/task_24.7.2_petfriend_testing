from api import PetFriends

from settings import valid_email, valid_password

pf = PetFriends()

def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_all_pets_with_valid_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0

def test_add_new_pets_with_valid_key(name='Bob', animal_type='cat', age=3, pet_photo='images/1.jpg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, pet_photo, name, animal_type, age)
    assert status == 200
    assert len(result) > 0

def test_del_of_pet(pet_id='4c4aab48-66e1-438d-ac9b-891f12e604cb'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.del_pet(auth_key, pet_id)
    assert status == 200
    assert len(result) == 0

def test_update_of_pet(pet_id='ddeef448-e723-4d10-99c1-5f21c5067f83', name='POOOOP', animal_type='dog', age=99):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.update_pet(auth_key, pet_id, name, animal_type, age)
    assert status == 200
    assert result['name'] == name