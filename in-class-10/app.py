from flask import Flask, render_template, request
from api import get_books   # later: from api import get_books_real as get_books

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/results")
def results():
    # 1. Read the search term from the form
    author = request.args.get("author_search", "").strip()

    # 2. Empty input
    if not author:
        return render_template(
            "home.html",
            message="Please type an author's name first, like Ferrante or Toni Morrison.")

    # 3. Call the API
    books = get_books(author)

    # 4. API error
    if books is None:
        return render_template(
            "home.html",
            message="We couldn't reach Open Library right now. Wait a minute and try your search again.")

    # Missing fields: skip books with no title, fill in a missing year
    clean_books = []
    for book in books:
        title = book.get("title")
        if not title:
            continue
        year = book.get("first_publish_year") or "year unknown"
        clean_books.append({"title": title, "year": year})

    # 5. No results, or nothing useful to show
    if len(clean_books) == 0:
        return render_template(
            "home.html",
            message=f"No books found for \"{author}\". Check the spelling, or try just the last name.")

    # 6. Show the results
    return render_template("results.html", books=clean_books, author=author)