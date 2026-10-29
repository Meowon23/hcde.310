What I asked the AI for, one piece per prompt (Stage 3):
- search_artworks(term) API call, returns artworks,error message
- / route and home.html
- /results route first skeleton with fake data, then the real one
- results.html template
- A first draft of the # comments in app.py, which I rewrote in my own words

#The / route shows search form
# The /results route reads word user typed
#If word is empty or only spaces it show message and stop.
#Ask Piece A (the fetch function) to search API.
#If came back as an error: show a friendly message. the API call failed
#If came back as an empty list: show “no results. it worked but nothing matched.
#otherwise, /results route reads word user typed, and shows the results page with 3x4 image grid

AI response:
Here’s how to approach each piece. I’ll explain the parts and leave the assembling to you, because the assignment wants these two files hand-written.

Part 1: the / route in app.py

A Flask route has three parts, and you need all three:

Import Flask and set up the app. At the top, import Flask and render_template from flask, then create the app with app = Flask(__name__).
Register the URL. Put @app.route("/") directly above a function. It tells Flask: “when someone visits /, run the function underneath.”
Return a page. Inside the function, return render_template("home.html"). This looks for the file in the templates/ folder, which you already have.

Then you run it from the hw4 folder (with your .venv active, which your terminal shows). Look in your Class 9 notes for the exact run command. It starts a local server and prints a link you open in the browser.

Part 2: home.html

It needs four things:

A heading: “Art Institute of Chicago”.
A <form>. It needs two attributes: action="/results" (where to send the data) and method="get" (so the word shows up in the URL, like /results?q=lion).
A text input and a label. The input needs a name="q". That name is the key your /results route will read later. The <label> is connected to the input with matching for and id values. This is your accessibility requirement.
A submit button. Use a real <button type="submit"> with text like “Search”. For the magnifier from your sketch, you can add an icon inside the button, but keep the text or an aria-label so screen readers know what it does.

The home-page image placeholder can be an <img> with alt text, or a plain gray <div> if it’s decoration only.

How to check it works (these are good for your spec)

Open / in the browser and see the heading, box, and button.
Press Tab: focus should go to the input, then the button.
Type “lion” and press Enter. The URL should change to /results?q=lion. It will show an error page for now, since /results doesn’t exist yet. That’s expected, and it proves the form works.

Where to look

Your Class 9 notes and the in-class-6 folder in your repo (it may have a working form to compare with).
If something breaks, read the traceback bottom line first, like you did in HW3.

Try it, and if you get stuck, paste what you wrote and the error. I can point to the line that’s wrong without rewriting it for you.

My Question:
can you check my work so far?

Reviewing the plan file and the missing AI-written comments
You’ve made real progress. home.html looks right, the plan is now in your own words, and 3x4 / 12 cards is consistently decided. Here’s what I’d fix, most important first.

app.py

Missing # AI-written tags. I don’t see them above the import (line 9) or the route (line 13). The assignment says code the AI writes gets that comment, so add one above each.
Dead code after return. Lines 16-22 sit under return render_template("home.html"), so they never run. They look like the Class 9 fake-data example, which belongs in the /results route, not in home(). Move them there when you write it.
Fake data is too thin. Your skeleton only has {"title": ...}. Use all five fields from your table, and include one artwork with image_id set to None and one with no artist_title, so your defaults get tested.
Order of the pseudocode. Line 7 says “reads word user typed” again, at the end. Reading the word should be step 1 of /results, before the empty check. The last line should only be about showing the grid.
Small cleanups. Line 6 still has an unclosed curly quote “, and line 4 still says “Piece A” (use search_artworks).
/results doesn’t exist yet. That’s the next piece.
home.html

It matches what I gave you. Since you’re marking it AI-written, make one change by hand, such as the heading text, the placeholder, or the gray box size, and write it in ai_log.md.
plan.md

The table won’t render. Lines 11-16 use - as separators. Use pipes, with a divider row under the header:
  | Field | Shown on | If null |
  |---|---|---|
Lines 4, 5, and 9 are still my wording, and 5 and 9 are instructions to you, not plan content. Rewrite them as statements, e.g. “image_id can be null, so the card shows a gray box”.
Headings: add Sketches, Data, and Spec.
Sketches: link your Figma export. The Screenshot 2026-10-28...png in hw4 may be it. Rename it to something like sketch.png and link it from plan.md.
The Spec section is the main missing piece. Each piece (/, /results, search_artworks, card image/defaults) needs In, Out, and 2-3 browser checks. Lines 7-9 are checks for one function, written as Python calls. Under /results, add your four empty states: empty input, no results, API error, and missing image/field.
Accessibility: add the checks (input label, Tab order, alt text).
Other items

Add place_of_origin to FIELDS in search_artworks, since your caption shows the place.
In ai_log.md, paste this chat and write down that your teacher allowed AI for the / route and home.html.
Next

Run the app now (from the hw4 folder with .venv active) and confirm / loads. The form should go to a “Not Found” page for /results, which is expected. Tell me if you get an error.
Fix the small items above and commit.
Write the /results skeleton with fake data.
Tell me when the page runs and I’ll help with the /results route.

AI response
Yes, replace the whole file with this. It keeps your pseudocode at the top (with the order fixed), then the imports, the helper function, and the two routes. The old commented-out fake-data lines are gone, since the real route replaces them.

app.py

