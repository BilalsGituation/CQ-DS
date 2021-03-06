'''
Introduction to Tuples:

Done lists and dictionaries so far.

A tuple is:
-ordered (can't change order)
-unchangeable (can't change the entries inside the structure)
-indexed

You can create one with round brackets
'''
'''
myTuple1 = tuple(range(int(input("How long do you want the first tuple to be?\n"))))
print(myTuple1)
myTuple2 = tuple(range(int(input("How long do you want the second tuple to be?\n"))))
print(myTuple2)
myTuple3 = tuple(range(int(input("And the third tuple?\n"))))
print(myTuple3)
myTuple4 = tuple(range(int(input("And the fourth one?\n"))))
print(myTuple4)

entry1 = myTuple1[int(input("Please choose an entry from your first tuple to display: ")) - 1]
print(entry1)
entry2 = myTuple2[int(input("Please choose an entry from your first tuple to display: ")) - 1]
print(entry2)
entry3 = myTuple3[int(input("Please choose an entry from your first tuple to display: ")) - 1]
print(entry3)
entry4 = myTuple4[int(input("Please choose an entry from your first tuple to display: ")) - 1]
print(entry4)
'''

'''
In contrast, sets are unordered, unchangeable (entry can't be switched out)
and sets also can't be indexed.
Like dictionaries, you create them using CURLY brackets although the difference
is that you cannot create an empty set, like you can an empty dictionary.
If you try:
EmptySet = {}
print(type(EmptySet))

you will get "<class 'dict'>"
'''
'''
mySet1 = {1,2,3,3,2,4,4,5}
mySet2 = list(set(mySet1))
print(mySet2) # This demonstrated that set printouts do not contain duplicates
mySet3 = {2, 8, 5392487208423984823, 5392487208423984823, 6, 4, 6, 2}
print(mySet3) # This demonstrated that set of 4 or under (as we discovered in class)
must be converted to list or will be reordered
'''

mySet1 = set(range(int(input("How long do you want the first set to be?\n"))))
print(mySet1)
mySet2 = set(range(int(input("How long do you want the second set to be?\n"))))
print(mySet2)
mySet3 = set(range(int(input("And the third set?\n"))))
print(mySet3)
mySet4 = set(range(int(input("And the fourth one?\n"))))
print(mySet4)

set_entry1 = mySet1.add(int(input("Try adding a duplicate to the first set you produced: ")))
print(mySet1) # Sets do not take duplicates unless they are converted to list
set_entry2 = mySet2.add(int(input("Lool, does't work, does it?\nTry adding one to the second set though: ")))
print(mySet2)
print("Lmaaaooooo, still doesn't work!")

print(mySet1) # original set fed to pop commands
mySet1.pop()
print(mySet1) # Pop removes the first entry in the 0th placeholder
mySet1.add(0)
print(mySet1) # And if you add it again, your set will be converted
              # to a list and your addition appears at the end
