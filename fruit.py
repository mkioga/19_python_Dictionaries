
# "update" method
# "update" method is used to combine dictionaries


# dictionaries holding fruit and vegetables
#
# fruit = {"orange": "It is yellow in color",
#          "apple": "it is red in color",
#          "lemon": "it is green in color"}
#
# vegetable = {"cabbage": "it has big leaves",
#              "spinach": "it is kind of long"}
#
# # Here we print out fruit and vegetable to show you what output looks like
#
# print()
# print(fruit)
# print()
# print(vegetable)
# print()
#
# # now we combine the two dictionaries using "update" method
# # here we add fruit to vegetable.
# # new vegetable now gives the combined output
# # You can also do the reverse i.e. add vegetable to fruit.
#
# vegetable.update(fruit)
# print(vegetable)



# Note that the "update" method returns "None"
# Remember from earlier discussion on "sort" method in "list"
# A new list is not returned when you call "sort"

# Same thing with "update" method in "dictionaries"
# A new dictionary is not return when you call "update" method either
#
# fruit = {"orange": "It is yellow in color",
#          "apple": "it is red in color",
#          "lemon": "it is green in color"}
#
# vegetable = {"cabbage": "it has big leaves",
#              "spinach": "it is kind of long"}
#
# print()
# print(vegetable)  # prints initial vegetable
# print()
#
# vegetable.update(fruit) # we add fruit to vegetable
# print(vegetable)   # prints new vegetable (which includes fruit)
# print()
#
# # update method will update the dictionaries, but if you call it or print it, it returns None
#
# print(fruit.update(vegetable)) # if you try to print the update method, it returns none
# print(fruit) # Note that new fruit includes vegetable
#




# "copy" method
# If you don't want to modify existing dictionaries, you can create new ones
# and copy the content of old ones in the new, then modify the new as you like
# you copy content of a dictionary to another using "copy" method

# Original dictionaries are "fruit" and "vegetable
#
# fruit = {"orange": "It is yellow in color",
#          "apple": "it is red in color",
#          "lemon": "it is green in color"}
#
# vegetable = {"cabbage": "it has big leaves",
#              "spinach": "it is kind of long"}
#
#
# print("Original dictionaries")
# print(fruit)
# print()
# print(vegetable)
# print()
#
# # We create new dictionary "fruit_and_veg" and copy contents of "fruit" to it.
#
# fruit_and_veg = fruit.copy()
# print(fruit_and_veg) # only has fruits in it.
# print()
#
# # Now we can update "fruit_and_veg" and add "vegetable" to it.
#
# fruit_and_veg.update(vegetable)
# print(fruit_and_veg)  # New "fruit_and_veg" has both fruits and vegetables
#
# # We can check to verify that the original fruit and vegetable has not been updated
#
# print()
# print("original fruit and vegetable not modified")
# print(fruit)
# print(vegetable)




# One way "copy" method can be useful is in updating user interface of our game
# we can make players to enter the name of a location rather than direction
# In this case, we will extend the "vocabulary" dictionary to include the location names.
#
#
# locations = {0: "Exit this is the exit",
#              1: "Road",
#              2: "Hill",
#              3: "Building, This is the building",
#              4: "Valley",
#              5: "Forest"}
#
# # We will also update all these entries in exits
# # so that if someone say types hill, it pulls 2 from vocabulary
# # and uses that 2 to pull 2 in exits hence go north to hill
#
# exits = {0: {"Q": 0},
#          1: {"W": 2, "2": 2, "E": 3, "3": 3, "N": 5, "5": 5, "S": 4, "4": 4, "Q": 0},
#          2: {"N": 5, "5": 5, "Q": 0},
#          3: {"W": 1, "1": 1, "Q": 0},
#          4: {"N": 1, "1": 1, "W": 2, "2": 2, "Q": 0},
#          5: {"W": 2, "2": 2, "S": 1, "1": 1, "Q": 0}}
#
# vocabulary = {"QUIT": "Q",
#               "NORTH": "N",
#               "SOUTH": "S",
#               "EAST": "E",
#               "WEST": "W",
#               "ROAD": "1", # We update this dictionary with this
#               "HILL": "2",
#               "BUILDING": "3",
#               "VALLEY": "4",
#               "FOREST": "5"}
#
# loc = 1 # We are starting at position 1
# print("First position(loc) = {}".format(loc))
# while True:
#     availableExits = ", ".join(exits[loc].keys()) # replace for loop with join to shorten code
#     print("availableExits = {}".format(availableExits))
#     print()
#     print("You are here: " + locations[loc])    # print current locatioon
#
#     if loc == 0:    # if location is 0, break (because you want to quit)
#         break
#
#     # we choose a direction and assign it to variable named "direction"
#     direction = input("Enter Direction: "+ availableExits +" : ").upper() # Enter exit. it converts to uppercase to match keys
#     print()
#
#     # This is the code we will add for this step
#     # We parse the user input (stored in "direction", and check if it exists in "vocabulary"
#
#     if len(direction) > 1: # if user entered more than one letter, check vocabulary dictionary
#         words = direction.split()  # We take input in "direction", split it by space, then assign it to variable "words"
#         print("split words are: {}".format(words)) # We print words here just to see what it has. Not necessary for the code
#         for word in words: # loop through all the entries in "words"
#             if word in vocabulary: # if any of entries in "words" match key in vocabulary
#                 direction = vocabulary[word] # retrieve the "value" corresponding to "key" in vocabulary and assign it to direction
#                 break # Then we break from the "if word in words"
#
#     # Then we use the new "direction" here as normal. so if user typed "QUIT", above code assigns "Q" to direction
#     # Then in below code, direction will be "Q" and it will run as normal
#
#     if direction in exits[loc]: # If value we chose in direction exits[loc] i.e. if its a valid location in exits
#         loc = exits[loc][direction]  # Gives loc value corresponding to chosen key in exits. W is 2, E is 3 etc
#         print("New position(loc) is: {} which is '{}''".format(loc, locations[loc]))
#     else:
#         print("You cannot go in that direction")




