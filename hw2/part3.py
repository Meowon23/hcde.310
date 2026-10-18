# HW2 Part 3 – Counting with a dictionary
#
# In `part3.py`:
#
# 1. Build a dictionary counting works per artist, and print it: `{'Vincent van Gogh': 1, ...}`. A
#    work with no artist counts under `'Unknown'`.
# 2. Print the artist with the most works: `Most works: Claude Monet (2)`
#
# (This is the letter-counting pattern from Class 3, applied to art.)
from artworks import artworks

counts = {}
for i in range(len(artworks)):
    artist = artworks[i].get("artist", "Unknown")
    counts[artist] = counts.get(artist, 0) + 1
print(counts)

best_name = ""
best_score = 0
for artist in counts:
    if counts[artist] > best_score:
        best_name = artist
        best_score = counts[artist] 
print(f"Most works: {best_name} ({best_score})")   


