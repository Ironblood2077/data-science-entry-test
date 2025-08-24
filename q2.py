def find_and_replace(lst, find_val, replace_val):
    """
    Replace all occurrences of find_val in lst with replace_val.
    Return -1 if lst is not a list.
    """
    if not isinstance(lst, list):
        return -1

    for i in range(len(lst)):
        if lst[i] == find_val:
            lst[i] = replace_val

    return lst

# Case 1: Replace numbers
print(find_and_replace([1, 2, 3, 4, 2, 2], 2, 5))
# Expected: [1, 5, 3, 4, 5, 5]

# Case 2: Replace strings
print(find_and_replace(["apple", "banana", "apple"], "apple", "orange"))
# Expected: ["orange", "banana", "orange"]