# In above code, when you run it, it gives you this line:
# Enter Direction: W, 2, E, 3, N, 5, S, 4, Q :
# you can see apart from directions, W,E,N,S, it also gives us numbers 2, 3, 5, 4 etc

# A solution to this is to store the named destinations (HILL, BUILDING, VALLEY etc) in
# a new dictionary and then combine them at the point when we check the players input

#
# locations = {0: "Exit this is the exit",
#              1: "Road",
#              2: "Hill",
#              3: "Building, This is the building",
#              4: "Valley",
#              5: "Forest"}
#
# # We are going to use the original exits with only directions
#
# exits = {0: {"Q": 0},
#          1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
#          2: {"N": 5, "Q": 0},
#          3: {"W": 1, "Q": 0},
#          4: {"N": 1, "W": 2, "Q": 0},
#          5: {"W": 2, "S": 1, "Q": 0}}
#
# # Then create a namedExits dictionary with the numbered exits
#
# namedExits = {1: {"2": 2, "3": 3, "5": 5, "4": 4},
#               2: {"5": 5},
#               3: {"1": 1},
#               4: {"1": 1, "2": 2},
#               5: {"2": 2, "1": 1}}
#
# vocabulary = {"QUIT": "Q",
#               "NORTH": "N",
#               "SOUTH": "S",
#               "EAST": "E",
#               "WEST": "W",
#               "ROAD": "1", # We update this dictionary with this
#               "HILL": "2",
#               "BUILDING": "3",
#               "VALLEY": "4",
#               "FOREST": "5"}
#
#
# # in below code under line with break
# # We will test if the user is not quiting (loc is not equal to 0)
# # Then create a combined directory by taking a copy of an instance of the
# # "exits" dictionary and updating it to include the appropriate "namedExits"
#
#
# loc = 1 # We are starting at position 1
# print("First position(loc) = {}".format(loc))
# while True:
#     availableExits = ", ".join(exits[loc].keys()) # replace for loop with join to shorten code
#     print("availableExits = {}".format(availableExits))
#     print()
#     print("You are here: " + locations[loc])    # print current locatioon
#
#     if loc == 0:    # if location is 0, break (because you want to quit)
#         break
#     else:
#         allExits = exits[loc].copy() # Take a copy of exits for say position 1 and copy them to new dictionary "allExits"
#         allExits.update(namedExits[loc]) # then we combine new "allExits" directory with "namedExits" dictionary for that instance
#
#     # we choose a direction and assign it to variable named "direction"
#     direction = input("Enter Direction: "+ availableExits +" : ").upper() # Enter exit. it converts to uppercase to match keys
#     print()
#
#     # This is the code we will add for this step
#     # We parse the user input (stored in "direction", and check if it exists in "vocabulary"
#
#     if len(direction) > 1: # if user entered more than one letter, check vocabulary dictionary
#         words = direction.split()  # We take input in "direction", split it by space, then assign it to variable "words"
#         print("split words are: {}".format(words)) # We print words here just to see what it has. Not necessary for the code
#         for word in words: # loop through all the entries in "words"
#             if word in vocabulary: # if any of entries in "words" match key in vocabulary
#                 direction = vocabulary[word] # retrieve the "value" corresponding to "key" in vocabulary and assign it to direction
#                 break # Then we break from the "if word in words"
#
#     # Then we use the new "direction" here as normal. so if user typed "QUIT", above code assigns "Q" to direction
#     # Then in below code, direction will be "Q" and it will run as normal
#
#     if direction in allExits: # here we test for "allExits"
#         loc = allExits[direction]  # new loc is given value in combined dictionary "allExits"
#         print("New position(loc) is: {} which is '{}''".format(loc, locations[loc]))
#     else:
#         print("You cannot go in that direction")





