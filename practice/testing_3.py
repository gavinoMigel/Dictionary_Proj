words = ["Application", "Apple", "Applied", "Acupuncture"]

def insertionSort(words):

    n = len(words)

    if n <= 1:
	    return 

    for i in range (1,n):
        j = i-1
        selected_words = words[i]
        compared_words = words[j]

    #Already defined index 0 and 1; next is compare per letter
        while selected_words [j] == compared_words[j] :
    #Check per Letter in of word in index 0 and word in index 1
            if compared_words[j] != selected_words[j] :
                movement_decision = compared_words[j] > selected_words[j]
                if movement_decision == False:
                    print("No Exchange Happened!")
                else:
                    selected_words[i] , compared_words[j] = compared_words[j], selected_words[i]

insertionSort(words)
print 
    