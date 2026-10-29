#The / route shows search form
# The /results route reads word user typed
#If word is empty or only spaces it show message and stop.
#Ask Piece A (the fetch function) to search API.
#If came back as an error: show a friendly message. the API call failed
#If came back as an empty list: show “no results. it worked but nothing matched.
#otherwise, /results route reads word user typed, and shows the results page with 3x4 image grid

import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# The info we ask the museum for on each artwork
FIELDS = "id,title,artist_title,date_display,place_of_origin,image_id"


# This sends search word to museum's API// then it gives back two things:
#  list of artworks + error message (None if nothing went wrong).
# Returning both lets  route tell " call failed" or  "no matches".

# AI-written
def search_artworks(term):
    url = "https://api.artic.edu/api/v1/artworks/search"
    params = {"q": term, "fields": FIELDS, "limit": 12}# requests puts the user's word into the URL safely
    headers = {"AIC-User-Agent": "HCDE310 student project"}

    try:
        # Give up after 10 seconds so the page doesn't freeze if the museum is slow
        response = requests.get(url, params=params, headers=headers, timeout=10)
    except requests.exceptions.RequestException:
        # No internet, bad URL, etc. Return a friendly message instead of crashing
        return [], "Could not reach the museum. Check your internet and try again."

    # 200 means museum said OK. Anything else means API error, 
    # code and reason (like 500 Internal Server Error) instead of using bad data
    if response.status_code != 200:
        return [], f"Sorry, there was a problem: {response.status_code} {response.reason}"

    data = response.json()
    return data["data"], None


# Shows home page with search form

# AI-written
@app.route("/")
def home():
    return render_template("home.html")


# Reads word from the form, searches, and shows results page
# //Every path sends message or artworks to results.html.

# AI-written
@app.route("/results")
def results():
    # The form send word in URL  .strip() removes spaces
    # ends so  word of only spaces counts as empty.
    word = request.args.get("q", "").strip()

    # Empty input don't call the API, just ask for a word
    if not word:
        return render_template("results.html", word=word, artworks=[],
                               message="Please type a word to search for.")

    artworks, error = search_artworks(word)

    # The API call failed, then it shows error message from search_artworks
    if error:
        return render_template("results.html", word=word, artworks=[], message=error)

    #  call worked but nothing matched so different message than an error
    if not artworks:
        return render_template("results.html", word=word, artworks=[],
                               message=f'No artworks found for "{word}". Try a different word.')

    # Success, it pass word too so search box stays filled in
    return render_template("results.html", word=word, artworks=artworks, message=None)