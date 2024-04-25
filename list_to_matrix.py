def reverse_string(s):
    s = list(s)
    
    # Initialize two pointers
    left, right = 0, len(s) - 1
    
    # Swap characters using the two pointers until they meet in the middle
    while left <= right:
        # Swap characters at left and right pointers
        s[left], s[right] = s[right], s[left]
        # Move the pointers inward
        left += 1
        right -= 1
    
    # Convert the list of characters back to a string
    return  s

# Example usage:
input_string = "hello0"
reversed_string = reverse_string(input_string)
print("Original string:", input_string)
print("Reversed string:", reversed_string)
