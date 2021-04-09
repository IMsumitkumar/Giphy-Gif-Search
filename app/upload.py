# python
import urllib.request
import json

url = "http://upload.giphy.com/v1/gifs"

values = {
    "api_key": "cVXPfoOVDz2dPEX6pgejfkJi9do21D8f",
    "username": "IMSumit",
    "source_image_url": "https://i.imgur.com/xoVBP0k.gif"
}

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}

data = json.dumps(values).encode("utf-8")

req = urllib.request.Request(url, data, headers)
with urllib.request.urlopen(req) as res:
    print(res.read().decode())

