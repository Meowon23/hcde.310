# Using the Open Library API in a Project

## What it is + why a designer might care

Open Library is a free, open catalog of books run by the Internet Archive. It has search, works, editions, authors, subjects, and cover images, and nearly every Open Library page has a JSON version. For a designer, that means you can build book-discovery tools (search, browse by subject, show covers) without a paid account or API key, and the data is structured enough to design real interfaces around: titles, authors, publication years, subjects, and cover art.

Docs: https://openlibrary.org/developers/api

## Setup

There is no API key and no account. only need Python and `requests`.

```
pip install requests
```

## One working example

```python
import requests, json

headers = {"User-Agent": "HCDE310-P0 (won23@uw.edu)"} 

ol = requests.get(
    "https://openlibrary.org/search.json",
    params={"q": "dune", "limit": 1,
            "fields": "key,title,author_name,first_publish_year,subject,cover_i"},
    headers=headers, timeout=10,
)
print(ol.url)
print(json.dumps(ol.json(), indent=2))
```

Output (trimmed to the f  irst three `subject` values; the real response may list more):

```json
{
  "numFound": 48299,
  "start": 0,
  "numFoundExact": true,
  "num_found": 48299,
  "documentation_url": "https://openlibrary.org/dev/docs/api/search",
  "q": "dune",
  "offset": null,
  "docs": [
    {
      "author_name": [
        "Frank Herbert"
      ],
      "cover_i": 11481354,
      "first_publish_year": 1965,
      "key": "/works/OL893414W",
      "title": "Dune",
      "subject": [
        "Dune (Imaginary place)",
        "Fiction",
        "Fiction, science fiction, general",
        "Dune (imaginary place), fiction",
        "New York Times reviewed",
        "Science fiction",
        "Science-fiction",
        "American literature",
        "nyt:mass-market-monthly=2021-11-07",
        "New York Times bestseller",
        "award:nebula_award=novel",
        "nyt:trade-fiction-paperback=2021-11-07",
        "Hugo Award Winner",
        "award:hugo_award=1966",
        "award:hugo_award=novel",
        "American Science fiction",
        "Long Now Manual for Civilization",
        "Ecology",
        "Fantasy fiction",
        "Large type books"
      ]
    }
  ]
}
```

How to read it:
- `numFound` is how many results matched in total (112), not how many came back (1, because of `limit=1`).
- `docs` is the list of results. Each one is a **work** (the book in general, not one specific printing).
- `author_name` and `subject` are **lists**, even when there is only one author.
- `cover_i` is a cover image ID. According to the Open Library covers docs, you can turn it into an image URL like `https://covers.openlibrary.org/b/id/<cover_i>-M.jpg` (`-S`, `-M`, `-L` for sizes).
- `key` is the work's ID, which you can use to link to or look up the book later.

Gotchas
## Gotchas

- Missing data:* Some books lack a cover, subject, or year. Use `doc.get("cover_i")`, not `doc["cover_i"]`, so your code doesn't crash.
- Too many matches:** Searching `dune` returned 48,299 results. Use `limit` and `fields`, and check the title and author before trusting the first result.
- 
Rate limits:** No key is needed, but heavy use can get you slowed or blocked. Send a `User-Agent` and don't loop requests quickly. Check the docs for current limits.
- 
Confusing docs:** The API info is spread across several pages. Start with `search.json` and change one parameter at a time.

Design angle

Project idea: A "find a book I can actually read" tool for students and people on a tight budget. The user searches by topic or title, and the app shows covers, authors, and publication years, then links out to the Open Library page for each book so they can see whether it can be borrowed or read online.

Ethical / UX consideration: 
Open Library's data is community-maintained, 
so don't hide books with missing covers or subjects. Show a placeholder 
instead, and link to the source page rather than promising a book is available.


AI use

I used Claude to help draft and structure this guide (the section outline, the gotchas wording, and the design-angle paragraphs). The code sample is my own code from P0, and I ran it myself and pasted the real output above.
