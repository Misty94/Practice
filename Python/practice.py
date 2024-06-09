# Boolean Values = True and False
# Integers = Whole Numbers
# Floating Numbers = Decimal Numbers
# Strings = Literal Text
# Tuples = Cannot be altered after creation, can hold a group of values, can contain mixed data types, enclosed by ()

dog = ('Tonks', 'german shepherd', 12, False)
print(dog[1])

# Lists = holds a group of values & can change. Stores a collection of related data & enclosed by []

my_list = [44, 56, 2, 8, 12, 9, 50]

print(len(my_list)) # Prints the length of the list

my_list.reverse() # Reverses the order of the elements in the list, without making a new list

my_list.pop(2) # Removes the value at that given position 

my_list.sort() # Sorts the items in order of least - greatest or alphabetically for strings

my_list.append("Hello") # Adds a value to the end of the list

print(my_list.index('Hello')) # returns the index (position) of the given value or an error if no value exists

print(my_list) # 7 6 [2,8,9,44,50,56, 'Hello']

stuff = ['read', 748, 'diamond paint'] # Iterate through a list
for i in range(0, len(stuff)):
    print(i, stuff[i]) # 0 read, 1 748, 2 dimaond paint

for v in stuff:
    print(v) # read, 748, diamond paint


# Dictionaries = Group of key:value pairs. Indexed by unique keys which are used to access values

# and checks that each expression on the left & right are both true
(1 <= 2) and (2 <= 3) # True

# or checks if either expression on the left or right is true
(1 <= 2) or (2 >= 3) # True

# not reverses the true-false value
x = [1, 2]
if not x:
    print('evermore') # does not print anything

x = []
if not x:
    print('evermore') # prints evermore


# Loop Examples
# One Argument
for i in range(5): # starts at 0 by default & increases by 1 by default
    print(i) # 0 1 2 3 4 

# Two Arguments
for i in range(2, 7): # starts at 2, exits the loop at 7
    print(i) # 2 3 4 5 6

# Three Arguments => if you need to increase by more than 1, all 3 arguments required
for i in range(2, 16, 3): # increases by 3
    print(i) # 2 5 8 11 14

for x in range(5, 1, -3): # To decrease, use a negative number
    print(x) # 5, 2

for x in 'Misty':
    print(x) # 'M' 'I' 'S' 'T' 'Y'

# Print integers 1 to 100. If divisible by 5, print "Stranger" instead. If divisible by 10, print "Danger!"
for i in range(1, 101):
    if i % 10 == 0:
        print("Danger!")
    elif i % 5 == 0:
        print("Stranger")
    else:
        print(i)

# Add odd integers from 0 to 500,000 and print final sum
sum = 0
for i in range(1, 500001, 2):
    sum += i
print(sum)

sum = 0
for i in range(0, 500001):
    if i % 2 == 1:
        sum += i
print(sum)

# Starting with a lowNum going through to a highNum, only print the integers that are a multiple of mult
lowNum = 3
highNum = 67
mult = 5
for i in range(lowNum, highNum):
    if i % mult == 0:
        print(i)


# While Loops => include progress towards making the expression False, otherwise, it'll never end
count = 0
while count <= 5:
    print("looping - ", count)
    count += 1

# While loops are used when it's unclear when your loop might need to stop
y = 8
while y > 0:
    print(y)
    y = y - 2
else:
    print("Final else statement")

# Break Example => Break stops the loop
for val in "Misty":
    if val == "t":
        break
    print(val) # M i s

# Continue Example => Continue stops where it's at, goes back to the beginning of the loop, & continues on
for val in "Misty":
    if val == "s":
        continue
    print(val) # M i t y


def say_hi(name): # name is the parameter 
    return "Hi, " + name

greeting = say_hi("Marlow")
print(greeting)
print(say_hi("Veronica"))
print(say_hi("Darcy")) # Marlow, Veronica, and Darcy are the arguments


# print() doesn't have any effect on your program; it is used for Debugging & to see what's happening!!!! Helps visualize your code

