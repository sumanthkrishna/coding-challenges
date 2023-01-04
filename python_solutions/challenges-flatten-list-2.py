def flatten(outer_list):
    return [
        item
        for inner_list in outer_list
        for item in inner_list
    ]