words = ["Application", "Apple", "Applied", "Acupuncture"]


def checkingPerLetters(words):
    firstWord = words[0]
    secondWord = words[1]

    if firstWord[4] == secondWord[4]:
        print(firstWord[4])
    else:
        greater = firstWord[4] > secondWord[4]
        if greater == False:
            print("No Exchange happened!")
        else:
            words[0], words[1] = words[1], words[0] 

checkingPerLetters(words)
print(words)
