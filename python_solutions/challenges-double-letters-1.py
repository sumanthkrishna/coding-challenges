def double_letters(input_string):
    # Iterate through the input string
    for i in range(len(input_string) - 1):
        # Check if the current character and the next character are the same
        if input_string[i] == input_string[i + 1]:
            # If they are the same, return True
            return True

    # If no pair of identical letters was found, return False
    return False

#print(double_letters("hello"))   # False
#print(double_letters("nono"))	  # True
