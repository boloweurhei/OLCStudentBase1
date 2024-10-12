'''
Task 3 - 2023

A mathematics program shown on page 7 creates 10 questions.
Each question is created by generating two random integers 
between 1 and 50 inclusive and adding them.

The program:
• outputs the questions
• allows the user to input their answer to each question
• outputs the user's total mark and the number of correct answers
• alters the output based on whether 1 or multiple correct answers are given.

If both random integers are greater than 25, the user gets 2 marks for a correct answer, 
otherwise, the user gets 1 mark for a correct answer.

If the user enters a correct answer:
• the total mark is incremented by the correct amount
• the text "Correct" is stored in a list, otherwise, 
  the text "Incorrect" is stored in the list.

When all questions have been answered, the list is searched to 
count how many times "Correct" is stored.
'''

import random
questions = 10
answer_list = []
correct = 0
incorrect = 0
total_mark = 0
for x in range(questions):
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    print("What is", num1, "+", num2, "?")
    user_answer = input()
    answer = num1 + num2
    if int(user_answer) == answer:
        if num1 > 25 and num2 > 25:
            total_mark = total_mark + 2
            answer_list = answer_list + ["Correct"]
        else:
            total_mark = total_mark + 1
            answer_list = answer_list + ["Correct"]
    else:
        answer_list = answer_list + ["Incorrect"]
list_length = len(answer_list) 
for i in range(list_length):
    if answer_list[i] == "Correct":
        correct = correct + 1
if correct  == 1:
    message = "answer."
else:
    message = "answers."
print("Your total mark is", total_mark, "and you had", correct, message)

'''
Open the file MATHS.py
Save the file asMYMATHS_2023_<your name>_<centre number>_<index number>.py

9.	Identify and correct the errors in the program so that 
it works according to the requirements given
Save your program.
[10 marks]

'''

'''

import random
questions = 10 # temp change this, remember to change back to 10
answer_list = [] 
correct = 0
incorrect = 0 # variable not used
total_mark = 0
for x in range(questions):  # 8. remove the -1
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    answer = num1 + num2 # 3. fixed answer variable
    print("What is", num1, "+", num2, "?")
    user_answer = input()
    if int(user_answer) == answer: # 9. int conversion for user_asnwer
        print("inside a")
        if num1 > 25 and num2 > 25: # 10 should be and condition
            print("inside b")
            total_mark = total_mark + 2
            answer_list = answer_list + ['Correct'] # 1. fixed quotation
        else:
            print("inside c")
            total_mark = total_mark + 1
            answer_list = answer_list + ['Correct'] # 11. need to count correct for 1 mark
    else:
        print("inside d")
        answer_list = answer_list + ["Incorrect"]
list_length = len(answer_list) #- 1 #2.  fixed minus sign, 4. list cannot minus 1
for i in range(list_length):
    if answer_list[i] == "Correct": # 7. index variable should be i
        correct = correct + 1 # 6. should correct += 1 
if correct  == 1: # 5. variable should use correct
    message = "answer."
else:
    message = "answers."
print("Your total mark is", total_mark, "and you had", correct, message)
'''