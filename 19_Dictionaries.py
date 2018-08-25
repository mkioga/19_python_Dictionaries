
# ======================
# 19_Dictionaries.py
# ======================

# =======================
# dictionaries & sets:
# =======================

# key, keys, description, del, dictionary.clear(), dictionary.get(), hashes, ordering, dict_keys, dict_values, Items & dict_items method,
# dict constructor, string join,

# In previous sections, we have seen how lists are used to store objects
# And then we can retrieve those objects by their index (position in the list)
# Lists are generally used to store similar items, although you can store
# Numbers and strings in the same list if you have a good reason for doing so.
# Lists are also ordered sequences, hence you can iterate all the items in
# a list and process them in order as we have done in previous videos.

# Dictionaries and sets are unordered collections of items
# They both guarantee that there will be no duplicates in that collection.

# Sets are similar to list as they are intended for storing similar items.
# But you cannot actually access individual items in sets using an index.
# A set is unordered, so an index is meaningless in the context of a set

# Dictionaries are unordered and contain key value pairs.
# The values are not accessed by an index but by means of a key.

# While discussing dictionaries, we will learn about two new string methods
# These are: (1) split and (2) join


# Here is an example of a dictionary
# NOTE: keys is separated by a colon (:) from description

fruit = {"Orange": "A Sweet orange citrus fruit",
         "Apple": "A red crunchy fruit",
         "Lemon": "A sour yellow citrus fruit",
         "Grape": "A small purple fruit growing in bunches",
         "Lime": "A sour green citrus fruit"}

print(fruit) # This just prints out what we have typed above
print("="*20)

# We will now use key e.g. Orange to access a particular element.
# We cannot use index to access dictionaries, but we use keys
# The key is "Orange" and the value is "A sweet orange citrus fruit"
# This is why its called a dictionary because you can store a list of words and their definitions

print(fruit["Orange"]) # Using key to access description of a single element (fruit)
print(fruit["Apple"])
print(fruit["Lemon"])
print(fruit["Grape"])
print(fruit["Lime"])
print("="*20)


# You can use Dictionaries to store different types of information.
# In this case we will make a dictionary of a motorBike and store its different info
# Values can be Both strings and numbers
# You can see the output prints all the elements whether strings or numbers.

motorBike = {"make": "Honda", "model": "250 dream", "color": "red", "engine_size": "250"}
print(motorBike["make"])
print(motorBike["model"])
print(motorBike["color"])
print(motorBike["engine_size"])
print("="*20)

# The values in Dictionaries are not restricted to strings and numbers
# They can be any python object, even another dictionary.
# Keys can also be different types of objects.
# The only restriction is that keys must be immutable, so you cannot use a list as a
# dictionary key, but you can use a tuple because they are immutable.



# Adding objects to a dictionary
# You an add an object to a dictionary

fruit = {"Orange": "A Sweet orange citrus fruit",
         "Apple": "A red crunchy fruit",
         "Lemon": "A sour yellow citrus fruit",
         "Grape": "A small purple fruit growing in bunches",
         "Lime": "A sour green citrus fruit"}

print(fruit) # This just prints out what we have typed above
print("="*20)


# Then we add a new object to dictionary fruit
# We will add pear (key) and its description (An odd shaped apple) to fruit dictionary

fruit["pear"] = "An odd shaped apple" # This will add pear to fruit.
print(fruit) # This will print the new fruit. in any order since dictionaries are unordered
print("="*20)

# Keys in a dictionary are unique.
# So if you add an key entry to existing key, it will replace the existing entry
# and not add to the existing entry
# we will add new description to pear and you will see it will replace old description
# old description (An odd shaped apple), New description (good with Tequilla)

fruit["pear"] = "Good with tequilla"
print(fruit) # result for pear is now "Good with tequilla

print("="*20)

# If you reuse a key, the description of last key is the one that will be used.
# For example, we can have two entries for Apple when creating dictionary fruit
# The description of last Apple key is one that is used
# Note that intellij will give you a warning that there is duplicate key. although not an error

fruit = {"Orange": "A Sweet orange citrus fruit",
         "Apple": "A red crunchy fruit", # First entry for apple
         "Lemon": "A sour yellow citrus fruit",
         "Grape": "A small purple fruit growing in bunches",
         "Lime": "A sour green citrus fruit",
         "Pear": "Good with Tequilla",
         "Apple": "Round and Crunchy"} # Second entry for apple

print("Output with two Apple key entries")
print(fruit) # This just prints out what we have typed above
print("="*20)


