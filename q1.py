def swap(x, y):
    """
    Swaps the values of x and y if they are numeric.
    Returns -1 if not numeric.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1
    
    # Swap values
    x, y = y, x
    
    print("x:", x, "y:", y)
    return

# Case 1: Not numeric
print(swap("Apple", 10))   # should return -1

# Case 2: Numeric
swap(9, 17)                # should print swapped values
