"""
Context: we have finished the if statement lessons and then started working on data structures like lists
"""

# Exercise 8 of Intro to Programming module
# Write a list generator that creates 2 lists of only strings and 2 lists of only numbers
# Does it work to generate a list that mixes strings and numbers?
# Credit also goes to https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits/2257449

import random
from random import randint
import string
'''
#letters
def rando(size=random.randint(2, 10), chars=string.ascii_lowercase):
    return "".join(random.choice(chars) for _ in range(size))

#numbers
def rando(size=random.randint(2, 10), chars=string.digits):
    return "".join(random.choice(chars) for _ in range(size))

# mixed
def rando(size=random.randint(2, 10), chars=string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))
'''
# print(rando())

'''Get some lists from the user by combining the input and range function'''

print("We are going to generate 4 lists of numbers. Would you choose some boundaries for me?")

#get user input
print("Ok, list 1...")
list1=list(range(int(input("Lower bound of this range?: ")),int(input("Upper Bound of this range?: ")), int(input("And increment?: "))))
print(list1)

#do it the other times
print("Now, list 2...")
list2=list(range(int(input("Lower bound of this range?: ")), int(input("Upper Bound of this range?: ")), int(input("And increment?: ")) ))
print(list2)

print("Ok, list 3...")
list3=list(range(int(input("Lower bound of this range?: ")),int(input("Upper Bound of this range?: ")), int(input("And increment?: ")) ))
print(list3)

print("Ok, list 4...")
list4=list(range(int(input("Lower bound of this range?: ")),int(input("Upper Bound of this range?: ")), int(input("And increment?: ")) ))
print(list4)

print("Ok, list 5...")
list5=list(range(int(input("Lower bound of this range?: ")),int(input("Upper Bound of this range?: ")), int(input("And increment?: ")) ))
print(list5)

print("Ok, list 6...")
list6=list(range(int(input("Lower bound of this range?: ")),int(input("Upper Bound of this range?: ")), int(input("And increment?: ")) ))
print(list6)

#User is demonstrated what the append and extend methods do
print("We will now 'mix' this up a bit:")
print("List concatenations using .append")
print("List 1:List 3")
list1.append(list3)
print(str(list1))
print("List 2:List 4")
list2.append(list4)
print(str(list2))

print("Now we're going to experiment with .extend:")
print("Extension: 1(5)")
list1.extend(list5)
print(str(list1))
print("Extension: 2(6)")
list2.extend(list6)
print(str(list2))

print("As you can see from our results, appendages add the entire list as an entry")
print("While extending a list adds the entries of the extended list")
print("as entries in the new list.")
print("NOTE: Our data remain unchanged as the script runs")
#print("\nNice! All done!")

'''
"Slicing" is the practice of getting specific entries of a list
and is demonstrated by
e.g.
list2=list(list1[0:8])
print(list2)            # now you have created a new list by slicing and printed it!
'''

#User-defined slice
print("Ok, let's do a slice of the most recently printed list.")
print("Please give me two numbers in ascending order. Lowest must be zero.")
print(list2[int(input("1st one? ")):int(input("2nd one? "))])
