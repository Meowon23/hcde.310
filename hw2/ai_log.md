# HW2 Part 6 – AI log (`ai_log.md`)

The tutor walks you through the routine (Try → Predict → Run → Explain → Log) as you chat, so your transcript shows most of it. In `ai_log.md`:

---

## 1. One prediction
*copy one prediction you made in a chat. Were you right? If not, what surprised you?*
for 2nd part of part4, I asked AI if it starts with counts = {} and I was right. 


## 2. What clicked
*pick one thing you were stuck on or didn't know. Without looking at the transcript, explain it in your own words.*
It was bit hard to figure out how to start, so I had to ask AI on where to begin

## 3. Too much?
*Did the tutor ever give you too much? What did you do? (one line)*
I think in a way? when it told me about:
Here’s the overall shape of the function, with the middle left for you: then it pretty much told me most of the work

## 4. Transcripts
*paste every tutor chat you used for HW2 (one is fine if that's all you had)*
ok on to 

def count_by_artist(artworks):
    """TODO: one line saying what it takes and what it returns."""
    pass
Here’s a hint for the last line. You already know this word from works_by:

python
    return titles
That line handed the finished list back to whoever called the function. Part 3 ended with print(counts), which only shows the dictionary on screen. For this function, swap print for the word you just saw above, and hand back counts instead of titles.

Here’s the overall shape of the function, with the middle left for you:

python
def count_by_artist(artworks):
    counts = {}
    ...your loop from Part 3 goes here...
    return ____
Two things to keep in mind:

Everything under def is indented 4 spaces.
return lines up with for, not inside it. (You did exactly this in works_by.)
Your one job: paste your Part 3 loop, indented one level under counts = {}, and fill in the blank after return. Rough is fine.

def count_by_artist(artworks):
    counts = {}
    for i in range(len(artworks)):
        artist = artworks[i].get("artist", "Unknown")
        counts[artist] = counts.get(artist, 0) + 1
    print(counts)
    return titles
    pass

You’ve got the heart of the function right: counts = {}, the loop, and the two lines inside it are all correct, and return lines up with for. Three small things left, and I’ll take the first one.

Look at the return line. It says return titles. You wrote titles in works_by, where that was the list you built. But this function never creates anything called titles. Python would raise a NameError, which usually means “you used a name I don’t know.”

Predict: in count_by_artist, which variable holds the finished dictionary? Check the first line of the function body.

Your one job: tell me what should go after return.

Two things to look at after that, one at a time:

The print(counts) line is still inside the function. The caller already prints the result at the bottom of the file, so what do you think happens if both print?
pass is no longer needed. Do you remember why?
return counts

Yes, return counts is right. counts is the variable holding the finished dictionary, and return hands it back to whoever called the function.

Predict: look at the function as it stands, with the print(counts) line still above return. When the file runs print(count_by_artist(artworks)) at the bottom, how many times do you think the dictionary shows up on screen, and why?

Then one thing to fix at a time. Do you still need print(counts) inside the function? Think about who is already doing the printing. Tell me your answer, then paste the function with your changes.

After that, we’ll deal with pass.

no

Yes, you can take it out. The bottom of the file already has print(count_by_artist(artworks)), so that line does the printing. If the function prints too, the dictionary shows up twice, once from inside the function and once from the call at the bottom.

A function’s job here is to hand the answer back, not to display it.

Your one job: delete the print(counts) line. Then look at the end of the function and tell me what you think should happen to pass. It’s still there. Do you remember what you said about functions that have real code in them?

Paste the whole function when you’ve made both changes.

def count_by_artist(artworks):
    counts = {}
    for i in range(len(artworks)):
        artist = artworks[i].get("artist", "Unknown")
        counts[artist] = counts.get(artist, 0) + 1
    return counts
    pass
Yes, the function is correct. print(counts) is gone, and return counts lines up with for, so it hands back the finished dictionary after the loop ends.

What’s left: pass is still sitting after return. Earlier I said return exits the function immediately, so that line can never run. It’s harmless, but it’s leftover scaffolding from the starter file.

Predict: if you delete pass and run the file, will the output of print(count_by_artist(artworks)) change? Will it still print None, or something else?

Your one job: delete pass, run the file, and paste all three lines of output. Then check them yourself with python3 check.py and tell me whether it passes.

After that, there’s one last piece: the two TODO docstrings. Try writing the one for count_by_artist first, using the pattern “Takes ___ and returns ___.”