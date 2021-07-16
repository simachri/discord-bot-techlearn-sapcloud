import requests
from io import BytesIO
import random
import logging

# Setup logging.
logging.basicConfig(level=logging.INFO)

async def fetch_random_superhero_avatar() -> tuple[str, BytesIO]:
    """Fetch a random superhero avatar from the API https://akabab.github.io/superhero-api/api/.

      This is an example of the JSON data returned by the API when invoking /api/id/1.json:
       {
        "id": 1,
        "name": "A-Bomb",
        "slug": "1-a-bomb",
        "powerstats": {
            "intelligence": 38,
            "strength": 100,
            "speed": 17,
            "durability": 80,
            "power": 24,
            "combat": 64
        },
        "appearance": {
            "gender": "Male",
            "race": "Human",
            "height": [
            "6'8",
            "203 cm"
            ],
            "weight": [
            "980 lb",
            "441 kg"
            ],
            "eyeColor": "Yellow",
            "hairColor": "No Hair"
        },
        "biography": {
            "fullName": "Richard Milhouse Jones",
            "alterEgos": "No alter egos found.",
            "aliases": [
            "Rick Jones"
            ],
            "placeOfBirth": "Scarsdale, Arizona",
            "firstAppearance": "Hulk Vol 2 #2 (April, 2008) (as A-Bomb)",
            "publisher": "Marvel Comics",
            "alignment": "good"
        },
        "work": {
            "occupation": "Musician, adventurer, author; formerly talk show host",
            "base": "-"
        },
        "connections": {
            "groupAffiliation": "Hulk Family; Excelsior (sponsor), Avengers (honorary member); formerly partner of the Hulk, Captain America and Captain Marvel; Teen Brigade; ally of Rom",
            "relatives": "Marlo Chandler-Jones (wife); Polly (aunt); Mrs. Chandler (mother-in-law); Keith Chandler, Ray Chandler, three unidentified others (brothers-in-law); unidentified father (deceased); Jackie Shorr (alleged mother; unconfirmed)"
        },
        "images": {
            "xs": "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/xs/1-a-bomb.jpg",
            "sm": "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/sm/1-a-bomb.jpg",
            "md": "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/md/1-a-bomb.jpg",
            "lg": "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/images/lg/1-a-bomb.jpg"
        }
      }

      :returns:
        - name of avatar
        - avatar as bytes
      :raises:
          HTTPError: Calling the API returned a non-200 error code.
    """
    # Use the cached URL of the API: https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api
    # The superhero database contains 731 entries, see https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json
    hero_found = False
    response = None
    for _ in range(5):
        # Generate a random superhero ID between 1 and 731.
        hero_id = random.randint(1, 731)
        logging.info(f"Random superhero ID is {hero_id}.")
        response = requests.get(
            f"https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/id/{hero_id}.json")
        # For some hero IDs the data package is very large and the HTTP request returns
        # a 403 error "Package size exceeds the configured limit of 50 MB".
        # Check if this error is returned. If yes, query a different, yet less performant 
        # URL.
        if response.status_code == 200:
            logging.info("Superhero data retrieved.")
            hero_found = True
            break
        logging.info("No superhero data retrieved. Trying again.")
    if not hero_found:
        if response:
            # Raise an exception if the HTTP request has a return code other than 200 - OK.
            response.raise_for_status()
        else:
            raise requests.HTTPError("No superhero found.")

    # Get the superhero data from the HTTP response.
    hero_data = response.json()

    # Download the avatar image from the URL that is given in the superhero
    # data under images/sm (= small image).
    hero_avatar_url = hero_data["images"]["sm"]
    logging.info(f"Superhero avatar image URL is {hero_avatar_url}.")

    response = requests.get(hero_avatar_url, stream=True)
    # Raise an exception if the HTTP request has a return code other than 200 - OK.
    response.raise_for_status()

    # Get the hero name.
    hero_name = hero_data["name"]
    logging.info(f"Superhero name is {hero_name}.")

    return hero_name, BytesIO(response.content)
