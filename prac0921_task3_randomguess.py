# random guessing game
# between 1 and 100
# too high, too low or correct


# think of a random number
# import random
# secret_num = random.randint(1, 100)
# attempts = 1

# while attempts < 11:
#     print("This is attempt #:", attempts)
#     guess = int(input("What is the number? "))

#     if guess > secret_num:
#         print("Your guess is too high. ")
#     elif guess < secret_num:
#         print("Your guess is too low.")
#     else:
#         print("Your guess is correct")
#         break
#     attempts += 1
# else:
#     print("You lost the game")
# guess
# attempts














# import random
# secret_num = random.randint(1, 100)
# print(secret_num)
# attempts = 1
# while attempts < 11:
#     guess = int(input("What is your guess? "))
#     if guess > secret_num:
#         print("your guess is too high. ")
#     elif guess < secret_num:
#         print("Your guess is too low. ") 
#     else:
#         print("your guess is correct. ")
#         break
# else:
#     print("you have lost. ")



# ask for a guess
# check if higher lower or correct
# loop to ask 10 times



# total = 0
# days_without_rainfall = 0
# highest_rainfall = 0
# average_rainfall = 0
# num_of_days = int(input("Enter the number of days: "))
# for i in range(num_of_days):
#     rainfall = float(input("Enter the amount of rainfall: "))
#     total = total + rainfall
#     if rainfall == 0:
#         days_without_rainfall += 1
#     if rainfall > highest_rainfall:
#         highest_rainfall = rainfall
#     average_rainfall = total / num_of_days
               

            

# print("Total rainfall is %d mm."%total)
# print("There are ", days_without_rainfall, "days without rain.")
# print("Highest rainfall collected is ", round(highest_rainfall, 1))
# print("Average rainfall collected is", round(average_rainfall, 2))


##############################################################
'''
The task is to edit program code so that countries and their capital cities can be added to or removed 
from a dictionary. 
The following program has a dictionary that contains countries and their capital cities. The program 
allows the user to:
• input a country
• input whether they want to remove a country and its capital city from the dictionary
• input whether they want to add a country and its capital city to the dictionary.
'''
# capital_cities = {
#  'singapore':'Singapore',
#  'japan':'Tokyo',
#  'australia':'Canberra',
#  'england':'London',
#  'france':'Paris',
#  'germany':'Berlin'
# }
# country = input("Please enter the name of a country: ").lower()
# remove = input("Would you like to remove any of the entries? (Y or N): ")
# add = input("Would you like to add a new entry? (Y or N): ")

'''
Task 3.1
Edit the program so that it:
• converts the input for country to lower case
• searches the dictionary for the country input and outputs the capital city of that country.
[3]
Save your program.
'''    
# capital_cities = {
#  'singapore':'Singapore',
#  'japan':'Tokyo',
#  'australia':'Canberra',
#  'england':'London',
#  'france':'Paris',
#  'germany':'Berlin'
# }
# country = input("Please enter the name of a country: ").lower() 
# remove = input("Would you like to remove any of the entries? (Y or N): ")
# add = input("Would you like to add a new entry? (Y or N): ")
# if country in capital_cities:
#     capital = capital_cities[country]
#     print("The capital of", country, "is", capital)

'''
Task 3.2
Copy and paste your program from sub-task 3.1.
Edit the program so that if the user enters the value ‘Y’ for remove, the program:
• allows the user to input a country they want to remove from the dictionary
• converts the country input to lower case
• removes the country from the dictionary that is input by the user.
[3]
Save your program.
 '''
# capital_cities = {
#  'singapore':'Singapore',
#  'japan':'Tokyo',
#  'australia':'Canberra',
#  'england':'London',
#  'france':'Paris',
#  'germany':'Berlin'
# }
# country = input("Please enter the name of a country: ").lower() 
# remove = input("Would you like to remove any of the entries? (Y or N): ")
# if remove == Y:
#     abc = input("Enter the country you want to remove from the dictionary. ").lower()
# for abc in capital_cities:
#     remove(abc)
# add = input("Would you like to add a new entry? (Y or N): ")
# if country in capital_cities:
#     capital = capital_cities[country]
#     print("The capital of", country, "is", capital)
'''
Task 3.3
Copy and paste your program from sub-task 3.2 .
Edit the program so that if the user enters the value ‘Y’ for add, the program:
• allows the user to input a country they want to add to the dictionary
• allows the user to input the capital city for the country they want to add
• adds the country and its capital city to the dictionary in the format country:capital
• outputs the dictionary at the end of the program.
[4]
'''




















# total_sum = 0
# counter = 0
# smallest_even_num = 101
# biggest_even_num = 0
# numinputs = int(input("How many numbers? "))
# while counter < numinputs:
#     number = int(input("Enter an even integer: "))
#     if number % 2 == 0 and number >= 2 and number <= 100):
#         print("The number is even. ")
        
#         if number < smallest_even_num:
#             smallest_even_num = number
#         if number > biggest_even_num:
#             biggest_even_num = number
#         total_sum += number
#         counter += 1
#     else:
#         print("The number is not even. Please send an even number. ")
     
     
                  

    
# print("The biggest even number is ", biggest_even_num)
# print("The smallest even number is ", smallest_even_num)
# print("Total sum is ", total_sum)






# total_sum = 0
# counter = 0
# bignum = 0
# smallnum = 101
# while counter < 5:
#     number = int(input("Enter an even integer: "))
#     if number % 2 == 0 and number > 1 and number < 101:
#         print("The number is even and between 2 and 100. ")
#         if number > bignum:
#            bignum = number
#         if number < smallnum:
#             smallnum = number
#         total_sum += number
#         counter += 1
#     else:
#         print("The number is not even or not between 2 and  100. ")
    

# print("the biggest even integer is ", bignum)
# print("the smallest even integer is ", smallnum)
# print("The total sum is", total_sum)


# total_sum = 0
# inputnum = int(input("How many numbers? "))
# counter = 0
# bignum = 0
# smallnum = 101
# while counter < inputnum:
#     number = int(input("Enter an even integer: "))
#     if number % 2 == 0 and number > 1 and number < 101:
#         print("The number is even and between 2 and 100. ")
#         if number > bignum:
#            bignum = number
#         if number < smallnum:
#             smallnum = number
#         total_sum += number
#         counter += 1
#     else:
#         print("The number is not even or not between 2 and  100. ")
    

# print("the biggest even integer is ", bignum)
# print("the smallest even integer is ", smallnum)
# print("The total sum is", total_sum)










