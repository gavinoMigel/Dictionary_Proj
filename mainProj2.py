import json
from mainProj1 import checkingPerLetters

f = open('sample.json')
sortedWords = json.load(f)

y = {"Amobot":"Voting for the wrong person"}

sortedWords.update(y)

sorting = list(sortedWords.keys())

checkingPerLetters(sorting)

newlySorted = {key:sortedWords[key] for key in sorting}

with open("sample.json", "w") as outfile:
    json.dump(newlySorted, outfile)

print(newlySorted)
#I have something to say; This is a testing.