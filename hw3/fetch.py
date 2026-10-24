# HW3 Part 2 + Part 3 + Part 4
#
# Instructions: README.md in this folder (same as the assignment on Canvas).

import requests

FIELDS = "id,title,artist_title,artist_display,date_display,place_of_origin,medium_display,dimensions"

# Functions go here (above the code that runs)
def count_by_artist(artworks):
    counts = {}
    for i in range(len(artworks)):
        artist = artworks[i].get("artist_title") or "Unknown"
        counts[artist] = counts.get(artist, 0) + 1
    return counts

def save_results(artworks, filename):
    file = open(filename, "w", encoding="utf-8")
    for artwork in artworks:
        title = artwork.get("title") or "Untitled"
        artist = artwork.get("artist_title") or "Unknown artist"
        date = artwork.get("date_display") or "Unknown date"
        file.write(f"{title} | {artist} | {date}\n")
    file.close()

term = input("Search the Art Institute for: ")

url = "https://api.artic.edu/api/v1/artworks/search"      
params = {"q": term, "fields": FIELDS}  
headers = {"AIC-User-Agent": "HCDE310 student project"}
response = requests.get(url, params=params, headers=headers)
if response.status_code != 200:
    print(f"Sorry, there was a problem: {response.status_code} {response.reason}")
    exit()
data = response.json()
if not data["data"]:
    print(f"No artworks found for {term}. Try a different word.")
    exit()
save_results(data["data"], f"{term}.txt")
for artwork in data["data"]:
    title = artwork["title"]
    artist = artwork.get("artist_title") or "Unknown artist"
    date = artwork.get("date_display") or "Unknown date"
    place = artwork.get("place_of_origin") or "Unknown place"
    medium = artwork.get("medium_display") or "Unknown medium"
    size = artwork.get("dimensions") or "Unknown size"
    print(f"{title} - {artist} ({date}) - {place} - {medium} - {size}")

counts = count_by_artist(data["data"])
print(counts)

