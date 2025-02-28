def invert_dictionary(example_dict):
    inverted_dict = {}
    for key, value in example_dict.items():
        if value not in inverted_dict:
            inverted_dict[value] = []
        inverted_dict[value].append(key)
    return inverted_dict

example_dict = {"Alice": 10, "Bob": 20, "Charlie": 10, "David": 30}
print("Inverted Dictionary:", invert_dictionary(example_dict))
