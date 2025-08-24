def find_first_negative(lst):
    """
    Find the first negative number in a list using while loop.
    """
    i = 0
    while i < len(lst):
        if lst[i] < 0:
            return lst[i]
        i += 1
    return "No negatives"
# Case 1: Has negatives
print(find_first_negative([3, 5, -1, 7, -2, 8]))  
# Expected: -1

# Case 2: No negatives
print(find_first_negative([2, 10, 7, 0]))  
# Expected: "No negatives"