# Deleting an entry from a Dictionary
# you can delete an entry from a dictionary using "del" key
# Here we want to delete the entry for Pear

del fruit["Pear"]
print("Printing after removing pear")
print(fruit)
print("="*20)

# Note that with "del" command, you need to specify the key to delete
# If you forget and just type "del fruit1" it will delete the entire dictionary
# And then we will get an error when we try to print the dictionary (fruit1)

fruit1 = {"Orange": "A Sweet orange citrus fruit",
         "Apple": "A red crunchy fruit", # First entry for apple
         "Lemon": "A sour yellow citrus fruit",
         "Grape": "A small purple fruit growing in bunches",
         "Lime": "A sour green citrus fruit",}

print("Before del fruit1")
print(fruit1) # This will give you the existing dictionary above
del fruit1     # Then we delete the entire dictionary
print("After del fruit1")
# print(fruit1) # This print will give an error because we are trying to print an dictionary that does not exist
print("="*20)



# If you wanted to delete all the entries in the dictionary but still retain the dictionary
# So you can have an empty dictionary and don't get an error,
# you use "fruit1.clear()
# This will delete contents of fruit1 but fruit1 will still exist.

fruit1 = {"Orange": "A Sweet orange citrus fruit",
          "Apple": "A red crunchy fruit", # First entry for apple
          "Lemon": "A sour yellow citrus fruit",
          "Grape": "A small purple fruit growing in bunches",
          "Lime": "A sour green citrus fruit",}

print("Before fruit1.clear")
print(fruit1)   # This will give you the existing dictionary above
fruit1.clear()  # Deletes contents of dictionary fruit1
print("After fruit1.clear")
print(fruit1)   # This prints empty dictionary. ()
print("="*20)


# Problem accessing items using keys
# If you try to access a key that does not exist, you will get an error
# Here we will try to print tomato (which does not exist)

fruit = {"Orange": "A Sweet orange citrus fruit",
          "Apple": "A red crunchy fruit", # First entry for apple
          "Lemon": "A sour yellow citrus fruit",
          "Grape": "A small purple fruit growing in bunches",
          "Lime": "A sour green citrus fruit",}

# print(fruit["tomato"]) # This will give an error saying KeyError "tomato"

print("="*20)

# ======================
# Method 1 for testing
# ======================

# A good way to avoid such error if you search for a non existent key
# is to use command to test if the key exist.
# we will use the "get" function
# Results here show that it will print the descriptions of the fruit if it exists
# but if it does not exist, it just prints none


fruit = {"Orange": "A Sweet orange citrus fruit",
         "Apple": "A red crunchy fruit", # First entry for apple
         "Lemon": "A sour yellow citrus fruit",
         "Grape": "A small purple fruit growing in bunches",
         "Lime": "A sour green citrus fruit",}

print(fruit)  # Print all the fruits
print(fruit["Apple"]) # Print apple only
while True:  # Code below prints if myKey entered is true (in fruit). Result is none if not true
    myKey = input("Please enter a fruit: ") # you will enter a fruit (key) to search
    if myKey == "quit":
        break # You break from loop if someone types quit
    description = fruit.get(myKey) # get function gets your myKey and searches fruit for it
    print(description)  # This will now print the description of the key you choose

print("="*20)

# ======================
# Method 2 for testing
# ======================

# Here is another way to test the entries to see if they exist in the dictionary


fruit = {"Orange": "A Sweet orange citrus fruit",
         "Apple": "A red crunchy fruit", # First entry for apple
         "Lemon": "A sour yellow citrus fruit",
         "Grape": "A small purple fruit growing in bunches",
         "Lime": "A sour green citrus fruit",}

print(fruit)  # Print all the fruits
print(fruit["Apple"]) # Print apple only

while True:
    myKey = input("Please enter a fruit: ")
    if myKey == "quit":
        break
    if myKey in fruit:  # tests if myKey (key) is in fruit. (fruit.has_key(myKey) command in python 2. deprecated
        description = fruit.get(myKey)
        print(description)
    else:
        print("We don't have a " + myKey) # Here we can append because its is string

print("="*20)

# ======================
# Method 3 for testing
# ======================

# Here is another way you can test for input and print a message if input is not in fruit
# on the line with description, we print if available or print default "we don't have a "
# if input is not in dictionary fruit

