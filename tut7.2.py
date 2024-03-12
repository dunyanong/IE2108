def merge2(A, m, n):
    if m > n:
        s = n
    else:
        s = m
    
    B = []
    if m < n:
        for i in range(s):
            B.append(A[i])
    else:
        for i in range(s):
            B.append(A[m+i])
        for i in range(m-1, -1, -1):
            A[n+i] = A[i]
        
    return sorted(B + A[:n])


# Example inputs
A = [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]
m = 7
n = 3

# Call the merge2 function
result = merge2(A, m, n)

# Print the result
print("Merged Array:", result)

