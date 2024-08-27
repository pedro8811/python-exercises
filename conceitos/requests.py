import requests
delay = 'https://httpbin.org/delay/6'
url = 'https://httpbin.org/basic-auth/pedro/testing'
r = requests.get(delay, timeout=3)

print(r)