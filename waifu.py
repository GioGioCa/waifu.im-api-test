import random
import requests
from PIL import Image
from io import BytesIO

# Define a dictionary mapping options to their respective URL parts
options = {
    "waifu": "waifu",
    "neko": "neko",
    "shinobu": "shinobu",
    "megumin": "megumin",
    "bully": "bully",
    "cuddle": "cuddle",
    "cry": "cry",
    "hug": "hug",
    "awoo": "awoo",
    "kiss": "kiss",
    "lick": "lick",
    "pat": "pat",
    "smug": "smug",
    "bonk": "bonk",
    "yeet": "yeet",
    "blush": "blush",
    "smile": "smile",
    "wave": "wave",
    "highfive": "highfive",
    "handhold": "handhold",
    "nom": "nom",
    "bite": "bite",
    "glomp": "glomp",
    "slap": "slap",
    "kill": "kill",
    "kick": "kick",
    "happy": "happy",
    "wink": "wink",
    "poke": "poke",
    "dance": "dance",
    "cringe": "cringe"
}

selected_option = random.choice(list(options.keys()))

url = f"https://api.waifu.pics/sfw/{options[selected_option]}"

response = requests.get(url)

try:
    if response.status_code == 200:

        json_data = response.json()

        desired_url = json_data.get("url")

        print(desired_url)

        image_response = requests.get(desired_url)
        image = Image.open(BytesIO(image_response.content))

        image.show()
    else:
        print(f"Error: {response.status_code}")
except Exception as e:
    print(f"An error occurred: {e}")