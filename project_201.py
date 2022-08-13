
import requests

while True:
    pokeman = input("Which Pokeman character would you like to find? ")
    pokeman = pokeman.lower()

    url = f"https://pokeapi.co/api/v2/pokemon/{pokeman}"

    req = requests.get(url)
    if req.status_code == 200:
        data = req.json()

        print(f"The name is:\t{data['name']}")
        print(f"Height:\t\t{data['height']}")

        print('Abilities')
        for ability in data['abilities']:
          print(ability['ability']['name'])
    else:
      print("Sorry, Pokeman not found")

