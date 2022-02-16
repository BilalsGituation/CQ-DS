'''
Introduction to Tuples:

Done lists and dictionaries so far.

A tuple is:
-ordered (can't change order)
-unchangeable (can't change the entries inside the structure)
-indexed
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
