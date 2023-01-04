def add_dots(input_string):
    # Initialize an empty result string
    result = ""

    # Iterate through the input string
    for char in input_string:
        # Add the current character and a dot to the result string
        result += char + "."

    # Return the result string
    return result

def remove_dots(input_string):
    # Remove all dots from the input string and return the result
    return input_string.replace(".", "")

#string = "test"
#print(add_dots(string))		#t.e.s.t
#print(remove_dots(add_dots(string)))	#test