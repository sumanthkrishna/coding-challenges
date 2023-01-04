def middleLetter(input_string):
    # Get the length of the input string
    string_length = len(input_string)

    # If the length of the string is even, return the empty string
    if string_length % 2 == 0:
        return ""
    # If the length of the string is odd, return the middle letter
    else:
        return input_string[string_length // 2]

#input_string = "abcde"
#print(mid(input_string))

#input_string = "abcdef"
#print(mid(input_string))

#The first input string has an even number of letters, so the function returns the empty string. The second input string has an odd number of letters, so the function returns the middle letter "c".