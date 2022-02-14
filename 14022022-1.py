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

print("We are going to generate 4 lists of random numbers. Would you choose some boundaries for me?")

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

print("\nNice! All done!")
