import requests
import pytest

token = '3fcb228449437599aef6e67e634d0cfb'
base_url = 'https://pokemonbattle.me:9104/'

#проверка ответа на GET/trainers
def test_status_code():
    response = requests.get(f'{base_url}trainers')

    assert response.status_code == 200


#в ответе есть конкретный тренер
def test_trainer_id():
    response = requests.get(f"{base_url}trainers", params={"trainer_id":3862})
    response_body = response.text

    assert response.json()["id"] == "3862"