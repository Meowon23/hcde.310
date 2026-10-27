import requests, json


headers = {"User-Agent": "HCDE310-P0 (won23@uw.edu)"}


ol = requests.get(
   "https://openlibrary.org/search.json",
   params={"q": "the left hand of darkness", "limit": 1,
           "fields": "key,title,author_name,first_publish_year,subject,cover_i"},
   headers=headers, timeout=10,
)
print(ol.url)
print(json.dumps(ol.json(), indent=2))


mb = requests.get(
   "https://musicbrainz.org/ws/2/artist",
   params={"query": "artist:Radiohead", "fmt": "json", "limit": 1},
   headers=headers, timeout=10,
)
print(mb.url)
print(json.dumps(mb.json(), indent=2))
