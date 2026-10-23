# HW3 Part 4 – Save the results

AI Use: Stage 3 (Little helper)

Write a new function, `save_results(artworks, filename)`, that writes one line per artwork (title, artist, date) to a `.txt` file. Call it so every search saves its results. Then run `fetch.py` for real once, with a search you pick, and **commit the `.txt` file it made**: that's your proof the live call works.

You may have the AI write this function (about 10 lines) using the **[Stage 3 helper prompt](https://canvas.uw.edu/courses/1959879/pages/stage-3-little-helper-prompt)** (rules on the [AI Use Card](https://canvas.uw.edu/courses/1959879/pages/ai-use-card)). Copilot autocomplete stays off. With or without AI, write each step in `ai_log.md` **as you go**:

Done early? Add `sort_by_date(artworks)` too (not graded).

---

## 1. Try
*paste your own attempt or plan for the function, even if it doesn't work*
my rough attempt:

def save_results(artworks, filename):
file = open file??
for artwork in artworks:
    title = artwork["title"]
    artist = artwork.get("artist_title") or "Unknown artist"
    date = artwork.get("date_display") or "Unknown date"
    print(f"{title} | {artist} | {date})
something like this? and I asked on how to build onto it and help code

## 2. Chat (AI only)
*paste the whole conversation, your messages and the AI's replies in order, or a share link from the Share button (the link in your address bar only works for you). No AI? Write "No AI used."*

my rough attempt:
def save_results(artworks, filename):
file = open file??
for artwork in artworks:
    title = artwork["title"]
    artist = artwork.get("artist_title") or "Unknown artist"
    date = artwork.get("date_display") or "Unknown date"
    print(f"{title} | {artist} | {date})
something like this? and I asked on how to build onto it and help code

#AI response
Weighing how to address the similarity honestly.
Your attempt has the right idea. The loop and the three fields are correct, and the or defaults are right. Here’s what it needs to become a working function:

Opening the file. file = open file?? becomes open(filename, "w", encoding="utf-8"). "w" means write, and filename is the input to your function.
print becomes file.write. print shows text on screen, and file.write puts it in the file.
Newline. write doesn’t end the line for you, so add \n at the end of the string.
Closing. Call file.close() after the loop.
Typo. Your f-string is missing the closing " before the ).
Indentation. The for and everything under it must be indented inside the def.

Here is how to write this function (about 10 lines)

def save_results(artworks, filename):
    file = open(filename, "w", encoding="utf-8")
    for artwork in artworks:
        title = artwork.get("title") or "Untitled"
        artist = artwork.get("artist_title") or "Unknown artist"
        date = artwork.get("date_display") or "Unknown date"
        file.write(f"{title} | {artist} | {date}\n")
    file.close()

Put it under # Functions go here, next to count_by_artist.

Calling it: add this after the no-results check (so it only runs when there are results), either right before or right after your printing loop:

save_results(data["data"], "results.txt")

Notes on how it works:

"w" means write, so each search replaces the old file.
encoding="utf-8" keeps names like René Magritte from breaking.
\n ends each line, so you get one artwork per line.
The or defaults match your printing loop, so the file never contains None.

## 3. Predict, then compare
*before you run the function, write what you think the file will contain for the sample data (`check.py` uses it) or for your search. Then paste what it actually contains. (A wrong prediction gets full credit. Don't edit it after running.)*
Lion (One of a Pair, South Pedestal) | Edward Kemeys | 1893
i always get Sorry, there was a problem: 403 Forbidden? when i tried "lion" or "123456789"

I asked AI. Response was...
That 403 comes from the museum’s firewall, not your code. Your step 3 is doing its job, and there’s nothing left to fix in fetch.py for the message itself. Here’s what to try, in order. Each takes a minute.

1.Check the header is really in. The headers = {...} line must be above requests.get, and the call must say headers=headers. If you only added the line but forgot to pass it in, the museum never sees it. Save the file before running.

2.Try a browser-style header. Some firewalls block anything that doesn’t look like a browser. Swap your header line for this, then run it again:
python
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.
36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"}

3.Change networks. Connect your laptop to your phone’s hotspot and run it again. If that works, the block is on your Wi-Fi’s address, not your code. Also turn off any VPN.

4.Test it in your browser. Paste this into Chrome:
https://api.artic.edu/api/v1/artworks/search?q=cat
If the browser shows a wall of JSON, the API is up and it’s your Python request that’s being rejected. If the browser also gets blocked, it’s your network or the museum.

5.Ask your instructor or TA now. The starter was supposed to work as is, and other students may have the same problem. Send them this: “I get 403 Forbidden from api.artic.edu with the starter code. check.py passes. Is there a fix for the live run?” It’s due Monday at 10am, so don’t wait until the weekend.
??

## 4. What surprised me
*one or two sentences. Where were you wrong, or what did you learn? For example: "I thought a missing artist would print `none`, but `.get` gave the fallback `unknown`."*
I did think .get("artist_title", "Unknown") would print the fallback for a missing artist, but check.py showed null as its own group. .get only uses the fallback when the key is missing, so I needed or "Unknown" 

## 5. Change one thing yourself
*once the function works, change one thing about it by hand, no AI. For example: a different line format (date first), a filename based on the search term, or sorted lines. Write what you changed and why, in one or two sentences.*

I changed: 
save_results(data["data"], "results.txt") 
into: 
save_results(data["data"], f"{term}.txt")

I changed the filename from results.txt to f"{term}.txt", so each search saves to its own file. this will make it so that new search dont overwrite the results from earlier one.