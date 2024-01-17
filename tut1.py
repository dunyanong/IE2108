""""
Create the following variables:
p = "Hello Singapore!"
pp = "I'm learning Python."
q = 10
r = 10.2
"""

p = "Hello Singapore!"
pp = "I'm learning Python."
q = 10
r = 10.2

"""
Display the variables, just make sure the variables are as what I expect.
"""

print(p)
print(pp)
print(q)
print(r)

"""
Display p + pp 
"""
print(f"p + pp: {p + pp}")

"""
Display q + r 
"""
print(f"q + r : {q + r}")

"""
Display range(10).
"""
print(range(10))

"""
Display list(range(10))
"""
print(list(range(10)))

"""
Modify the above statement to display [1, 3, 5, 7, 9].
"""
print(list(range(1, 10, 2)))

"""
Modify the above statement to display [20, 18, 16, 14, 12].
"""
print(list(range(20, 11, -2)))

"""
Create a list b with the following elements: 'data', 'and', 'book', 'structure', 'hello', 'st'.
Display it to make sure that your command worked. 
"""
print(['data', 'and', 'book', 'structure', 'hello', 'st' ])

"""
Append a number 32 to the end of the list and verify your command works
"""
data = ['data', 'and', 'book', 'structure', 'hello', 'st' ]
data.append(32)
print(data)

"""
What is the meaning of b[2:3]? 
"""
b = [0, 1, 2, 3, 4]
result = b[2:3]
print(result)

"""
Remove the 3rd element of the list.
"""
c = [0, 1, 2, 3, 4]
c.pop(2)
print(c)

"""
Use a different command to remove the 1st element of the list.
"""
d = [1, 2, 3, 4, 5]
d = d[1:]
print(d)

"""
Display the number of elements in the list (the length of the list).
"""
e = [1, 2, 3, 4, 5]
print(f"length: {len(e)}")

"""
For the following 2 values, check whether both are greater than 0
"""
a = 32
b = 132
if (a > 0 and b > 0): print("both are greater than 0")

"""
For the following 2 values, check whether at least one is greater than 0
"""
a = 32
b = -32
if (a >0 or b > 0): print("at least one is greater than 0.")


"""
What data type is person defined below?
"""
person = {}
print(type(person))

"""
Display person after the following.
person['firstname'] = 'Jacky'
person['lastname'] = 'Chan'
person['age'] = 69
person['address'] = ['Hong Kong']
"""
person['firstname'] = 'Jacky'
person['lastname'] = 'Chan'
person['age'] = 69
person['address'] = ['Hong Kong']
print(person)

"""
Display his first name.
"""
print("First name: " + person["firstname"])

"""
Write a basic calculator that performs addition, subtraction, multiplication, and division.
"""
def calculator(val1, val2, operator):
    if (operator == '+'): print(val1 + val2)
    elif (operator == '-'): print(val1 - val2)
    elif (operator == '*'): print(val1 - val2)
    elif (operator == '/'): print(val1 / val2)

calculator(1, 2, '/')

"""
Generate and print the first n numbers in the Fibonacci sequence
which is 0, 1, ..., with each subsequent number equal to the sum of
the previous 2 numbers. 
"""
def fibonaccci(n):
    if (n == 0 or n == 1): return n
    
    return fibonaccci(n - 1) + fibonaccci(n - 2)

print(fibonaccci(4))


"""
Check if a given string is a palindrome (reads the same forwards and backwards).
"""
def is_palindrome(input):
    left = 0
    right = len(input) - 1
    
    while(left < right):
        if (input[left] != input[right]): return False
        
        left += 1
        right -= 1

    return True

print(is_palindrome("ollo"))

"""
Write a simple game where the user tries to guess a randomly generated number.
The program first selects a random number without telling you the number.
You make a guess. The program will tell you if too high or too low, until
you guess it right.
Hint: Use the following:
import random (for importing a library on random numbers)
random.randint(1, 100) (for generating a random integer between 1 and 100, including both 1 and
100 themselves.)
"""
import random
def random_number_game():
    answer = random.randint(1, 100)
    user_number = 0

    while (answer != user_number):
        user_number = int(input("Guess Number: "))        
        if (user_number > answer): print("Too high")
        elif(user_number < answer): print("Too low")
        else: 
            print("correct")
            break
    
random_number_game()