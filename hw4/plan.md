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


