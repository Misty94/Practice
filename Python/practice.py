# Boolean Values = True and False
# Integers = Whole Numbers
# Floating Numbers = Decimal Numbers
# Strings = Literal Text
# Tuples = Cannot be altered after creation, can hold a group of values, can contain mixed data types

dog = ('Tonks', 'german shepherd', 12, False)
print(dog[1])

# Lists = holds a group of values & can change. Stores a collection of related data

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

# return statements mean Exit This Function Now - any remaining code will not be run & can pass a value to the outer scope
# A function call is equal to whatever that function returns & that returned value remains after the function is completed

# set defaults when declaring the parameters
def be_cheerful(name='', repeat=2):
    print(f"good morning {name}\n" * repeat)

# No argument provided, the defaults are used:
be_cheerful() # output: good morning (repeated on 2 lines) because the default is 2 & name is left off because it doesn't have a default value

# 1 unnamed argument provided, that value is used as the first parameter & the second's default value is used
be_cheerful("Emma") # output: good morning Emma (repeated on 2 lines)

#1 named argument provided, that value is used for that parameter, & the other's default is used
be_cheerful(name="Spinner") # output: good morning Spinner (repeated on 2 lines)
be_cheerful(repeat=6) # output: good morning (repeated on 6 lines)

# Both unnamed arguments provided - values assigned to parameters in order
be_cheerful("Zoey", 3)

be_cheerful(name="Miles", repeat=5) # output: good morning Miles (repeated on 5 lines)
be_cheerful(name="Maya", repeat=1) # output: good morning Maya (only on 1 line)

# Argument order doesn't matter if we are explicit when sending in our arguments!
# Both named arguments provided = Values assigned to associated parameter
be_cheerful(repeat=3, name="Zig")    # output: good morning Zig (repeated on 3 lines)



