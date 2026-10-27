import requests
base = "https://api.artic.edu/api/v1/artworks"

requests.get(base + "?limit=1")
requests.get(base + "/search?q=cats&limit=1")
requests.get(base + "/search?q=zzzqqxx&limit=1")

# for each: r.json()["pagination"]["total"]
r = requests.get(base + "?limit=1")
if r.status_code == 200:
    data = r.json()
artworks = data["data"]
print(artworks)