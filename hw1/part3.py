# HW1 Part 3: Decisions
# Run it:  python3 part3.py
# Your output must match expected/part3.txt exactly.

from artworks import titles, years

cutoff = 1900  # works made before this year are "old"

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
years = [1889, 1942, 1930, 1884, 1903, 1906, 1893, 1965, 1890, 1973]

for i in range(len(titles)):
    if years[i] > cutoff:
        print(titles[i])
print()

old = 0
modern = 0

for i in range(len(titles)):
    if years[i] < cutoff:
        print(f"{titles[i]}: old")
        old = old + 1

    if years[i] >= cutoff:
        print(f"{titles[i]}: modern")
        modern = modern + 1
print()

print("Old:" , old)
print("Modern:", modern)
    