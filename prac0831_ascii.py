#computhink student portal chapter 4 (programming) 
# x = 5
# print(x)

# name = 'alice'
# print(name)

# a = 17
# b = 26
# print(a + b)

# first_name = 'john'
# last_name = 'tan'
# print(first_name, last_name)

# name = 'john'
# age = 30
# print("Hello,", name, ". You are", age , "years old.")

# x = 5
# print(x)
# x = x + 3
# print(print(x), x)

# pi = 3.14159
# r = 5
# circumference = 2 * pi * r
# print(circumference)

# user_name = input("What is your name: ")
# print("Hello,", user_name, "!")


tele_num = '934(4930)4'
for i in tele_num:
    if i == '(' or i == ')' or i == ' ':
        del(i)
print(tele_num)