'''
Making dictionaries on 16.02.2022 - catching up
'''
'''
At time of publication, this script does not cycle back in order to
modify the dictionary further than one change
'''

# Dictionaries are initiated thus:
databook = {}
# Then a key has its own "dictionary" initiated. Variables added by User
Person = input("Name please?\n")
Place = input("Where are you?\n")
Temp = input("How is the temperature there?\n")
Hat = input("What colour is your hat?\n(Please write "+'none'+" if you do not own one)\n")
Numberr = int(input("Please type in the first number you think of:\n"))

# User inputs added to dictionary
databook[Person] = {}
databook[Person]["Location"] = Place
databook[Person]["Temperature (Qualitative)"] = Temp
databook[Person]["Hat colour"] = Hat
databook[Person]["Number chosen"] = Numberr

# Shows what we've got so far
print(databook)

# Offer chance to modify dictionary
def ask_options(prompt):
    ask_options.Mods = int(input(prompt))
    while True:
        try:
            ask_options.Mods == 1 or ask_options.Mods == 2 or ask_options.Mods == 3 or ask_options.Mods == 4
            break
        except:
            print("Please select one of the options.")
            continue

# Call function
ask_options("Would you like to (1) add or (2) delete entries\n or (3) change any of your entries or (any other number) exit the program?\n")

# Address User choice
# User wanted to add entry =>
if ask_options.Mods == 1:
    Adds = input("Which property would you like to add an entry for?\n")
    databook[Person][Adds] = input("And what would you like the entry to say?\n")
    print("End state of data structure:\n" + str(databook))

# User wanted to delete entry =>
elif ask_options.Mods == 2:
    while True:
        try:
            Deletes = input("Which entry would you like to delete?\n")
            databook[Person].pop(Deletes)
            print("End state of data structure:\n" + str(databook))
            break
        except KeyError:
            print("Please enter something included in the dictionary or\ninterrupt the Program however your system does that.")
            continue

        # User wanted to alter entry =>
elif ask_options.Mods == 3:
    Changes = input("Which entry would you like changed?\n") # Fixed - doesn't accept new entries and loops back if input not accepted
    while True:
        if Changes in databook[Person]:
            databook[Person][Changes] = input("What would you like to change that entry to?\n")
            print("End state of data structure:\n" + str(databook))
            break
        elif Changes not in databook[Person]:
            print("Please enter something included in the dictionary or\ninterrupt the Program however your system does that.\n")
            Changes = input("Which entry would you like changed?\n")
            continue
        else:
            break

        # User wanted to end Program
else:
    print("End state of data:\n" + str(databook))
