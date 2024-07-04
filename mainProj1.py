import json # Using json to save the sorted words

words = {
    "Bet":"Agreement or approval.  Can be said as a question to ask if someone wants to do something or confirm.", 
    "Clout": "Influence or power, especially in social media.", 
    "Keri":"Can Do it All", 
    "Charot":"Kidding Around", 
    "Dasurv":"Deserve", 
    "Flex":"To show off or boast.",
    "Aesthetic":"Concerning the appreciation of beauty or good taste", 
    "AFAM":"A Foreigner Assigned to Manila", 
    "Alam Na This":"We all know what’s gonna happen.", 
    "Anyare":"What happened?", 
    "Apakaganda":"Very Beautiful",
    "Forda... Ang Ferson":" 'for the person' Indicates what the person are up to."}

slangWords = list(words.keys())

def checkingPerLetters(slangWords):
    n = len(slangWords) # checking the length of the list. This will be the indicator when to stop knowing that the sorting is done

    if n <= 1: 
        return

    for i in range(1, n):
        selected_word = slangWords[i]
        j = i - 1

        # Move words[j] to words[j + 1] until the right position for selected_word is found
        while j >= 0:
            compared_word = slangWords[j]

            # Compare character by character
            char_index = 0
            while char_index < min(len(selected_word), len(compared_word)): # Finding the length of both words and set as the criteria.
                if selected_word[char_index] == compared_word[char_index]: # If the character is the same; 
                    char_index += 1                                        # It will increment by one
                else:
                    break

            # Determine if we need to move the selected_word
            if char_index < min(len(selected_word), len(compared_word)): # char_index
                if selected_word[char_index] < compared_word[char_index]: # the currect index of index of the word
                    slangWords[j + 1] = compared_word # {Apple,Apple.Application}
                    j -= 1  # j = -1 since the initial of j is 0
                else:
                    break
            else:
                if len(selected_word) < len(compared_word): 
                    slangWords[j + 1] = compared_word  # j = 0 which is index 0
                    j -= 1
                else:
                    break

        slangWords[j + 1] = selected_word

checkingPerLetters(slangWords)

updated_words = {key: words[key] for key in slangWords}
with open("sample.json", "w") as outfile:
    json.dump(updated_words, outfile)