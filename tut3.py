"""
Suppose that an array s contains float values. Write a Python program that prints the
sum of the first 𝑚 float elements of s.
"""
p = [1.0, 2.0, 5.0, 6.0, 7.0]
sum = 0
for i in range (3):
    sum += p[i]
    
print(sum)

"""
Write a Python program that prints the smallest and largest values in the array S that
stores m unique elements.
"""
p = [1, 6, 2, 9, 8]
p = sorted(p)

print("Smallest: ", p[0])
print("Largest: ", p[-1])

"""
Given an integer array s with length n > 1 such that s[i] ≤ s[i + 1] for all i. Write a
Python program to insert an input value x into the array so that the property s[i] ≤
s[i + 1] is maintained for all i.
"""


schools = "EEE MAE CEE NBS"
days = "Mon\nTue\n\tWed\nThu\nFri\n\tSat\nSun"

print(schools)
print(days)
print("""
Mary had a little lamb, little lamb, little lamb.
Mary had a little lamb, its fleece was white as snow. And everywhere that Mary went. Mary went. Mary went. And everywhere that Mary went, the lamb was sure to go. """)

age = int(input("How old are you? "))
weight = float(input('How much do you weight (in kg)? ')) 
print(f"So, you are {age} years old and weight {weight} kg.")

def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b
def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b
def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b
def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b
print("Let's test these functions!") 
age = add(20, 5)
height = subtract(1.80, 0.04)
weight = multiply(32, 2)
iq = divide(300, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")
print("False" == 1)
print("True" == 1)
print(1 != 10 or 30 < 4) # != stands for not equal print(not("False" != "True"))

count = [1, 2, 3, 4]
fruits = ["apples", "pears", "melon", "kiwi"] 
word = "testing"
new_word = ""

for number in count:
    print(number, end=" ")
print("\n")
for fruit in fruits:
    print(f"I like {fruit}!")
for char in word:
    new_word = char + new_word
print(new_word*3) # can you predict this output