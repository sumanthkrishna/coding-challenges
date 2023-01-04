def count(input_string):
    # Split the input string by hyphens
    syllables = input_string.split("-")

    # Return the length of the syllables list
    return len(syllables)
	
# print(count("ho-tel"))   #2