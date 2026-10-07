# HW1 Part 2: Lists and loops
# Run it:  python3 part2.py
# Your output must match expected/part2.txt exactly.

from artworks import titles
titles = [
    "The Bedroom",
    "Nighthawks",
    "American Gothic",
    "A Sunday on La Grande Jatte",
    "The Old Guitarist",
    "Water Lilies",
    "The Child's Bath",
    "Sky above Clouds IV",
    "Stacks of Wheat (End of Summer)",
    "Mao",
]

for i in range(len(titles)):
    print(f"{i + 1}. {titles[i]}")

print("Titles:", len(titles))

count = 0 
for title in titles:
    if "a" in title:
        count = count + 1
print('Titles with an "a":', count)

longest = ""

for title in titles:
    if len(title) > len(longest):
           longest = title
print("Longest:", longest)