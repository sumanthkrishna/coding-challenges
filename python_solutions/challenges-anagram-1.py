def is_anagram(string1, string2):
    # Convert both strings to lowercase and sort their characters
    string1 = sorted(string1.lower())
    string2 = sorted(string2.lower())

    # Check if the sorted strings are equal
    return string1 == string2

#print(is_anagram("typhoon", "opython")) #True
#print(is_anagram("Alice", "Bob")) 		 #False