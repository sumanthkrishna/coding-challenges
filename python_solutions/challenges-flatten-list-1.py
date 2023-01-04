def flatten(input_list):
    # Initialize an empty result list
    result = []

    # Iterate through the input list
    for item in input_list:
        # If the item is a list, flatten it and add its elements to the result list
        if isinstance(item, list):
            result.extend(flatten(item))
        # If the item is not a list, add it to the result list
        else:
            result.append(item)

    # Return the result list
    return result

#input_list = [[1, 2, 3], [4, 5], [6, 7, 8, [9, 10]]]
#print(flatten(input_list))   #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
