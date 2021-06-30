import requests
from io import BytesIO
import random


async def fetch_random_superhero_avatar() -> tuple[str, BytesIO]:
    """Fetch a random superhero avatar from the API https://akabab.github.io/superhero-api/api/.

      :returns:
        - name of avatar
        - avatar as bytes
      :raises:
          requests.ConnectionError: Calling the API returned a non-200 error code.
    """
    # Use the cached URL of the API: https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api
    # The superhero database contains 731 entries, see https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json
    # Generate a random superhero ID between 1 and 731.
    hero_id = random.randint(1, 731)
    response = requests.get(
        f"https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/id/{hero_id}.json")
    if response.status_code != 200:
        raise requests.ConnectionError
    hero_data = response.json()

    # Fetch the avatar image.
    hero_avatar_url = hero_data["images"]["sm"]
    response = requests.get(hero_avatar_url, stream=True)
    if response.status_code != 200:
        raise requests.ConnectionError

    hero_name = hero_data["name"]

    return hero_name, BytesIO(response.content)
