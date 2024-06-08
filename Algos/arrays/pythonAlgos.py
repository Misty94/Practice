# Create a function that accepts a number as input.
# Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element)

def countdown (a):
    b = a - 1
    downList = [a, b]
    for x in downList:
        b -= 1
        downList.append(b)
        if b == 0:
            return downList
        
j = countdown(5)
d = countdown(10)
print(j)
print(d)


def countdown2(num):
    new = []
    for i in range(num, -1, -1):
        new.append(i)
    return new

print(countdown2(5))
print(countdown2(10))


# Create a function that will receive a list with two numbers.
# Print the first value and Return the second.

def printAndReturn (twoList):
    print(twoList[0])
    return twoList[1]

print(printAndReturn([1,2]))
print(printAndReturn([8,10]))


# Create a function that accepts a list and returns the sum of the first value in the list plus the list's lenght

def firstPlusLength(list):
    sum = list[0] + len(list)
    return sum

print(firstPlusLength([1,2,3,4,5])) # 6
print(firstPlusLength([2,4,6,8,10])) # 7


# Write a function that accepts a list & creates a new list containing only the values from the original list that are greater than its 2nd value.
# Print how many values this is & Return the new list
# If the list has less than 2 elements, have the function return False

def greaterValue(list):
    if len(list) < 2:
        return False
    newList = []
    count = 0
    for i in range(len(list)):
        if list[i] > list[1]:
            newList.append(list[i])
            count += 1
    print(count) # Or I could have just print(len(newList))
    return newList

print(greaterValue([5,2,3,2,1,4]))
print(greaterValue([3]))
print(greaterValue([8,1,-3,5]))


# Write a function that accepts two integers as parameters: size and value
# The function should create and return a list whose length is equal to the given size & whose values are all the given value.

def sizeValue(size, value):
    list = []
    for i in range(0, size):
        list.append(value)
    return list

print(sizeValue(4,7)) # [7,7,7,7]
print(sizeValue(6,2)) # [2,2,2,2,2,2]