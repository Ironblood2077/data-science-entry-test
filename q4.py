def string_reverse(s):
    """
    Reverse a given string.
    Return -1 if s is not a string.
    """
    if not isinstance(s, str):
        return -1
    return s[::-1]
# Case 1
print(string_reverse("Hello World"))  
# Expected: "dlroW olleH"

# Case 2
print(string_reverse("Python"))  
# Expected: "nohtyP"
