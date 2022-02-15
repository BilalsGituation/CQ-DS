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
list1=list(range(int(input("Lower bound of this range?: ")),int(input("Upper Bound of this range?: ")) + 1, int(input("And increment?: "))))
print(list1)

#do it the other times
print("Now, list 2...")
list2=list(range(int(input("Lower bound of this range?: ")), int(input("Upper Bound of this range?: ")) + 1, int(input("And increment?: ")) ))
print(list2)

print("Ok, list 3...")
list3=list(range(int(input("Lower bound of this range?: ")),int(input("Upper Bound of this range?: ")) + 1, int(input("And increment?: ")) ))
print(list3)

print("Ok, list 4...")
list4=list(range(int(input("Lower bound of this range?: ")),int(input("Upper Bound of this range?: ")) + 1, int(input("And increment?: ")) ))
print(list4)

print("Ok, list 5...")
list5=list(range(int(input("Lower bound of this range?: ")),int(input("Upper Bound of this range?: ")) + 1, int(input("And increment?: ")) ))
print(list5)

print("Ok, list 6...")
list6=list(range(int(input("Lower bound of this range?: ")),int(input("Upper Bound of this range?: ")) + 1, int(input("And increment?: ")) ))
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

print("As the results show, appendages nest an entire list as a last entry,")
print("while extending a list adds the individual entries of the list added")
print("as entries in the resulting list.")
print("NOTE: Our data remain unchanged as the script runs")
#print("\nNice! All done!")


'''"Slicing" is the practice of getting specific entries of a list
and is demonstrated by'''
'e.g.'
print('"Slicing" is the practice of getting specific entries of a list\nand is demonstrated by\ne.g.\nlist2=list(list1[0:8])\nprint(str(list2))"')
sloice=list(list1[0:8])
print(str(list1))
print(str(sloice))            # now you have created a new list by slicing and printed it!


#User-defined slice

# User is handed the second of the two most-recently generated lists, and instructed to choose slice points.
def get_list_n_slice(FuncList, prompt1, prompt2):
    print("Length of list is " + str(len(FuncList)))


    # While loop gets broken when invalid answers are given more than once
    while True:
        try:
            slice1 = int(input(prompt1))
            slice2 = int(input(prompt2))
            # Reject invalid inputs
        except ValueError:
            print("Try again, pal. Whole numbers only. \n")
            continue
# So valid answers are under the length of the list
        if  int(slice1) <= len(FuncList) and int(slice2) <= len(FuncList):
            print(str(FuncList[slice1:slice2]))
            break
# Responds differently when different invalid answers are submitted,
# which can depend on how many times that is done.
        elif slice1 >= len(FuncList) or slice2 >= len(FuncList):
            print("Sorry, you've selected a number larger than the list")
            while True:
                try:
                    slice3 = int(input("Please give the first number again: "))
                except ValueError:
                    print("That wasn't a number.")
                    continue
                if slice3 >= len(FuncList):
                    print("I was only patient enough to take overly large numbers one time.")
                    return # return stops my function (def) running when cnd met
                else:
                    print("Thanks!")
                    break
            while True:
                try:
                    slice4 = int(input("Please give the second number again: "))
                except ValueError:
                    print("That wasn't a number.")
                    continue
                if slice4 >= len(FuncList):
                    print("I was only patient enough to take overly large numbers one time.")
                    return
                else:
                    print(FuncList[slice3:slice4])
                    print('Notice how it starts on the entry after where you sliced it')
                    print('with the first number!')
                    break
            break


# Just to be clear, added an else statement
        else:
            break


# Function is introduced to user, then called
print("Ok, let's do a slice of the other extended list we printed.")
print("Please give me two numbers in ascending order. Lowest should be zero or higher.")
get_list_n_slice(list(list2), "1st one? ", "2nd one? ")

'''
# Demonstration of .remove function
print("Cool, let's take one out of the other new list. You choose.")
print("Length of list is " + str(len(list1)))
list1.remove(int(input("Which shall we remove? ")))
print(str(list1))
'''
