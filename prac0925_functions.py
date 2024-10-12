### Basic 1: Functions with no parameters, no return value
'''
# Question 1: Declare a function that prints "Hello, World!" 
# and call the function.
# Example input: 
# Expected output: Hello, World!
'''
# Write your code here

def hello():
    # code that you want to run inside
    print("Hello world")
    print("sdf world")
    print("Hellfdsfsdfsdo world")
    print("Hellsdfsdfsdfso world")

# call the function
#hello()


### Basic 2: Functions with 1 or more parameters
'''
# Question 2: Declare a function greet that takes a 
# name as a parameter and prints a greeting message.
# Example input: name = 'John'
# Expected output: 'Hello, John!'
'''
# Write your code here
def hello(yourname, myname):
    print("Hello,",yourname)
    print("I am", myname)

hello("Alex","Ryan")

'''
# Question 3: Declare a function greet that takes yourname and myname
# as parameters and prints a introduction message.
# Example input: yourname = 'John', myname="Marcus"
# Expected output: 'Hello, John! I'm Marchus, nice to meet you!'
'''
# Write your code here


### Basic 3: Functions with parameters and return value

'''
# Question 4: Declare a function that takes two numbers 
# as parameters and returns their sum.
# Example input: a = 5, b = 3
# Expected output: 8
'''
# Write your code here
def add(num1, num2, num3):
    output = num1 + num2 + num3
    return output

num1 = add(2,3,4)
num2 = add(5,6,7)
num3 = add(23,43556,456457)
num4 = add(234,56,35)
num5 = add(34,6545,74)

print(num1 + num2 + num3 + num4 + num5)

#print(add(5, 3)) #this code will test your function

'''
# Question 5: Declare a function that takes a number as a parameter 
# and returns True if the number is even, otherwise False.
# Example input: number = 4
# Expected output: True
'''
# Write and test your code here
def isiteven(num):
    if num % 2 == 0:
        return True
    else:
        return False

num = int(input("WHat is the number? "))
print(isiteven(num))


'''
# Question 6: Declare a function that takes a list of numbers 
as a parameter and returns the sum of the list.
# Example input: numbers = [1, 2, 3, 4, 5]
# Expected output: 15
'''
# Write and test your code here


'''
# Question 7: Declare a function that takes a string 
# as a parameter and returns the string in uppercase.
# Example input: text = 'hello'
# Expected output: 'HELLO'
'''
# Write and test your code here


'''
# Question 8: Declare a function that takes a number as a
parameter and returns a string "positive" if the number is positive, 
"negative" if the number is negative, and "zero" if the number is zero.
# Example input: number = -1
# Expected output: 'negative'
'''
# Write and test your code here


'''
# Question 9: Declare a function that takes two numbers as 
# parameters and returns the larger number.
# Example input: a = 7, b = 10
# Expected output: 10
'''
# Write and test your code here


'''
# Question 10: Declare a function that takes a 
# list of strings as a parameter and returns the first longest string.
# Example input: strings = ['apple', 'banana', 'cherry']
# Expected output: 'banana'
'''
# Write and test your code here


'''
# Question 11: Declare a function that takes a string 
# and a number as parameters 
# and returns the string repeated that many times.
# Example input: text = 'abc', count = 3
# Expected output: 'abcabcabc'
'''
# Write and test your code here


'''
# Question 12: Declare a function that takes a 
# list of numbers as a parameter and returns the average of the list.
# Example input: numbers = [1, 2, 3, 4, 5]
# Expected output: 3.0
'''
# Write and test your code here


'''
# Question 13: Declare a function that takes a string 
# as a parameter and returns the string reversed.
# Example input: text = 'hello'
# Expected output: 'olleh'
'''
# Write and test your code here


'''
# Question 14: Declare a function that takes a list of 
# numbers as a parameter and returns the smallest number.
# Example input: numbers = [3, 1, 4, 1, 5]
# Expected output: 1
'''
# Write and test your code here


'''
# Question 15: Declare a function that takes a list of 
# numbers as a parameter and 
# returns a new list with each number squared.
# Example input: numbers = [1, 2, 3]
# Expected output: [1, 4, 9]
'''
# Write and test your code here



'''
Question 16: Create a function that calculates the area of a triangle
parameters: base, height
return: 0.5 x base x height

Use this function to add up 3 triangle's areas
triangle1 is base 20, height 34
triangle2 is base 30, height 87
triangle3 is base 44, height 99
'''
# Write and test your code here


'''
Question 17: Write a function that calculates the total cost
after tax for a list of prices.
#[20084, 45000, 660000, 93938, 737362, 8373628]
#10% tax

Parameters: prices (list of floats), tax_rate (float)
Return: total_cost (float)
'''
# Write and test your code here


'''
Question 18: Construct a function that reverses the items in a list.
You are not allowed to use list slicing or reverse

Parameters: inarray(list)
Return: modified_list

inarray = [1,2,3,4,5]
outarray = [5,4,3,2,1]
'''
# Write and test your code here


'''
Question 19: Construct a function that reverses the characters in a string.
You are not allowed to use list slicing or reverse.
convert the output into lowercase

Parameters: instring(string)
Return: outstring(string)

instring = "BAZOOKA"
outstring = akoozab
'''
# Write and test your code here


'''
Question 20: Create a function that continuously asks the user to 
input a valid email address until one is entered.

Parameters: 
Return: email (str)
'''
# Write and test your code here


'''
Question 21: Create a function to calculate the sum of 
all even numbers in a given list.
Parameters: numbers (list of integers)
Return: sum_of_evens (int)

Example:
numbers = [1, 2, 3, 4, 5, 6]
sum_of_evens = 12
'''
# Write and test your code here


'''
Question 22: Write a function that finds the smallest number in a list.
Parameters: numbers (list of integers)
Return: smallest (int)

Example:
numbers = [34, 79, 23, 54, 12]
smallest = 12
'''
# Write and test your code here



'''
Question 23: Develop a function that determines if a word is a palindrome.
Parameters: word (str)
Return: is_palindrome (bool)

Example:
word = "radar"
is_palindrome = True
'''
# Write and test your code here



'''
Question 24: Create a function that takes a list of words and 
returns a list of their lengths.
Parameters: words (list of str)
Return: lengths (list of int)

Example:
words = ["hello", "world", "python", "excellent"]
lengths = [5, 5, 6, 9]
'''
# Write and test your code here



'''
Question 25: Write a function that multiplies all numbers in a list together.
Parameters: numbers (list of floats)
Return: product (float)

Example:
numbers = [1.5, 2.0, 4.0]
product = 12.0
'''
# Write and test your code here



'''
Question 26: Develop a function that formats a date 
from YYYYMMDD to "DD/MM/YYYY" format.
Parameters: datestr (str)
Return: formatted_date (str)

Example:
datestr = "20230424"
formatted_date = "24/04/2023"
'''
# Write and test your code here