print()
fruit = {"Orange": "A Sweet orange citrus fruit",
         "Apple": "A red crunchy fruit", # First entry for apple
         "Lemon": "A sour yellow citrus fruit",
         "Grape": "A small purple fruit growing in bunches",
         "Lime": "A sour green citrus fruit",}

print(fruit)  # Print all the fruits
print(fruit["Apple"]) # Print apple only

while True:
    myKey = input("Please enter a fruit: ")
    if myKey == "quit":
        break
    description = fruit.get(myKey, "we don't have a "+myKey)
    print(description)

print("="*20)

# ==============================================
# Using for loop to iterate through dictionary:
# ==============================================

# The choice of test method to use depends on what you want to do after the test.
# if you want to take some more action after the test, Method 2 would probably be better

# You can iterate or print all the values in the dictionary using for loop
# Note that in dictionary, the list may appear in any order if you run them several times
# And not necessarily the order in which it is typed.
# The dictionary key is hashed, hence you may hear dictionaries referred to as hashes.


fruit = {"Orange": "A Sweet orange citrus fruit",
         "Apple": "A red crunchy fruit", # First entry for apple
         "Lemon": "A sour yellow citrus fruit",
         "Grape": "A small purple fruit growing in bunches",
         "Lime": "A sour green citrus fruit",}

print(fruit)  # Print all the fruits
print("This prints all the items in Dictionary 'fruit'")
print()
for description in fruit:   # Looping through fruit and printing all
    print(fruit[description])

print("="*20)

# we will be looking at hashes later, but they are basically a one way function
# So if you use the same one way function on the key Apple, you will always get the
# same hash, but trying to work out what key was used to create that hash can take a
# powerful computer months to figure out.
# Hash functions are used in cryptography and calculating checksums
# Hash can also be used to store passwords in a database

# It can be helpful to think of a dictionary as being created with a load of free slots.
# And into those slots, data is actually stored.
# The key is hashed, and the hash value is used to determine which slot is used.
# Because we are creating the dictionary every time we run the program, the slots are
# allocated differently so that the items are in different orders.

# Python does not randomly move things around though as we will see in the following example
# If you run this first time, the 10 iterations give same result
# However if you run the 10 iterations again, its supposed to result in a different order.
# However in my program. its all same order.
# Teacher explanation for changes is that at the time the results are created that the
# slots are arbitrarilly created.


fruit = {"Orange": "A Sweet orange citrus fruit",
         "Apple": "A red crunchy fruit", # First entry for apple
         "Lemon": "A sour yellow citrus fruit",
         "Grape": "A small purple fruit growing in bunches",
         "Lime": "A sour green citrus fruit",}

print(fruit)  # Print all the fruits

for i in range(10):
    for description in fruit:  # description iterates through the key
        print(description + " is " + fruit[description])  # fruit[description]) is the description of the key
    print('-' * 40) # This is a separator after each iteration

print("="*20)


# ===========================
# Ordering dictionary keys:
# ===========================

# One reason ordering may be important is for humans to read
# In this case, we are going to order the output when we want to print it.
# So we are going to create the list from the dictionary keys using .keys function
# Then sort the list
# Then print the results

fruit = {"Orange": "A Sweet orange citrus fruit",
         "Apple": "A red crunchy fruit", # First entry for apple
         "Lemon": "A sour yellow citrus fruit",
         "Grape": "A small purple fruit growing in bunches",
         "Lime": "A sour green citrus fruit",}

print(fruit)  # Print all the fruits
print()
ordered_keys = list(fruit.keys()) # Gets the list of keys from the dictionary with .keys
ordered_keys.sort()  # Then we are going to sort them.
for f in ordered_keys:
    print(f + " - " + fruit[f]) # f is keys, fruit[f] is content of keys

print("="*20)



# you can do same program as above but with one less line as shown


fruit = {"Orange": "A Sweet orange citrus fruit",
         "Apple": "A red crunchy fruit", # First entry for apple
         "Lemon": "A sour yellow citrus fruit",
         "Grape": "A small purple fruit growing in bunches",
         "Lime": "A sour green citrus fruit",}

print(fruit)  # Print all the fruits
print()
ordered_keys = sorted(list(fruit.keys())) # Gets the list of keys and sort them

for f in ordered_keys:
    print(f + " - " + fruit[f]) # f is keys, fruit[f] is content of keys

print("="*20)

# Here is an even shorter way of doing it.
# Note that fruit.keys does not create a regular sorted list.
# But when we add sorted in front of it, it sorts the list.


