import json
from mainProj1 import checkingPerLetters

f = open('sample.json')
sortedWords = json.load(f)

y = {"Simp" : "Someone who does way too much for a person they like."}

sortedWords.update(y)

sorting = list(sortedWords.keys())

checkingPerLetters(sorting)

newlySorted = {key:sortedWords[key] for key in sorting}

with open("sample.json", "w") as outfile:
    json.dump(newlySorted, outfile)

print("New Word, Already Added!")