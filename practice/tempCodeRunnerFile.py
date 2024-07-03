import json
from mainProject1_copy import words,checkingPerLetters

f = open('sample.json')

y = {"Ampago":"Nak nang tokwa"}

sortedWords = json.load(f)

sortedWords.update(y)

sorting = list(sortedWords.keys())

checkingPerLetters(sorting)

print({key:sortedWords[key] for key in sorting})
