words = ["Application", "Apple", "Applied", "Acupuncture"]

def insertionSort(words):
    n = len(words)

    if n <= 1:
        return 

    for i in range(1, n):
        selected_word = words[i]
        j = i - 1

        while j >= 0 and selected_word < words[j]:
            words[j + 1] = words[j]
            j -= 1
        
        words[j + 1] = selected_word

insertionSort(words)
print(words)
