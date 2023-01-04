def online_count(statuses):
    # Initialize a counter to keep track of the number of people online
    online_count = 0

    # Iterate through the dictionary
    for name, status in statuses.items():
        # If the status is "online", increment the counter
        if status == "online":
            online_count += 1

    # Return the number of people online
    return online_count

#Here is an example of how you can use this function:
#statuses = {
#    "Alice": "online",
#    "Bob": "offline",
#    "Eve": "online",
#}
#print(online_count(statuses))

#This would output the following:  2