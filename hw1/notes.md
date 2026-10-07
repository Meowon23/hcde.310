# HW1 notes

## Part 4: Predict, run, explain

**My prediction for `predict.py` (written BEFORE running it):**
for i in range(3):
    print(i, titles[i], years[i] + 100)
print(len(titles))
print(len(titles[0]))

it will loop 3 times, and print index from 0, title and year + 100
and 
print(len(titles)) will print the number titles in the list
print(len(titles[0])) will print the length of length of characters in 1st?

0 The Bedroom 1989
1 Nighthawks 2042
2 American Gothic 2030
10
11

**What it actually printed:**

0 The Bedroom 1989
1 Nighthawks 2042
2 American Gothic 2030
10
11

**Explain:** If I was off, which line surprised me and why? If I was right, why do the last two lines print different numbers?

I got the lines right, after looping for 3 times, 
print(len(titles)) will print the number titles in the list which is 10,
print(len(titles[0])) will print the length of character in 1st title which is 11

## Part 5: Reflection (about 100 words)

Look back at your Day 1 app: its code if you can still open it, or your screenshots of it running. Is there anything you can now recognize (a loop, an `if`, a list)? Where? If you only have screenshots, what do you think the code had to do to make the app behave that way?

for example, i found part of the code from the day1 app with if statement, it only runs the code if the statement under it is valid, such as if the artwork has the keyword in it. Loop could be used for showing artwork, because the code has to loop through each artwork. List could be used for search results, where it could store multiple artworks that match the search? There were many cases that uses these if makes it very complicated I also learned that `len()` can be used to find how many items are in a list. These could be used for making an artwork search thingy.