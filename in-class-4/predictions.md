# Class 4: Five broken snippets

Your name: Won Kim
Collaborator: Roger Tang

# Part 1: Predict

**Don't run anything yet.** Read each snippet in `exercise.py` and write your guesses. A wrong guess is fine: the point is to compare.

## Snippet 1
- Which line breaks? print("Find it in room " + exhibit["Room"]) will break
- What error will Python show? (the kind and the message)  type error
- What's the fix? make it into lowercase "r"

## Snippet 2
- Which line breaks? print("Find it in room " + exhibit["room"])
- What error will Python show? (the kind and the message) type error
- What's the fix? use the get. to get the room number 

## Snippet 3
- Which line breaks? for i in range(len(exhibits) + 1):
- What error will Python show? (the kind and the message) index out of range
- What's the fix? get rid of + 1 

## Snippet 4
- Which line breaks? print(count_visits(visit, 243))
- What error will Python show? (the kind and the message) name error
- What's the fix? add "s" at the end of visit. 

## Snippet 5
- Which line breaks?    print(longest)
- What error will Python show? (the kind and the message) type error?
- What's the fix?   return instead of print

# Part 2: Run

Run `python3 exercise.py`. Python stops at the first error, so fix that snippet in `exercise.py`, run again, and see the next one. Fill in what actually happened.

## Snippet 1
- Which line broke? print("Find it in room " + exhibit["Room"])
- What error did Python show? KeyError: 'Room'
- What's the fix? print(f"Find it in room {exhibit['room']}")


## Snippet 2
- Which line broke?     print("Find it in room " + exhibit["room"])
- What error did Python show? TypeError: can only concatenate str (not "int") to str
- What's the fix? print(f"Find it in room {exhibit['room']}")

## Snippet 3
- Which line broke?     print(i + 1, exhibits[i])
- What error did Python show? IndexError: list index out of range
- What's the fix? getting rid of + 1 ... for i in range(len(exhibits)):

## Snippet 4
- Which line broke?     print(count_visits(visit, 243))
- What error did Python show? NameError: name 'visit' is not defined. Did you mean: 'visits'?
- What's the fix? fix the name from visit to "visits"

## Snippet 5
- Which line broke?     print(title.upper())
- What error did Python show? AttributeError: 'NoneType' object has no attribute 'upper'
- What's the fix? Change print(longest) to -> return longest

When all five are fixed, run `python3 check.py` until it says ✓.

Bonus: Snippet 5 prints something *before* it crashes. What, and why does it still crash?

# Part 3: Tutor practice (one snippet)

Pick one snippet. Write your guess first, then ask your tutor. Paste the chat (or a share link) below.

- Snippet #: 5 
- Our guess before asking: the print(longest) should be return longest
- Chat: https://claude.ai/chat/bfbcdfaa-16f7-446f-9bc0-c7773e2d9860
- Did it give you too much? What did you do? I asked it to explain it more easily and it
gave me a scenario to think on, and or kind of error I asked it for what are some examples of error that are possible and it explained a few so I could figure out the correct type.
