# HW2 Part 2 – One dict = one thing
#
# In `part2.py`, print each artwork as `Title - Artist (Year)`, for example `The Bedroom - Vincent van
# Gogh (1889)`. Use `.get()` so a missing artist or year prints `Unknown` instead of crashing.

#    {"title": "The Bedroom", "artist": "Vincent van Gogh", "year": 1889, "medium": "Oil on canvas"},

from artworks import artworks

for i in range(len(artworks)):
    title = artworks[i]["title"]
    artist = artworks[i].get("artist", "Unknown")
    year = artworks[i].get("year", "Unknown")
    
    print(f"{title} - {artist} ({year})")
    
    

    