python
# ---- Pseudocode (my plan) ----
# The / route shows search form
# The /results route reads the word the user typed
# If word is empty or only spaces, show message and stop
# Ask search_artworks to search the API
# If it came back with an error: show a friendly message, the API call failed
# If it came back as an empty list: show "no results", it worked but nothing matched
# Otherwise: show the results page with the 3x4 image grid

import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# AI-written
FIELDS = "id,title,artist_title,date_display,place_of_origin,image_id"


# AI-written
def search_artworks(term):
    url = "https://api.artic.edu/api/v1/artworks/search"
    params = {"q": term, "fields": FIELDS}
    headers = {"AIC-User-Agent": "HCDE310 student project"}

    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
    except requests.exceptions.RequestException:
        return [], "Could not reach the museum. Check your internet and try again."

    if response.status_code != 200:
        return [], f"Sorry, there was a problem: {response.status_code} {response.reason}"

    data = response.json()
    return data["data"], None


# AI-written
@app.route("/")
def home():
    return render_template("home.html")


# AI-written
@app.route("/results")
def results():
    word = request.args.get("q", "").strip()

    if not word:
        return render_template("results.html", word=word, artworks=[],
                               message="Please type a word to search for.")

    artworks, error = search_artworks(word)

    if error:
        return render_template("results.html", word=word, artworks=[], message=error)

    if not artworks:
        return render_template("results.html", word=word, artworks=[],
                               message=f'No artworks found for "{word}". Try a different word.')

    return render_template("results.html", word=word, artworks=artworks, message=None)

Three things to check

results.html. Make sure it has the {% if message %} block right after </form> (from my last message). The route sends message to the template, so without that block the messages won’t show.
# AI-written on home(). Your teacher allowed AI for it, so I marked it. If you rewrite the route by hand later, remove the tag.
You still owe the explanation comments. The assignment wants # comments in your own words on the parts that matter: what each function or route does and why, and any line that handles user input or errors. Good places are the .strip() line, the timeout=10, the try/except, and the if error and if not artworks checks.

To run it

cd "/Users/won23/hcde310 GitHub/hcde.310/hw4"
flask --app app run

Then search “lion”, try an empty search, and try 12345678901234. Commit if it works, and tell me if you get an error.

////// I uploaded a screeshot of error, after i ran it

AI response: 
The last line of the traceback says what’s wrong: TemplateNotFound: results.html. Flask looks for that file in templates/ and it doesn’t exist yet. I only gave you the skeleton version in pieces, so you never created it.

The traceback also shows app.py line 79, the final return render_template(...) with message=None. To get there, the search worked and the API sent back artworks. Only the template is missing.

Create hw4/templates/results.html (right-click templates in the Explorer, choose New File, and name it results.html), then paste this complete version:

html
<!-- AI-written -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Results - Art Institute of Chicago Search</title>
  <style>
    .grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }
    .card img, .no-image { width: 100%; height: 200px; object-fit: cover; background: #ddd; }
    .no-image { display: flex; align-items: center; justify-content: center; }
  </style>
</head>
<body>
  <main>
    <form action="/results" method="get">
      <label for="q">Search for artwork</label>
      <input type="text" id="q" name="q" value="{{ word }}">
      <button type="submit">Search</button>
    </form>

    {% if message %}
      <p role="alert">{{ message }}</p>
    {% endif %}

    <div class="grid">
      {% for a in artworks %}
        <div class="card">
          {% if a.image_id %}
            <img src="https://www.artic.edu/iiif/2/{{ a.image_id }}/full/400,/0/default.jpg"
                 alt="{{ a.title or 'Untitled artwork' }}">
          {% else %}
            <div class="no-image">No image available</div>
          {% endif %}
          <p>{{ a.title or "Untitled" }} by {{ a.artist_title or "Unknown artist" }}
             ({{ a.date_display or "Unknown date" }}) - {{ a.place_of_origin or "Unknown place" }}</p>
        </div>
      {% endfor %}
    </div>
  </main>
</body>
</html>

Then:

Save the file. The folder should now have templates/home.html and templates/results.html.
Stop the server (Ctrl+C in the terminal) and start it again with flask --app app run. Or just refresh the browser, since Flask reads templates fresh each time.
Search “lion” again. You should see up to 12 cards in 3 columns.

Then run the other checks:

Empty box or only spaces: the “Please type a word” message.
12345678901234: the “No artworks found” message.
Broken URL (change artworks/search to artworkz/search in app.py, search, then change it back): the error message with 404.

The grid shows 12 cards by default. If you see a different number, tell me...

After that it worked. 
Things that surprised me: 
The first run crashed with TemplateNotFound: results.html. The AI had o
only given me parts of the template, and I hadn't created the file.

What I changed myself:
Fixed plan.md(table, headings, my own wording)
the API gave me 10 results, not 12 like the AI said. I added limit": 12 to get my 3x4 grid


/////
In the home page, there is one search bar, a heading, and large image area for place holder.
in the results page, search bar stays at the top with the term filled in (user input), then a 3x4 grid of cards, showing 12 total. Each card has an image(image_id.) and a caption that explains the title by artist (date) - place to the user.

The image URL https://www.artic.edu/iiif/2/{image_id}/full/400,/0/default.jpg. 
 image_id to fields= parameter, and note it can be null

 search_artworks("monet") returns a non-empty list and None.
search_artworks("12345678901234") returns [] and None.
Temporarily misspell the URL and confirm you get [] plus a message, not a traceback

Field - Shown on - If null
title - card caption - “Untitled”
artist_title - card caption - “Unknown artist”
date_display - card caption - “Unknown date”
place_of_origin - card caption - “Unknown place”
image_id - card image - gray box + “No image available"