import requests
import urllib.request
import urllib.response
import time
from bs4 import BeatifulSoup

class LoadHtml:
    def __init__(self):
        pass


    url = "https://instacart.com"
    response = requests.get(url)
    soup = BeatifulSoup(response.text, "html.parser")

    soup.findAll('a')