def multiply(num_list, num):
    print("num_list is", num_list, "and num is", num) # num_list is [2,4,10,16] and num is 5
    for x in num_list:
        print("This is x:", x) # 2 # 4 # 10 # 16
        x *= num
        print("X is now this:", x) # 10 # 20 # 50 # 80
        print("This is num_list:", num_list) # num_list never changes! Google 'unable to modify list value in for loop python'
    return num_list
a = [2, 4, 10, 16]
b = multiply(a,5)
print(b) # [2,4,10,16]

# Now Fixed:
def multipy2(num_list, num):
    for x in range(len(num_list)):
        num_list[x] *= num
    return num_list
a = [2, 4, 10, 16]
b = multipy2(a, 5)
print(b) #[10,20,50,80]


# return statements mean Exit This Function Now - any remaining code will not be run & can pass a value to the outer scope
# A function call is equal to whatever that function returns & that returned value remains after the function is completed


# set defaults when declaring the parameters
def be_cheerful(name='', repeat=2):
    print(f"good morning {name}\n" * repeat)

# No argument provided, the defaults are used:
be_cheerful() # output: good morning (repeated on 2 lines) because the default is 2 & name is left off because it doesn't have a default value

# 1 unnamed argument provided, that value is used as the first parameter & the second's default value is used
be_cheerful("Emma") # output: good morning Emma (repeated on 2 lines)

# 1 named argument provided, that value is used for that parameter, & the other's default is used
be_cheerful(name="Spinner") # output: good morning Spinner (repeated on 2 lines)
be_cheerful(repeat=6) # output: good morning (repeated on 6 lines)

# Both unnamed arguments provided - values assigned to parameters in order
be_cheerful("Zoey", 3)

be_cheerful(name="Miles", repeat=5) # output: good morning Miles (repeated on 5 lines)
be_cheerful(name="Maya", repeat=1) # output: good morning Maya (only on 1 line)

# Argument order doesn't matter if we are explicit when sending in our arguments!
# Both named arguments provided = Values assigned to associated parameter
be_cheerful(repeat=3, name="Zig")    # output: good morning Zig (repeated on 3 lines)


# When a function doesn't return anything, it outputs None
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x) # 5, None


def concatenate(b,c):
    return str(b) + str(c)
print(concatenate(2,5)) # 25


# Python Dictionaries:
# unordered collection of objects
# values are accessed using a key (typically a string)
# can shrink or grow as needed & the contents can be modified & can be nested
# sequence operations such as slice cannot be used

# Keys are usually strings, but the values can be any type.
# Keys are like the label for the stored value

person = {"first": "Hermione", "last": "Granger", "age": 15, "is_witch": True}
capitals = {} # an empty dictionary
book = {  # another way to write out a dictionary
    "title": "Harry Potter and the Order of the Phoenix",
    "format": "hardcover",
    "pages": 870,
    "have_read": True
}

# Dictionaries do not have an .append(). Instead, you add new values by setting a new key (like you would a variable.)

capitals["USA"] = "Washington D.C"
capitals["Mexico"] = "Mexico City"
capitals["France"] = "Paris"

person2 = {"first": "George", "last": "Weasley", "age": 17, "is_wizard": True}
print(person2)
capitals["Sweden"] = "Stokholm"
capitals["Russia"] = "Moscow"
print(capitals)

# Each Key Must Be Unique!
# If you use an existing key as the index, the old value associated with that key is Overwritten by the new value.

person3 = {"first": "Ada", "last": "Lovelace", "age": 42, "is_organ_donor": True}
person3["email"] = "alovelace@codingdojo.com" # Adds a new key value pair for email to person
person3["last"] = "Bobada" # Changes person's "last" value to "Bobada"
print(person3)
# The syntax is the same for adding a new value as it is for updating a value!

# Testing For An Existing Key
if "favorite_class" in person:
    print("favorite_class already exists")
else:
    person["favorite_class"] = "all_of_them"
print(person)

if "Peru" not in capitals:
    capitals["Peru"] = "Lima"
else: 
    print("Peru is already included.")
print(capitals)


