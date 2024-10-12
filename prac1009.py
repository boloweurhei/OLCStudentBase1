'''
program refinement
write a program to ask for height(meters) again and again in 
 - input height (m), keep asking until the person says stop
 - Your program will output the average height

 - your program will say if the height is more than average, less than average or average
# > average = 1.9, < average = 1.5

The program will ask you to input a height, and tell you if
- you are above or below the average height
'''

# total_height = 0 # used for average calculation
# height_count = 0
# highest = 1.9
# lowest = 1.5

# # again and again, while True
# for i in range(5):
#     height = float(input("Enter a height: "))

#     if height > highest:
#         print("Your height is higher than the average. ")
#     elif height < lowest:
#         print("Your height is lower than average. ")
#     else:
#         print("Your height is average.")

#     # calculate the total height
#     total_height += height # keep adding the heights into total_height
#     height_count += 1 # keep count of how many height added

# print("The average height of the 5 heights is {}m".format(round(total_height/ height_count, 1)))




'''
development of program
you are writing a program to keep track of the distance and time of a cycling 
competition. 

Write a program to input distance (km), and time (mins) into  2 list, 
You will keep asking for distance and time, until the user say stop

After this you have to calculate the average time taken by the cyclist

Your answer must be in hours and minutes. 
e.g. 61 minutes => 1 hour and 1 minute

'''
# time is 9.8 hours
# import math
# distance = []
# time = []
# c = 0 
# while True:
#     dis = float(input("What is the distance? "))
#     tim = float(input("What is the time? "))
#     distance.append(dis)
#     time.append(tim)
#     stop = input("Enter 'y' to continue and 'n' to stop. ")
#     if stop == 'n':
#         break
# for i in time:
#     c += i
# avgtime = c / len(time)
# # calculate the average time taken


# hourvalue = math.floor(avgtime)
# minute = (avgtime % 1) * 60
# print("Average time is", hourvalue,"hours and", round(minute), "minutes. ")


# given a certain number of minutes, output, how many hours and minutes
# e.g. 61 minute is 1 hour and 1 minute
# import math
# minutes = int(input("Enter the number of minutes: "))
# days = minutes / (60 * 24)
# hours = math.floor(days / 24)
# minute = ((minutes / 60) % 1) * 60
# print(math.floor(days), "days")
# print(hours, "hours")
# print(round(minute), "minutes")