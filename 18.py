import requests

try:
    response = requests.get("https://goole.com")
except BaseException as e:
    print(f"something went wrong: {e.args}")
