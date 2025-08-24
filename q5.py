def check_divisibility(num, divisor):
    """
    Check if num is divisible by divisor.
    Return -1 if inputs are not numeric.
    """
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        return -1
    
    return num % divisor == 0
# Case 1: 10 divisible by 2
print(check_divisibility(10, 2))  # Expected: True

# Case 2: 7 divisible by 3
print(check_divisibility(7, 3))   # Expected: False
