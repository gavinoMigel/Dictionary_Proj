def insertionSort(words):
	n = len(words) 
	
	if n <= 1:
		return 

	for i in range(1, n): # Iterate over the array starting from the second element
		key = words[i] # Store the current element as the key to be inserted in the right position
		j = i-1
		while j >= 0 and key < arr[j]: # Move elements greater than key one position ahead
			arr[j+1] = arr[j] # Shift elements to the right
			j -= 1
		arr[j+1] = key # Insert the key in the correct position

# Sorting the array [12, 11, 13, 5, 6] using insertionSort
words = ["Application", "Apple"]
insertionSort(words)
print(words)