fruit = {"Orange": "A Sweet orange citrus fruit",
         "Apple": "A red crunchy fruit", # First entry for apple
         "Lemon": "A sour yellow citrus fruit",
         "Grape": "A small purple fruit growing in bunches",
         "Lime": "A sour green citrus fruit",}

print(fruit)  # Print all the fruits
print()

for f in sorted(fruit.keys()): # We use for, in and sorted functions in one line
    print(f + " - " + fruit[f]) # f is keys, fruit[f] is content of keys

print("="*20)


# if you are not planning to sort the keys, you can use this simple code


fruit = {"Orange": "A Sweet orange citrus fruit",
         "Apple": "A red crunchy fruit", # First entry for apple
         "Lemon": "A sour yellow citrus fruit",
         "Grape": "A small purple fruit growing in bunches",
         "Lime": "A sour green citrus fruit",}

print(fruit)  # Print all the fruits
print()

for f in fruit:
    print(f + " - " + fruit[f]) # f is keys, fruit[f] is content of keys

print("="*20)


# Using "Values"
# If you are only planning to display the values of the keys i.e. the descriptions of the keys
# you can use this command


fruit = {"Orange": "A Sweet orange citrus fruit",
         "Apple": "A red crunchy fruit", # First entry for apple
         "Lemon": "A sour yellow citrus fruit",
         "Grape": "A small purple fruit growing in bunches",
         "Lime": "A sour green citrus fruit",}

print(fruit)  # Print all the fruits
print()

for value in fruit.values():  # fruit.values() pulls the descriptions of the keys
    print(value) # f is keys, fruit[f] is content of the description or values

print("="*20)


# It is however better to use keys (above) and get the values (fruit[f]) because
# this method is more optimized and efficient
# This method below is more efficient


fruit = {"Orange": "A Sweet orange citrus fruit",
         "Apple": "A red crunchy fruit", # First entry for apple
         "Lemon": "A sour yellow citrus fruit",
         "Grape": "A small purple fruit growing in bunches",
         "Lime": "A sour green citrus fruit",}

print(fruit)  # Print all the fruits
print()

for key in fruit:
    print(fruit[key]) # f is keys, fruit[f] is content of keys

print("="*20)



# Note that both "keys" and "values" return list like objects
# keys return dict_key object and values return dict_values object.
# both of these are what is called a view object.
# And if the underlying dictionary changes, then they will change as well.

fruit = {"Orange": "A Sweet orange citrus fruit",
         "Apple": "A red crunchy fruit", # First entry for apple
         "Lemon": "A sour yellow citrus fruit",
         "Grape": "A small purple fruit growing in bunches",
         "Lime": "A sour green citrus fruit",}

print(fruit)  # Print all the fruits
print()

print(fruit.keys())      # returns a dict_keys object
print(fruit.values())    # returns a dict_values object

print("="*20)


# And if the underlying dictionary changes, then they will change as well.
# We are going to show some example code of how this works
# We are going to assign the dictionary keys to a variable named "fruit_keys"
# then add key named "Tomato" to the dictionary and then see what happens to
# our variable "fruit_keys"
# We see that the variable "fruit_keys" is then updated after we add a new key to fruits
# This is the only way that view objects can be updated indirectly with dictionaries behind
# the scenes


fruit = {"Orange": "A Sweet orange citrus fruit",
         "Apple": "A red crunchy fruit", # First entry for apple
         "Lemon": "A sour yellow citrus fruit",
         "Grape": "A small purple fruit growing in bunches",
         "Lime": "A sour green citrus fruit",}

print(fruit)  # Print all the fruits
print()

fruit_keys = fruit.keys()  # we create variable named fruit_keys and assign int fruit.keys
print("Initial fruit_keys variable. before changes")
print(fruit_keys)          # then we print that variable fruit_keys
print()
fruit["Tomato"] = "Tomato is a red fruit"  # We add key Tomato to dictionary fruit.
print("fruit_keys after tomato is added to fruit")
print(fruit_keys)  # We see that the variable fruit_keys is now updated with key tomato

print("="*20)



# We can't add items using delete. it will get error.
# but what we can do is convert them into lists using list method and then sort.

# ========================================
# "Items" method & "dict_items" method:
# ========================================

# Items method is one more view method we should look at.
# "items" method returns a "dict_items" method, another dynamic view object that consist
# of "key" and "value" tuples as well.

fruit = {"Orange": "A Sweet orange citrus fruit",
         "Apple": "A red crunchy fruit", # First entry for apple
         "Lemon": "A sour yellow citrus fruit",
         "Grape": "A small purple fruit growing in bunches",
         "Lime": "A sour green citrus fruit",}

