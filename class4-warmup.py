def label(year):
    if year < 1900:
        return "old"
    return "modern"

print(label(1889),label(1942))

#label(1889): Since 1889 is less than 1900, 
#   the if condition evaluates to True and it returns "old".

#label(1942): Since 1942 is not less than 1900, 
#   the if condition evaluates to False, skips to the next line, and returns "modern".

titles = ["Nighthawks", "The Bedroom", "Sky above Clouds IV"]
for t in titles:
    if "the" in t.lower():
        print(t)

def titles_with(word, titles):
    """ Returns a list of titles with the word in it """
    titles_with_word = []
    for t in titles:
        if word in t.lower():
            titles_with_word.append(t)
    return titles_with_word

print(titles_with("the", titles))

myList = ["cats", "dogs", "goats"]
for i in myList:
    print(f"{i + 1}. {myList[i]}")
