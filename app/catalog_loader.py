import requests
import json
import re

URL = "https://tcp-us-prod-rnd.shl.com/voiceRater/shl-ai-hiring/shl_product_catalog.json"

def clean_json_text(text):

    # remove invalid control characters
    text = re.sub(r'[\x00-\x1F\x7F]', '', text)

    return text

def load_catalog():

    response = requests.get(URL)

    cleaned_text = clean_json_text(response.text)

    data = json.loads(cleaned_text)

    return data