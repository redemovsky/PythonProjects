import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '427cdbcfc1b8c274f3ea4ffa20944bdc'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
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


'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_reg)
print(response.text)'''

'''response = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = response_conf)
print(response.text)'''

response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response.text)