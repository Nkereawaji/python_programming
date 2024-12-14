import requests
r = requests.get("https://www.harvoxx.com")
print(
    r.status_code
)
print
print(
    r.headers
)