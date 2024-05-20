import requests
import pytest  

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '427cdbcfc1b8c274f3ea4ffa20944bdc'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '4040'
body_reg = {
    "trainer_token": TOKEN,
    "email": "anatoly.4nikin@gmail.com",
    "password": "Iloveqa1"
}

response_conf = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

def test_status_code(): 
    response = requests.get(url=f'{URL}/trainers')
    assert response.status_code == 200

def test_part_of_responce(): 
    response_get = requests.get(url=f'{URL}/trainers')
    assert response_get.json()["data"][0]["id"] == '4040'
 
    

