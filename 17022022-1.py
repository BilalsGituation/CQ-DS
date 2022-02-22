"""
This is the 6th day of learning Python with the class

Today is our Introduction to loops.
This script will address "for" loops
"""

# Faculty = 1
# for i in range(1,11):
#     print(i)
#     Faculty = Faculty * i
#     print(Faculty)

"""
i (the running index) increases from 1-11, and the Faculty keeps getting iterated
for every "i" in the range (range inherently goes up 1->2->3->...).
"""

# First loop generates all numbers between 0 and 22
print("\nFirst loop: Numbers 0-21:\n")
loopI1 = -1
for i in range(0, 22):
    loopI1 = loopI1 + 1
    print(loopI1)

# Second loop: summarises only even numbers in first range
print("\nSecond loop: Numbers 0-21 (even):\n")
loopI2 = -2
for i in range(0, 21, 2):
    loopI2 = loopI2 + 2
    print(loopI2)


# Third loop: summarises first range in reverse order
print("\nThird loop: Numbers 0-21 (reversed):\n")
loopI3 = 22
for i in reversed(range(0, 22)):
    loopI3 = loopI3 - 1
    print(loopI3)