print(fruit)  # Print all the fruits
print()
print("printing fruit.items method")
print(fruit.items()) # result looks similar to a tuple.

fruit_tuple = tuple(fruit.items()) # we will make tuple with tuple build in function
print()
print("this print resuls or fruit_tuple")
print(fruit_tuple)  # This prints a regular tuple

# This is the result from "print(fruit_tuple) above
# (('Orange', 'A Sweet orange citrus fruit'), ('Apple', 'A red crunchy fruit'), ('Lemon', 'A sour yellow citrus fruit'), ('Grape', 'A small purple fruit growing in bunches'), ('Lime', 'A sour green citrus fruit'))

# Then with this regular tuple, we can use it like we did with other regular tuples

print()
print("now we print results from tuple above:")
print()
for snack in fruit_tuple:
    item, description = snack
    print("key: "+ item + " Description: " + description)

print("="*20)

# ====================
# "dict" constructor:
# ====================

# It is also possible to go the other way around
# to produce a dictionary from tuples of "key: value" pairs.
# The "dict" constuctor is used to do that

# We are going to pass results from tuple to "dict" function to create dictionary

fruit = {"Orange": "A Sweet orange citrus fruit",
         "Apple": "A red crunchy fruit", # First entry for apple
         "Lemon": "A sour yellow citrus fruit",
         "Grape": "A small purple fruit growing in bunches",
         "Lime": "A sour green citrus fruit",}

print(fruit)  # Print all the fruits
print()
print("printing fruit.items method")
print(fruit.items()) # result looks similar to a tuple.

fruit_tuple = tuple(fruit.items()) # we will make tuple with tuple build in function
print()
print("This print results of fruit_tuple")
print(fruit_tuple)  # This prints a regular tuple that we created
print()

print("For loop prints key & description of each element in tuple")
for snack in fruit_tuple:
    item, description = snack  # unpack the inside tuple
    print("key: "+ item + " Description: " + description)

print()
print("Print the dictionary from tuple above")
print(dict(fruit_tuple)) # we use the "duct" built in function to get dictionary from tuple

print("="*20)


# ========================
# String method "join":
# ========================

# Remember that strings are immutable (cannot be changed)
# Hence its not very efficient to concatenate strings in a loop
# Every time you concatenate a string to a new string, the new string has to be created
# and if that is done in a loop, it becomes expensive and slow

# String join method is there to help us
# it takes a sequence and produces a string from it.
# The items in the new string are separated by the the string that join was called upon

# This example is not a good way of making code.
# Because every time through the loop, it is creating a new copy of newString.
# because strings are immutable.
# Augmented assignment (+=) will help because it tries to update the variable in place
# but in this case, that is not possible because strings are immitable


myList = ["a", "b", "c", "d"] # This is a list.

newString = '' # newString is empty for now

for c in myList:
    newString += c +", "
print(newString) # we print the contents of myList

print("="*20)

# In this case, we want to use join
# Note that we don't use for loop because join does not require a for loop
# Note that join takes the list and separates one by one
# Then displays the result separated by whatever you give it in the " "


myList = ["a", "b", "c", "d"] # This is a list.
print(myList)
print("Output using join")
newString = ".".join(myList) # Separates by "."
print(newString)
newString = ", ".join(myList) # Separates by ","
print(newString)
newString = "|".join(myList) # Separates by "|"
print(newString)
newString = "".join(myList) # Separates by nothing
print(newString)

print("="*20)

# # Here is another example using a string separated by commas


letters = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z" # string
print(letters)
print("Output using join")
newString = ".".join(letters) # Separates by "."
print(newString)
newString = ",".join(letters) # Separates by ","
print(newString)
newString = "|".join(letters) # Separates by "|"
print(newString)
newString = "".join(letters) # Separates by nothing
print(newString)

print("="*20)



# # Here is another example using a continuous string

letters = "abcdefghijklmnopqrstuvwxyz" # string
print(letters)
print("Output using join")
newString = ".".join(letters) # Separates by "."
print(newString)
newString = ",".join(letters) # Separates by ","
print(newString)
newString = "|".join(letters) # Separates by "|"
print(newString)
newString = "".join(letters) # Separates by nothing
print(newString)

print("="*20)


# # Here is another example using a numbers and separating it with text "number"

numbers = "123456789" # This is a string too. If you use numbers (no " ") it gives error

