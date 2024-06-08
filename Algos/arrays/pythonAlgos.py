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