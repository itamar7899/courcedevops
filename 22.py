import requests
responce  = requests.get("http://127.0.0.1:5000/names")
print(responce.text)