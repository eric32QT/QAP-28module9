from api import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password


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


def test_add_new_pet_with_valid_data(name='Rufus', animal_type='Senbernard',
                                     age='6', pet_photo='images/Hummel_Vedor_vd_Robandahoeve.jpg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name


def test_successful_delete_self_pet(self):
    _, auth_key = self.pf.get_API_key(valid_email, valid_password)
    _, myPets = self.pf.get_list_of_pets(auth_key, "my_pets")

    if len(myPets['pets']) == 0:
        self.pf.add_new_pet(auth_key, "Суперкот", "кот", "3", "images/cat1.jpg")
        _, myPets = self.pf.get_list_of_pets(auth_key, "my_pets")

    pet_id = myPets['pets'][0]['id']
    status, _ = self.pf.delete_pet(auth_key, pet_id)
    _, myPets = self.pf.get_list_of_pets(auth_key, "my_pets")

    assert status == 200
    assert pet_id not in myPets.values()


def test_successful_update_self_pet_info(self, name='Мурзик', animal_type='Котэ', age=5):
    _, auth_key = self.pf.get_API_key(valid_email, valid_password)
    _, myPets = self.pf.get_list_of_pets(auth_key, "my_pets")

    if len(myPets['pets']) > 0:
        status, result = self.pf.update_pet_info(auth_key, myPets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['name'] == name
    else:
        raise Exception("There is no my pets")

# 10 автотестов для тестирования сайта petfriends1.herokuapp.com


def test_get_api_key_for_invalid_user(email=invalid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result


def test_get_api_key_for_valid_user_with_invalid_password(email=valid_email, password=invalid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result


def test_get_api_key_for_invalid_user_with_invalid_password(email=invalid_email, password=invalid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result


def test_get_api_key_with_no_user_data_and_valid_password(email='', password=invalid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result


def test_get_api_key_for_valid_user_with_no_password(email=valid_email, password=''):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result


def test_add_new_pet_with_invalid_name(name='3o79hjhaK@@@***', animal_type='Senbernard',
                                     age='6', pet_photo='images/Hummel_Vedor_vd_Robandahoeve.jpg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_with_invalid_animal_type(name='Rufus', animal_type='###$$$$jkbfjadhad8978979',
                                     age='6', pet_photo='images/Hummel_Vedor_vd_Robandahoeve.jpg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_with_invalid_age(name='Rufus', animal_type='Senbernard',
                                     age='сорок_пять', pet_photo='images/Hummel_Vedor_vd_Robandahoeve.jpg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_with_video_instead_of_picture(name='Rufus', animal_type='Senbernard',
                                     age='6', pet_photo='images/Miku.mp4'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_with_no_data(name='', animal_type='',
                                     age='', pet_photo=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name
