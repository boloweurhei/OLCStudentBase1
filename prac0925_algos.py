'''
max in list
min in list
sum of list
count of list
average of list
position of max in list
position of min in list

split a list without split()


Practice 1

list1 = [2944, 5490, 2357, 2619, 1177, 451, 8299, 2533, 4682, 6040,
         5972, 7532, 4382, 8311, 6664, 4918, 3656, 3769, 6179, 7720,
         1777, 7149, 2175, 8665, 4586, 5208, 320, 1314, 8950, 4884,
         756, 6196, 5935, 5291, 8619, 2630, 1831, 3127, 4698, 6291,
         2478, 5792, 9362, 7348, 8040, 3556, 598, 6187, 8959, 880,
         6601, 538, 3439, 8508, 8649, 5139, 8076, 78, 6776, 362,
         6368, 6460, 8604, 1763, 1713, 2354, 2167, 6612, 8149, 7961,
         4270, 5285, 7346, 5667, 2102, 900, 8063, 4577, 2285, 9592,
         5671, 537, 9777, 9421, 5455, 1241, 990, 3745, 8443, 4213,
         4183, 2463, 9562, 8137, 5101, 397, 6966, 9927, 7473, 4105]

## Question: Find the maximum number in this list
'''
list1 = [2944, 5490, 2357, 2619, 1177, 451, 8299, 2533, 4682, 6040,
         5972, 7532, 4382, 8311, 6664, 4918, 3656, 3769, 6179, 7720,
         1777, 7149, 2175, 8665, 4586, 5208, 320, 1314, 8950, 4884,
         756, 6196, 5935, 5291, 8619, 2630, 1831, 3127, 4698, 6291,
         2478, 5792, 9362, 7348, 8040, 3556, 598, 6187, 8959, 880,
         6601, 538, 3439, 8508, 8649, 5139, 8076, 78, 6776, 362,
         6368, 6460, 8604, 1763, 1713, 2354, 2167, 6612, 8149, 7961,
         4270, 5285, 7346, 5667, 2102, 900, 8063, 4577, 2285, 9592,
         5671, 537, 9777, 9421, 5455, 1241, 990, 3745, 8443, 4213,
         4183, 2463, 9562, 8137, 5101, 397, 6966, 9927, 7473, 4105]
# maxnum = 0
# for i in list1:
#     if i > maxnum:
#         maxnum = i
# print(maxnum)
    
# minnum = 1000000000000000000
# for i in list1:
#     if i < minnum:
#         minnum = i
# print(minnum)

# sum = 0
# for i in list1:
#     sum += i
# print(sum)



# count = 0
# for i in list1:
#     count += 1
# print(count)

# list1.index(maxnum) # list

# print(list1.index(maxnum))

# print(list1.index(minnum))


'''
Practice 2

word_list = [
    "swimming", "jumping", "hearth", "magnify", "education", "important", "programming", "development",
    "implementation", "strategy", "technology", "platform", "hardware", "software", "interface", "database",
    "network", "internet", "protocol", "algorithm", "analysis", "function", "variable", "constant",
    "structure", "integer", "floating", "boolean", "string", "character", "operation", "encryption",
    "security", "authentication", "authorization", "firewall", "encryption", "decryption", "integrity",
    "availability", "confidentiality", "phishing", "malware", "virus", "spyware", "adware", "ransomware",
    "debugging", "testing", "deployment", "backup"
]

## Question 1: Find the length of the longest word in this list.



## Question 2: Check if there are multiple words with the longest length.
## If there are, print out all the words with the longest length

# Challenge 1: 
- Count the number of vowels in each word. 
- Return the word containing the most vowels.
        e.g. adware = vowel count is 3 (a, a, e)
- If there are multiple words that contains the most number of vowels, 
output all the words into a list and display it.
'''


word_list = [
    "swimming", "jumping", "hearth", "magnify", "education", "important", "programming", "development",
    "implementation", "strategy", "technology", "platform", "hardware", "software", "interface", "database",
    "network", "internet", "protocol", "algorithm", "analysis", "function", "variable", "constant",
    "structure", "integer", "floating", "boolean", "string", "character", "operation", "encryption",
    "security", "authentication", "authorization", "firewall", "encryption", "decryption", "integrity",
    "availability", "confidentiality", "phishing", "malware", "virus", "spyware", "adware", "ransomware",
    "debugging", "testing", "deployment", "backup"]
    
# to find the length of list/ string


# howlong = len(word_list[i])
#  for i in range(len(word_list)):
# for i in range(len(word_list)):
#     print(len(word_list))
        


#sentence2 = "the capital of china is beijing and the capital of japan is tokyo" # original sentence

# splitted = sentence1.split(" ")
# print(splitted)

sentence = "the,capital,of,china,is,beijing,and,the,capital,of,japan,is,tokyo," # original sentence
delim = ","
tempstring = '' # temporary string
listsentence = [] # empty list to hold the result

# use an algorithm to split a sentence into a list using a delimiter
# # BUT WITHOUT USING split() function

# loop through every single character in this sentence
for s in sentence:
    # check if this current character is the delimiter
    if s == delim:
        #pass # i'll fill in this code later
        listsentence.append(tempstring)
        tempstring = '' # clear out, so i can handle the next word

    else:
        # this is not a delimiter

        # construct the word between the delimiter
        tempstring = tempstring + s
        print(tempstring)

# manually add the last one
#listsentence.append(tempstring)
print(listsentence)