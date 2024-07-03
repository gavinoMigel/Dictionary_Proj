words = ["Application", "Apple", "Applied", "Acupuncture"]

def checkingPerLetters(words):
    n = len(words)

    if n <= 1:
        return

    for i in range(1, n):
        selected_word = words[i]
        j = i - 1

        # Move words[j] to words[j + 1] until the right position for selected_word is found
        while j >= 0:
            compared_word = words[j]

            # Compare character by character
            char_index = 0
            while char_index < min(len(selected_word), len(compared_word)):
                if selected_word[char_index] == compared_word[char_index]:
                    char_index += 1
                else:
                    break

            # Determine if we need to move the selected_word
            if char_index < min(len(selected_word), len(compared_word)):
                if selected_word[char_index] < compared_word[char_index]:
                    words[j + 1] = compared_word
                    j -= 1
                else:
                    break
            else:
                if len(selected_word) < len(compared_word):
                    words[j + 1] = compared_word
                    j -= 1
                else:
                    break

        words[j + 1] = selected_word

checkingPerLetters(words)
print(words)
