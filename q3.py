def update_dictionary(dct, key, value):
    """
    Updates dictionary with a key-value pair.
    Prints original value if key exists, then updates.
    """
    if key in dct:
        print("Original value:", dct[key])
    dct[key] = value
    return dct
# Case 1: Add new key
print(update_dictionary({}, "name", "Alice"))
# Expected: {"name": "Alice"}

# Case 2: Update existing key
print(update_dictionary({"age": 25}, "age", 26))
# Expected print: Original value: 25
# Expected return: {"age": 26}
