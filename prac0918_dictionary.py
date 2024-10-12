# using for loop

# print numbers from 0 - 9

# print numbers from 2 - 15

# print odd numbers from 1 to 37

# print every character from the word "SINGAPORE"

# for i in range(10):
#     print(i)

# for i in range(2, 16):
#     print(i)

# for i in range(1, 38, 2):
#     print(i)

# for i in "SINGAPORE":
#     print(i)

# using while loop
# print numbers from 0 - 9
# count = 0

# while count < 10:
#     print(count)
#     count = count + 1 # the variable count is equal to the value of count + 1


# print numbers from 2 - 15
#count = 0
#while count > 1 and count < 16:
# while count < 16:
#     print(count)
#     count = count + 1


# print odd numbers from 1 to 37
# count = 1
# while count < 38:
#     if count % 2 == 1:
#         print(count)
#     count = count + 1
#     # print(count)
#     # count = count + 2

##################################################
'''
################ Define a dictionary ###############
Define a dictionary named menu which will store a food item and price of food

'hamburger' costs 10
'pizza' costs 18.5
'lasagne' costs 25.70
'fries' costs 5
'''
# write and test your code here 

# menu = {'hamburger': 10,
#         'pizza': 18.5,
#         'lasagne': 25.70,
#         'fries': 5}
# print(menu)


'''
################ Retrieve values from a dictionary ###############
Print out the price of Lasagne only
Print out the price of Fries only
'''
# menu = {'hamburger': 10,
#         'pizza': 18.5,
#         'lasagne': 25.70,
#         'fries': 5}
# print(menu['lasagne'])



'''
########### Change the value of a dictionary key ###############
Change the price of hamburger to 20
Change the price of Fries to 3
'''
# write and test your code here 
# menu = {'hamburger': 10,
#         'pizza': 18.5,
#         'lasagne': 25.70,
#         'fries': 5}
# menu['hamburger'] = 20
# print(menu)

'''
############ Increase the value of a dictionary key ############
Increase the price of Lasagne by 5
Decrease the price of Pizza by 3
'''
# menu = {'hamburger': 10,
#         'pizza': 18.5,
#         'lasagne': 25.70,
#         'fries': 5}
# menu['lasagne'] = menu['lasagne'] + 5
# print(menu)



'''
############### Add a new key/ Value to the dictionary #####################
Add a new menu item => Pasta which cost 15
Add a new menu item => Sandwich which cost 6
'''
# menu = {'hamburger': 10,
#         'pizza': 18.5,
#         'lasagne': 25.70,
#         'fries': 5}
# menu['pasta'] = 15
# print(menu)

'''
############### Add a new key/ Value to the dictionary #####################
Delete menu item Pasta
'''
# write and test your code here 
# menu = {'hamburger': 10,
#         'pizza': 18.5,
#         'lasagne': 25.70,
#         'fries': 5,
#         'pasta': 15}
# del(menu['pasta'])
# print(menu)
'''
########### Loop through to Retrieve Keys ##################
# Write a for loop, and only display the name of food item that you sell
# only display the keys
'''
# # menu = {'hamburger': 10,
#         'pizza': 18.5,
#         'lasagne': 25.70,
#         'fries': 5}
# for i in menu:
#     print(i)




'''
########### Loop through to Retrieve Values ##################
Write a for loop, and only print out the price
'''
#write and test your code here 
# menu = {'hamburger': 10,
#         'pizza': 18.5,
#         'lasagne': 25.70,
#         'fries': 5}
# for i in menu:
#     print(menu[i])
    




'''
########### Loop through to Retrieve Key and Values ##################
Write a for loop, and print out the menu key and values
e.g.
Hamburger costs $10.00
Pizza costs $18.50
'''
# write and test your code here 
# menu = {'hamburger': 10,
#         'pizza': 18.5,
#         'lasagne': 25.70,
#         'fries': 5}
# for i in menu:
#     print(i, 'costs', menu[i])


'''
#################### Challenge 1 ######################################
Write a program to calculate how much money you need to buy all the items in the menu.
'''
# write and test your code here 
# menu = {'hamburger': 10,
#         'pizza': 18.5,
#         'lasagne': 25.70,
#         'fries': 5}
# total = 0
# for i in menu:
#     total = total + menu[i]
# print("i need $", total, "to buy everything")


'''
############### Challenge 2 ##########################################
Write a program to determine the most expensive item in the menu
'''
# write and test your code here 
# menu = {'hamburger': 10,
#         'pizza': 18.5,
#         'lasagne': 25.70,
#         'fries': 5}
# num = 0
# expitem = ''
# for i in menu:
#     if menu[i] > num:
#         num = menu[i]
#         expitem = i
# print("the most expensive item is", expitem,"costing $", num)

'''
################ Challenge 3 ########################################
#### Due to inflation, prices have increased. Update all the prices by 10%
'''
# write and test your code here 
menu = {'hamburger': 10,
        'pizza': 18.5,
        'lasagne': 25.70,
        'fries': 5}
for i in menu:
    menu[i] = menu[i] * 1.1
print(menu)


'''
################ Challenge 4 ########################################
Upgrade this system where you ask customers what they want, and display the price 
# you can check if a key exists in a dicionaty, by using the 'in' keyword
# for example: if 'hamburger' in menu: will return true if hamburger exists 

Example:

Hello, What is your name? John
>>> Hi John, what would you like to eat? Laksa
>>> I'm sorry John, we don't sell Laksa. 

Hi John, what would you like to eat? Hamburger
>>> Great choice! Please pay $10.00. Your order will be delivered soon!
Hi John, what would you like to eat? Exit

Ok, bye!

### CHALLENGE: implement a wallet feature, so you have limited money to buy the item
Keep asking until no more money to buy

'''
# write and test your code here 
