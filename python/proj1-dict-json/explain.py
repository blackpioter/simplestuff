import json
from difflib import get_close_matches

def print_ans(ans):
    if isinstance(ans, str):
        print(ans)
    else:
        for i in range(len(ans)):
            print("%s. %s" % (i+1, ans[i]))


def suggest(word):
    try:
        suggestion = get_close_matches(word, jp.keys(), cutoff=0.8)[0]
    except IndexError:
        suggestion = []
    return suggestion


def explain(word):
    suggestion = suggest(word)
    if word in jp:
        return jp[word]
    elif word.title() in jp:
        return jp[word.title()]
    elif word.upper() in jp:
        return jp[word.upper()]
    elif len(suggestion) > 0:
        ans = str(input("%s not found. Did you mean %s (Y/n)? " % (word, suggestion)) or "Y")
        if ans in ("Y", "y"):
            return jp[suggestion]
        else:
            return "Such word does not exist in our dictionary"
    else:
        return "Such word does not exist in our dictionary"

fd = open("data.json")
jp = json.load(fd)

word = input("Please provide word: ")
print_ans(explain(word))

fd.close()
