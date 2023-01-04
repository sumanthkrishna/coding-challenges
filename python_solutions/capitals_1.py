def capitals(inputString):
    # Create an empty list to store the capital letters and their positions
    capital_letters = []

    # Iterate through the input string
    for i in range(len(inputString)):
        # Check if the current character is a capital letter
        if inputString[i].isupper():
            # If it is a capital letter, add it to the list along with its position
            capital_letters.append((inputString[i], i))
    # Return the list of capital letters and their positions
    return capital_letters
	
#Run the Example

#inputString = "Hello World"
#print(capitals(inputString))
#This would output the following list: [('H', 0), ('W', 6)], which are the capital letters "H" and "W" and their positions in the input string "Hello World".