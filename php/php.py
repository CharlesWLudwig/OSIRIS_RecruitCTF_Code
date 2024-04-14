import requests

url = "http://recruit.osiris.bar:10003"

response = requests.get(url, params={
    'get_param': 'Hello world!'
})

with open("response.txt", "w") as f:
    f.write(response.text)