print(numbers)
print("Output using join")
newString = " Number ".join(numbers) # Separates by "."
print(newString)
newString = ",".join(numbers) # Separates by ","
print(newString)
newString = "|".join(numbers) # Separates by "|"
print(newString)
newString = "".join(numbers) # Separates by nothing
print(newString)

print("="*20)

# =========================
# Game using dictionaries:
# =========================

# Here we have "Locations" in a dictionary

locations = {0: "Exit",
             1: "Road",
             2: "Hill",
             3: "Building",
             4: "Valley",
             5: "Forest"}

# Then we have exits in a list comprised of dictionaries.

exits = [{"Q": 0},
         {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         {"N": 5, "Q": 0},
         {"W": 1, "Q": 0},
         {"N": 1, "W": 2, "Q": 0},
         {"W": 2, "S": 1, "Q": 0}]

loc = 1 # We are starting at position 1
print("First position(loc) = {}".format(loc))
while True:
    availableExits = ""     # We initialize availableExits to null
    for direction in exits[loc].keys(): # iterate thru exits, and get the keys of each position in exits
        print("exits keys in loc {} are {}".format(loc, exits[loc].keys()))  # we print this to show you the keys
        availableExits += direction + ", " # Adds all the keys to availableExits
        print("availableExits = {}".format(availableExits))

    print("You are here: " + locations[loc])    # print current locatioon

    if loc == 0:    # if location is 0, break (because you want to quit)
        break

    # we choose a direction and assign it to variable named "direction"
    direction = input("Enter Direction: "+ availableExits ).upper() # Enter exit. it converts to uppercase to match keys
    print()
    print("exits[loc] = {}".format(exits[loc]))  # NOTE that loc here is the one above, which initially is 1
    print()
    if direction in exits[loc]: # If value we chose is in exits[loc], where loc is the preceeding loc number. initial was 1
        loc = exits[loc][direction]  # Gives loc value corresponding to chosen key in exits. W is 2, E is 3 etc
        print("New position(loc) = {}".format(loc))
    else:
        print("You cannot go in that direction")

print("="*20)


# Above program works, but we know that concatenating a string inside a loop is not a good idea
# This command here: availableExits += direction + ", "
# if a lot of people are playing this game, there will be slow performance
# you can replace that for loop with a join



locations = {0: "Exit",
             1: "Road",
             2: "Hill",
             3: "Building",
             4: "Valley",
             5: "Forest"}

# Then we have exits in a list comprised of dictionaries.

exits = [{"Q": 0},
         {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         {"N": 5, "Q": 0},
         {"W": 1, "Q": 0},
         {"N": 1, "W": 2, "Q": 0},
         {"W": 2, "S": 1, "Q": 0}]

loc = 1 # We are starting at position 1
print("First position(loc) = {}".format(loc))
while True:
    availableExits = ", ".join(exits[loc].keys()) # replace for loop with join to shorten code
    print("availableExits = {}".format(availableExits))

    print("You are here: " + locations[loc])    # print current locatioon

    if loc == 0:    # if location is 0, break (because you want to quit)
        break

    # we choose a direction and assign it to variable named "direction"
    direction = input("Enter Direction: "+ availableExits +" : ").upper() # Enter exit. it converts to uppercase to match keys
    print()
    if direction in exits[loc]: # If value we chose in direction exits[loc] i.e. if its a valid location in exits
        loc = exits[loc][direction]  # Gives loc value corresponding to chosen key in exits. W is 2, E is 3 etc
        print("New position(loc) = {}".format(loc))
    else:
        print("You cannot go in that direction")

print("="*20)

# ===========
# Challenge:
# ===========
# Part 1:

# Modify the program so that "exits" is a "dictionary" and not a "list".
# with the keys being the numbers of the location and the values being dictionaries
# holding the exits (as they do at present). No change will be needed in the actual code


locations = {0: "Exit",
             1: "Road",
             2: "Hill",
             3: "Building",
             4: "Valley",
             5: "Forest"}

# We have turned "exits" from a list [] into a dictionary {}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}


# Note that we did not have to change any of the code below after we changed
# "exits" from a list to a dictionary.
# This is because if we are using a numerical "key" in a "dictionary", the sytax
# for retrieving the dictionary value by key is the same as retrieving a list by index


loc = 1 # We are starting at position 1
print("First position(loc) = {}".format(loc))
while True:
    availableExits = ", ".join(exits[loc].keys()) # replace for loop with join to shorten code
    print("availableExits = {}".format(availableExits))

    print("You are here: " + locations[loc])    # print current locatioon

    if loc == 0:    # if location is 0, break (because you want to quit)
        break

    # we choose a direction and assign it to variable named "direction"
    direction = input("Enter Direction: "+ availableExits +" : ").upper() # Enter exit. it converts to uppercase to match keys
    print()
    if direction in exits[loc]: # If value we chose in direction exits[loc] i.e. if its a valid location in exits
        loc = exits[loc][direction]  # Gives loc value corresponding to chosen key in exits. W is 2, E is 3 etc
        print("New position(loc) = {}".format(loc))
    else:
        print("You cannot go in that direction")

print("="*20)

# ==================
# Challenge Part 2:
# ==================

# Once that is working, create another dictionary that contains words that players may use
# These words will be the keys, and their values will be a single letter that the program
# can use to determine which way to go.


locations = {0: "Exit",
             1: "Road",
             2: "Hill",
             3: "Building",
             4: "Valley",
             5: "Forest"}

# We have turned "exits" from a list [] into a dictionary {}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}


# Now we create the second "dictionary" and name it "vocabulary"
# Note for example that "QUIT" is the "key" and "Q" is the "value" for this dictionary

vocabulary = {"QUIT": "Q",
              "NORTH": "N",
              "SOUTH": "S",
              "EAST": "E",
              "WEST": "W"}


loc = 1 # We are starting at position 1
print("First position(loc) = {}".format(loc))
while True:
    availableExits = ", ".join(exits[loc].keys()) # replace for loop with join to shorten code
    print("availableExits = {}".format(availableExits))

    print("You are here: " + locations[loc])    # print current locatioon

    if loc == 0:    # if location is 0, break (because you want to quit)
        break

    # we choose a direction and assign it to variable named "direction"
    direction = input("Enter Direction: "+ availableExits +" : ").upper() # Enter exit. it converts to uppercase to match keys
    print()

    # This is the code we will add for this step
    # We parse the user input (stored in "direction", and check if it exists in "vocabulary"

    if len(direction) > 1: # if user entered more than one letter, check vocabulary dictionary
        for word in vocabulary: # retrieve through all the keys in "vocabulary" e.g. "QUIT", "NORTH" etc
            if word in direction: # if any of the vocabulary keys match what user entered (in direction)
                direction = vocabulary[word] # retrieve the "value" corresponding to "key" in vocabulary and assign it to direction

    # Note that when you run above command, you can type "go north" and it will work fine
    # This is because we are going through our "vocabulary" dictionary first and comparing each
    # key in it to see if it matches what is being typed

    # Then we use the new "direction" here as normal. so if user typed "QUIT", above code assigns "Q" to direction
    # Then in below code, direction will be "Q" and it will run as normal

    if direction in exits[loc]: # If value we chose in direction exits[loc] i.e. if its a valid location in exits
        loc = exits[loc][direction]  # Gives loc value corresponding to chosen key in exits. W is 2, E is 3 etc
        print("New position(loc) = {}".format(loc))
    else:
        print("You cannot go in that direction")

print("="*20)





# ======================
# Using "split" method:
# ======================

# In the above code, we saw that you can type "go north" and it will work fine
# because we are going through our "vocabulary" dictionary first and comparing
# each key in it to see if it matches what is being typed

# This can be inefficient if the "vocabulary" dictionary is large.
# A better way would be first check each word that the player has typed,
# and then compare it to keys in "vocabulary" dictionary to see if it is there.

# To do this, we need to break up the input that the player typed into its individual words
# or individual sequences of characters separated by spaces.
# So we will do the opposite of "join" using a method called "split"

# Given a string, the "split" method will split the string into a list
# containing all the parts of the string that are separated by our chosen method
# here we will say separated by default i.e "space"
# But we could use commas, periods etc


# Lets try the "split" function and see its output

locations = {0: "Exit this is the exit",
             1: "Road",
             2: "Hill",
             3: "Building, This is the building",
             4: "Valley",
             5: "Forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

vocabulary = {"QUIT": "Q",
              "NORTH": "N",
              "SOUTH": "S",
              "EAST": "E",
              "WEST": "W"}

# splits sentence [0] into a list containing the 5 words (default separation is space)
print("==== Using split example 1 =======")

print(locations[0].split())

# We specified comma as separator, hence we get a list with only two words because sentence [3] has only one comma
print("==== Using split example 2 =======")
print(locations[3].split(","))

# "split" is the opposite of "join"
# So "join" will join words based on the separator, default is space
# "locations[0].split())" returns "['Exit', 'this', 'is', 'the', 'exit']" which is separated.
# Then we use "join" which takes the separate words and joins them again.
# This will print the original words in sentence [0]

print("== using join example 1 =====:")
print(' '.join(locations[0].split()))

# Note that the ' ' in front of the join method is to put a space between the words being joined
# Here are some example outputs
print("== using join example 2 =====:")
print(''.join(locations[0].split()))  # No space between the joined words
print('='.join(locations[0].split())) # Equal sign between the joined words
print('= '.join(locations[0].split())) # Equal sign and space


print("==== Using split in program =======")
loc = 1 # We are starting at position 1
print("First position(loc) = {}".format(loc))
while True:
    availableExits = ", ".join(exits[loc].keys()) # replace for loop with join to shorten code
    print("availableExits = {}".format(availableExits))

    print("You are here: " + locations[loc])    # print current locatioon

    if loc == 0:    # if location is 0, break (because you want to quit)
        break

    # we choose a direction and assign it to variable named "direction"
    direction = input("Enter Direction: "+ availableExits +" : ").upper() # Enter exit. it converts to uppercase to match keys
    print()

    # This is the code we will add for this step
    # We parse the user input (stored in "direction", and check if it exists in "vocabulary"

    if len(direction) > 1: # if user entered more than one letter, check vocabulary dictionary
        for word in vocabulary: # retrieve through all the keys in "vocabulary" e.g. "QUIT", "NORTH" etc
            if word in direction: # if any of the vocabulary keys match what user entered (in direction)
                direction = vocabulary[word] # retrieve the "value" corresponding to "key" in vocabulary and assign it to direction

    # Note that when you run above command, you can type "go north" and it will work fine
    # This is because we are going through our "vocabulary" dictionary first and comparing each
    # key in it to see if it matches what is being typed

    # Then we use the new "direction" here as normal. so if user typed "QUIT", above code assigns "Q" to direction
    # Then in below code, direction will be "Q" and it will run as normal

    if direction in exits[loc]: # If value we chose in direction exits[loc] i.e. if its a valid location in exits
        loc = exits[loc][direction]  # Gives loc value corresponding to chosen key in exits. W is 2, E is 3 etc
        print("New position(loc) = {}".format(loc))
    else:
        print("You cannot go in that direction")







# Now that we have seen how "split" and "join" methods works, we will modify the code
# to work the correct way around i.e. check the players input against the vocabulary
# instead of the vocabulary against the players input


# Lets try the "split" function and see its output

locations = {0: "Exit this is the exit",
             1: "Road",
             2: "Hill",
             3: "Building, This is the building",
             4: "Valley",
             5: "Forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

vocabulary = {"QUIT": "Q",
              "NORTH": "N",
              "SOUTH": "S",
              "EAST": "E",
              "WEST": "W"}



loc = 1 # We are starting at position 1
print("First position(loc) = {}".format(loc))
while True:
    availableExits = ", ".join(exits[loc].keys()) # replace for loop with join to shorten code
    print("availableExits = {}".format(availableExits))

    print("You are here: " + locations[loc])    # print current locatioon

    if loc == 0:    # if location is 0, break (because you want to quit)
        break

    # we choose a direction and assign it to variable named "direction"
    direction = input("Enter Direction: "+ availableExits +" : ").upper() # Enter exit. it converts to uppercase to match keys
    print()

    # This is the code we will add for this step
    # We parse the user input (stored in "direction", and check if it exists in "vocabulary"

    if len(direction) > 1: # if user entered more than one letter, check vocabulary dictionary
        words = direction.split()  # We take input in "direction", split it by space, then assign it to variable "words"
        print(words) # We print words here just to see what it has. Not necessary for the code
        for word in words: # loop through all the entries in "words"
            if word in vocabulary: # if any of entries in "words" match key in vocabulary
                direction = vocabulary[word] # retrieve the "value" corresponding to "key" in vocabulary and assign it to direction
                break # Then we break from the "if word in words"

    # Then we use the new "direction" here as normal. so if user typed "QUIT", above code assigns "Q" to direction
    # Then in below code, direction will be "Q" and it will run as normal

    if direction in exits[loc]: # If value we chose in direction exits[loc] i.e. if its a valid location in exits
        loc = exits[loc][direction]  # Gives loc value corresponding to chosen key in exits. W is 2, E is 3 etc
        print("New position(loc) = {}".format(loc))
    else:
        print("You cannot go in that direction")