# Challenge
# We have mentioned that the data for the adventure game could be organized in many
# different ways. We've created another way for you.
# Your challenge is to change the code to make it work
# The "locations" dictionary is modified so that everything is in a single dictionary

# Note that dictionaries "exits" and "namedExits" are combined in "locations"


locations = {0: {"desc": "This is the exit",
                 "exits": {},
                 "namedExits": {}},
             1: {"desc": "This is the Road",
                 "exits": {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
                 "namedExits": {"2": 2, "3": 3, "5": 5, "4": 4}},
             2: {"desc": "This is the Hill",
                 "exits": {"N": 5, "Q": 0},
                 "namedExits": {"5": 5}},
             3: {"desc": "This is the building",
                 "exits": {"W": 1, "Q": 0},
                 "namedExits": {"1": 1}},
             4: {"desc": "This is the Valley",
                 "exits": {"N": 1, "W": 2, "Q": 0},
                 "namedExits": {"1": 1, "2": 2}},
             5: {"desc": "This is the Forest",
                 "exits": {"W": 2, "S": 1, "Q": 0},
                 "namedExits": {"2": 2, "1": 1}}
             }

# We are going to use the original exits with only directions

# exits = {0: {"Q": 0},
#          1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
#          2: {"N": 5, "Q": 0},
#          3: {"W": 1, "Q": 0},
#          4: {"N": 1, "W": 2, "Q": 0},
#          5: {"W": 2, "S": 1, "Q": 0}}
#
# # Then create a namedExits dictionary with the numbered exits
#
# namedExits = {1: {"2": 2, "3": 3, "5": 5, "4": 4},
#               2: {"5": 5},
#               3: {"1": 1},
#               4: {"1": 1, "2": 2},
#               5: {"2": 2, "1": 1}}

vocabulary = {"QUIT": "Q",
              "NORTH": "N",
              "SOUTH": "S",
              "EAST": "E",
              "WEST": "W",
              "ROAD": "1",   # We update this dictionary with this
              "HILL": "2",
              "BUILDING": "3",
              "VALLEY": "4",
              "FOREST": "5"}


# in below code under line with break
# We will test if the user is not quiting (loc is not equal to 0)
# Then create a combined directory by taking a copy of an instance of the
# "exits" dictionary and updating it to include the appropriate "namedExits"

# Explain (1), here we use ", ".join(locations[loc]["exits"].keys())"
# to extract the exits value from the master dictionary "locations"
# So we use "locations[loc]" to go to location 1 (section for road)
# Then we go further to "join(locations[loc]["exits"]" to extract key  named "exits"
# Then use "join(locations[loc]["exits"].keys())" to extract the "values" of "exits" key


loc = 1 # We are starting at position 1
print("First position(loc) = {}".format(loc))
while True:
    availableExits = ", ".join(locations[loc]["exits"].keys()) # Explain(1) Extract exits value from locations
    print("availableExits = {}".format(availableExits))
    print("You are in position: {}".format(loc))  # print position number which is loc
    print("Desc of your location: {}".format(locations[loc]["desc"])) # Description of your location is pulled from "loc" then "desc" keys

    if loc == 0:    # if location is 0, break (because you want to quit)
        break
    else:
        allExits = locations[loc]["exits"].copy() # pull exits from locations using key "loc" and "exits"
        print("allExits before update: {}".format(allExits)) # AllExits before being added with namedExits
        allExits.update(locations[loc]["namedExits"]) # combine "exits" and "namedExits"
        print("allExits after update: {}".format(allExits)) # allExits after update

    # we choose a direction and assign it to variable named "direction"
    direction = input("Enter Direction: "+ availableExits +" : ").upper() # Enter exit. it converts to uppercase to match keys
    print()

    # This is the code we will add for this step
    # We parse the user input (stored in "direction", and check if it exists in "vocabulary"

    if len(direction) > 1: # if user entered more than one letter, check vocabulary dictionary
        words = direction.split()  # We take input in "direction", split it by space, then assign it to variable "words"
        print("split words are: {}".format(words)) # We print words here just to see what it has. Not necessary for the code
        for word in words: # loop through all the entries in "words"
            if word in vocabulary: # if any of entries in "words" match key in vocabulary
                direction = vocabulary[word] # retrieve the "value" corresponding to "key" in vocabulary and assign it to direction
                break # Then we break from the "if word in words"

    # Then we use the new "direction" here as normal. so if user typed "QUIT", above code assigns "Q" to direction
    # Then in below code, direction will be "Q" and it will run as normal

    if direction in allExits: # here we test for "allExits"
        loc = allExits[direction]  # new loc is given value in combined dictionary "allExits"
        print("New position = : {}: Description = : {}".format(loc, locations[loc]))
    else:
        print("You cannot go in that direction")