full_name = person["first"] + " " + person["last"]
print(full_name)


cities_so_far = {"Charlotte": 2, "New Orleans": 1}
new_visits = ["NYC", "Las Vegas", "Orlando", "New Orleans"]

cities_so_far["NYC"] = 1
cities_so_far["New Orleans"] += 1
cities_so_far["Orlando"] = 1
cities_so_far["Las Vegas"] = 1
print(cities_so_far)


# Removing Values
value_removed = cities_so_far.pop("NYC") # This will remove the key "NYC" and return its value 1
del cities_so_far['Las Vegas'] # This will delete the key, and not return anything
print(cities_so_far)


# Built In Functions
print(len(cities_so_far)) # 3 - Gives the total length of the dictionary
print(str(cities_so_far)) # Produces a string representation of a dictionary
print(type(cities_so_far)) # dict - Returns the type of the passed variable

# Built in Methods
#.get(key, default=None) Safe way to get a value, if the key might not exist. Returns the value for the specified key or None (or a value you specify) if the key is not in the dictionary.
x = cities_so_far.get("Orlando")
print(x) # 1
j = cities_so_far.get("Paris")
print(j) # None
# Add and update multiple key-value pairs at once, by passing in another dictionary of the pairs to update & add
cities_so_far.update({"Boston": 1, "New Orleans": 3}) 
print(cities_so_far)
# Removes all elements from the dictionary
cities_so_far.clear()
print(cities_so_far) # {} empty dictionary


# For Loops Through Dictionaries
my_dict = {"name": "Elsbeth", "language": "Python"}
for each_key in my_dict:
    print(each_key) # name, language

for each_key in my_dict:
    print(my_dict[each_key]) # Elsbeth, Python

us_capitals = {
    "Virginia": "Richmond",
    "North Carolina": "Raleigh",
    "Texas": "Austin",
    "New York": "Albany"
}

for key in us_capitals.keys():
    print(key) # Virginia, North Carolina, Texas, New York

for val in us_capitals.values():
    print(val) # Richmond, Raleigh, Austin, Albany

for key, val in us_capitals.items():
    print(key, " = ", val) # Virginia = Richmond, North Carolina = Raleigh, etc.


# Nesting - dictionaries can contain lists, tuples, and other dictionaries. Lists can contain dictionaries. It can be many levels deep.

# List of Dictionaries
users = [
    {"first": "Katniss", "last": "Everdeen"}, # index 0
    {"first": "Peeta", "last": "Mellark"}, # index 1
    {"first": "Gale", "last": "Hawthorne"} # index 2
]

print(users[0]["last"]) # Everdeen

# Dictionary of Lists
resume_data = {
        #           0           1           2
    "skills": ["front-end", "back-end", "database"],
    "languages": ["Python", "Java", "JavaScript"],
    "hobbies": ["reading", "diamond painting", "making friendship bracelets"]
}

print(resume_data["skills"][1]) # back-end
print(users[2]["first"]) # Gale

# If it starts with {curly}, it's the start of a dictionary & you need a key to access something one level further into it
# If it starts with [brackets], it's a list & you need an index to go one level further into it


# Update Values in Dictionaries & Lists

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


# Change the value 10 in x to 15
x[1][0] = 15
print(x) # [5,2,3], [15,8,9]

# Change the last_name of the first student from Jordan to Bryant
students[0]["last_name"] = "Bryant"
print(students)

# In the sports directory, change Messi to Andres
sports_directory["soccer"][0] = "Andres"
print(sports_directory)

# Change the value 20 in z to 30
z[0]['y'] = 30
print(z)


# Iterate Through a List of Dictionaries
# Create a function that given a list of dictionaries, the function loops through each dictionary in the list & prints each key and value.
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(students):
    for i in range(len(students)): 
        output = ""
        for key, val in students[i].items():
            output += f"{key} - {val}, "
        print(output)

print(iterateDictionary(students))


# Get Values From a List of Dictionaires
# Create a function that given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary

def iterateDictionary2(key_name, students):
    for i in range(len(students)):
        pass