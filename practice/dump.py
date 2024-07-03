from mainProject1_copy import checkingPerLetters,slangWords,words


checkingPerLetters(slangWords)
updated_words = {key: words[key] for key in slangWords}
print(updated_words)

#slangWords = sortedWords.update()
#checkingPerLetters(slangWords)
#print({key:words[key] for key in sortedWords})