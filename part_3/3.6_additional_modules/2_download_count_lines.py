import requests

url = input().strip()

r = requests.get(url)
lines = r.text.splitlines()

print(len(lines))
