# HW2 Part 1 – Model first (in `design.md`, no code)

---

## 1. Why is `artworks` a list of dictionaries and not one big dictionary? What would you lose or gain the other way?
Searching “van Gogh” has to check every artwork, and a list allows duplicates.
A big dictionary gains fast lookup when you know the key, but it loses the first value if there’s a duplicate, because the last one overwrites it. 

## 2. Which fields are sometimes missing? What should the app show when they are?
Artist, year, and medium is all missing a few. App should show not recorded, instead of the information because it doesnt have the key and crash

