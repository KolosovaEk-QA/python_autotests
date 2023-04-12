import requests

token = '3fcb228449437599aef6e67e634d0cfb'
headers = {'trainer_token':token}
base_url = 'https://pokemonbattle.me:9104/'

#создать покемона
response_add_pokemon = requests.post(f'{base_url}pokemons', headers = headers, json = {
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
})

print(response_add_pokemon.text)

#изменить имя покемона
response_change_name = requests.put(f'{base_url}pokemons', headers = headers, json = {
    "pokemon_id": "8987",
    "name": "Бульбазавр new",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
})

print(response_change_name.text)


#поймать покемонам в покебол
response_pokeball = requests.post(f'{base_url}trainers/add_pokeball', headers = headers, json = {
    "pokemon_id": "8987"
})

print(response_pokeball.text)