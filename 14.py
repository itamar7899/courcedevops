import requests

response  = requests.get("https://www.freecodecamp.org/news/python-new-line-and-how-to-python-print-without-a-newline/")
if response.status_code == 200:
    print("this page is found")

    