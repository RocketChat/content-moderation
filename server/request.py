import requests

payload = {
      'url': [
            "https://unsplash.com/photos/I2fStgjOyAg/download?force=true",
            "https://unsplash.com/photos/-Hm_xIcYbUY/download?force=true&w=640"
      ]
}

resp = requests.post("http://127.0.0.1:5000/predict", json = payload)

print(resp.json())