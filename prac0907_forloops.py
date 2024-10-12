'''
# Question 1: Print numbers from 0 to a given number (exclusive)
# Test case 1: example input: 5, example output: 0 1 2 3 4
# Test case 2: example input: 3, example output: 0 1 2
'''
## Write and test your code here
#num = int(input)
#for i in range(num):
 #   print(i)

'''
# Question 2: Print numbers from a given start number 
# to a given stop number (exclusive)
# Test case 1: example input: 3 8, example output: 3 4 5 6 7
# Test case 2: example input: 1 5, example output: 1 2 3 4
'''
## Write and test your code here

#for i in range(3, 8):
 #   print(i)

'''
# Question 3: Print even numbers from 0 to a given number (exclusive)
# Test case 1: example input: 10, example output: 0 2 4 6 8
# Test case 2: example input: 7, example output: 0 2 4 6
'''
## Write and test your code here

#for i in range(2, 20 , 2):
  #  print(i)

'''
# Question 4: Print numbers from a given start number 
# to a given stop number (exclusive) with a given step
# Test case 1: example input: 2 10 2, example output: 2 4 6 8
# Test case 2: example input: 1 10 3, example output: 1 4 7
'''
## Write and test your code here
#num = int(input("What is the start number? "))
#num2  = int(input("What is the stop number? "))
#num3  = int(input("What is the step number? "))

#for i in range(num, num2, num3 ):
 #   print(i)

'''
# Question 5: Print the squares of numbers from 
# 0 to a given number (exclusive)
# Test case 1: example input: 5, example output: 0 1 4 9 16
# Test case 2: example input: 3, example output: 0 1 4
'''
## Write and test your code here

#num = int(input("What is the number? "))

#for i in range(num):
#    print(i**2)



'''
# Question 6: Print the cubes of numbers from a 
# given start number to a given stop number (exclusive)
# Test case 1: example input: 1 5, example output: 1 8 27 64
# Test case 2: example input: 2 6, example output: 8 27 64 125
'''
## Write and test your code here

#num = int(input("What is the start number? "))
#num2 = int(input("What is the stop number? "))

#for i in range(num, num2):
 # print(i**3)


'''
# Question 7: Print numbers in reverse from 
# a given start number to 0 (inclusive)
# Test case 1: example input: 5, example output: 5 4 3 2 1 0
# Test case 2: example input: 3, example output: 3 2 1 0
'''
# ## Write and test your code here
# num = int(input("What is the start number? "))

# #for i in range(num, -1, -1):
#  #   print(i)

'''
# Question 8: Print the even numbers from a 
# given start number to a given stop number (exclusive)
# Test case 1: example input: 2 10, example output: 2 4 6 8
# Test case 2: example input: 1 7, example output: 2 4 6
'''
## Write and test your code here

#num1 = int(input("What is the start number? "))
#num2 = int(input("What is the stop number? "))
#for i in range(num1, num2, 2):
  # print(i)





# for i in range(2, 49, 2):
#     print(i)

num1 = int(input("Enter a start number: "))
num2 = int(input("Enter a stop number: "))
num3 = int(input("Enter a step number: "))
for i in range(num1, num2, num3):
    print(i**2)