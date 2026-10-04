# AI log

## HW0: Class 1, build an app with AI

Paste every prompt you sent, in order, with the AI's replies. A share link to the chat is fine too, but paste the prompts here either way. Your thinking about it goes in `day1.md`.

**Share link (optional):**

### Prompt 1

Build a single-page interactive web app. It calls the Art Institute of Chicago API (https://api.artic.edu/api/v1/artworks/search) when the user searches or filters, and shows results with images. Keep it under ~150 lines. It's for [who want to search up artwork assoicated with the keyword and ] who want to [learn information about it]. My sketch is attached; follow it. Explain how the code works in plain language, section by section.

```

**AI's reply:**
I'm still trying to get your HEIC sketch decoded, since the usual converters here are failing. Next I'll try a couple of other routes.

I built the app as one HTML file of 145 lines. I couldn't test the live API calls because this environment has no internet. The script passes a syntax check, but the Art Institute filters are untested. The type filter is the one I'm least sure about. Open the file in your browser on a normal connection to try it. Claude's hosted preview blocks requests to outside sites, so the search won't work there.

Following your sketch
Title: "Art Institute of Chicago API" sits at the top left.
Search bar: a pill-shaped box with the magnifier at its right end.
Filter button: the small box beside the bar opens a filter panel.
Cards: a three-column grid, with the image above two lines of text (title and artist). It drops to two columns and then one on smaller screens.
Stars: each image has a star in its top-right corner.
Load more: a button at the bottom brings in the next batch. I used this for the partial bottom row in your sketch.
Learn more: clicking an image opens a detail window. This wasn't in your sketch, but it's how you learn about the artwork.
How the code works

1. The HTML structure (lines 40–66). This is the skeleton from your sketch: heading, search form, a hidden filter panel, a status line, an empty grid and a hidden "Load more" button. A <dialog> element at the bottom holds the detail window. Nothing is loaded until the user acts.

2. The CSS (lines 8–38). A few colours and sizes are defined once at the top. The grid is three equal columns with breakpoints for narrower screens. Each card is a white frame on a grey "gallery wall". The star is placed in the frame's corner and turns red when starred. I added a visible focus outline so the page works with a keyboard.

3. The setup (lines 68–76). This sets the API address and the list of fields to request (title, artist, date, medium and so on). Asking only for these keeps responses small. seen remembers every artwork shown so a click can look it up, and stars remembers the ones you starred. esc makes text safe to place in the page, and pic builds the image address from an artwork's image ID.

4. The search function (lines 78–96). This is the part that calls the API. It builds the address from the keyword plus any filters:

The type dropdown and the "Public domain only" box add extra conditions.
It shows "Searching…" while it waits.
It drops results that have no image.
It draws the cards.
It hides "Load more" on the last page.
If something fails, it shows a plain message instead of breaking.

5. Drawing cards (lines 98–107). card turns one artwork into a framed image with a star and two lines of text. draw puts the cards in the grid, either replacing the old ones or adding to them for "Load more".

6. The detail window (lines 109–118). showInfo fills the dialog with a large image, the title, artist and a list of date, medium, origin, dimensions and credit. It adds the museum's description (with its formatting stripped) and a link to the artwork's page on artic.edu.

7. Wiring up the controls (lines 120–142).

Submitting the form, changing a filter or pressing "Load more" each run a search.
The filter button shows and hides the panel.
"Starred only" shows your saved artworks without calling the API.
One click listener on the grid handles every card, so new cards work without extra setup. A click on the star saves or unsaves the artwork. A click on the image opens the detail window.

Stars are kept in memory only, so they reset when you reload the page.
Artwork search
Code·HTML 
### Prompt 2

```
Screenshot 2026-10-03 at 7.33.21PM.png
Build a single-page interactive web app. It calls the Art Institute of Chicago API (https://api.artic.edu/api/v1/artworks/search) when the user searches or filters, and shows results with images. Keep it under ~150 lines. It's for [who want to search up artwork assoicated with the keyword and ] who want to [learn information about it]. make artwork more informative. My sketch is attached; follow it. Explain how the code works in plain language, section by section.
```

**AI's reply:**

I'll update the existing app so each artwork shows more, from the card up to the detail window, and keep it under 150 lines.

Edited a file, shared a file, and 5 more steps
I updated artwork-search.html (147 lines) so each artwork tells you more. The layout still follows your sketch. The script passes a syntax check, but I haven't run it against the live museum API from here. Open the file in your own browser to try it. If a field doesn't show up for some artworks, that's the first thing to check.

What's more informative
On each card: the second line now shows the artist and the date together (for example, "Vincent van Gogh · 1889"). The sketch has two lines of text under each image, so I kept it to two.
In the detail window, which opens when you click an image:
Style: for example Impressionism.
Type: for example painting or print.
Subjects: topics like landscapes, flowers or portraits.
See it in person: whether it's on view, and in which gallery.
Description: if the museum has no full description, it falls back to the short one.
Longer text: the window now scrolls if the description is long.
How the code works, section by section
1. HTML (lines 51–69). This is the page from your sketch: title, search bar, filter button, an empty grid, and a "Load more" button. A hidden <dialog> at the end is the pop-up for details.

2. CSS (lines 8–48). This makes it look right: three columns, a white frame around each image, the star in the corner, and a pop-up that stays on screen and scrolls.

3. Setup (lines 71–79). The museum's address and the list of details to ask for. I added the new details here: style, type, subjects and gallery. Two memory lists keep track of artworks you've seen and starred.

4. search() (lines 80–99). The front desk. It writes a request from your keyword and filters, sends it to the museum, and shows the results. It skips artworks with no image and shows a message if the museum can't be reached.

5. card() and draw() (lines 101–109). card() builds one framed picture with its star, title, and artist and date. draw() puts the cards on the page.

6. showInfo() (lines 111–122). The information plaque. It builds a list of facts, leaves out any the museum doesn't have, and fills the pop-up with a big image, the facts, the description, and a link to the museum's page.

7. Event listeners (lines 123–144). The switchboard that connects your typing and clicks to the functions above.

Which section would you like to try explaining in your own words? I can check it and tell you what's right or missing.
Artwork search
Code·HTML 


(Copy the block above for more prompts.)
### Prompt 3
Build a single-page interactive web app. It calls the Art Institute of Chicago API (https://api.artic.edu/api/v1/artworks/search) when the user searches or filters, and shows results with images. Keep it under ~150 lines. It's for [who want to search up artwork assoicated with the keyword and ] who want to [learn information about it]. But can you make it so that each row has 4 artwork instead of 3, so the user can look at more artwork at once. My sketch is attached; follow it. Explain how the code works in plain language, section by section.

**AI's reply:**

The grid now shows four artworks per row, and the file is 148 lines. The script passes a syntax check, but I haven't viewed the page or run it against the live museum API from here, so open the file in your own browser to see how it looks.

What changed
Four columns: the desktop grid went from three to four. The "Load more" batch is still 12 artworks, so it fills exactly three rows of four.
Wider page: I made the page wider (from 1000px to 1240px) so four cards don't get squeezed.
Smaller screens: the grid steps down to three columns, then two, then one as the screen narrows. The sketch doesn't show this, but four columns on a phone would be unreadable.

The title, pill-shaped search bar, filter button, stars and "Load more" button all stay as in your sketch.

How the code works, section by section

1. HTML (lines 52–70). This is the skeleton from your sketch: title, search bar, filter button, an empty grid and a "Load more" button. The hidden <dialog> at the end is the pop-up for artwork details.

2. CSS (lines 8–49). This controls how it looks. The key line is grid-template-columns:repeat(4,1fr), which means "make four equal columns." The @media lines below it are rules for narrower screens that change the number to 3, 2, or 1.

3. Setup (lines 72–80). The museum's address and the list of details to ask for (title, artist, date, style, subjects, gallery and so on). Two memory lists keep the artworks you've seen and the ones you've starred.

4. search() (lines 81–100). The front desk. It builds a request from your keyword and filters, sends it to the museum, and waits. It skips artworks with no image, hands the rest to the display code, and shows a message if the museum can't be reached.

5. card() and draw() (lines 102–110). card() builds one framed picture with its star, title, and artist and date. draw() places the cards in the grid, which lays them out four across.

6. showInfo() (lines 112–123). The information plaque. It lists the facts the museum has for that artwork (style, medium, subjects, whether it's on view) and leaves out any it doesn't have. It then fills the pop-up with a big image, the description, and a link to the museum's page.

7. Event listeners (lines 124–145). The switchboard that connects your typing and clicks to the functions above: search, filters, "Load more", stars and opening the pop-up.

Which section would you like to explain back to me in your own words? I'll tell you what's right and what's missing.

Artwork search
Code·HTML 