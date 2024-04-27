def reverse_string(s):
    # Initialize two pointers
    left = 0
    right = len(s) - 1
    
    s = list(s)
    
    # Loop until the pointers meet or cross
    while left < right:
        # Swap characters at left and right pointers
        s[left], s[right] = s[right], s[left]
        
        # Move the pointers towards each other
        left += 1
        right -= 1
    
    # Convert the list back to string
    return "".join(s)

# Example usage:
s = "hello"
reversed_s = reverse_string(s)
print("Reversed string:", reversed_s)