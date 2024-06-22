local_val = "magical unicorns"

def square(x):
    return x * x

class User:
    def __init__(self, name):
        self.name = name
    
    def say_hello(self):
        return "hello"


print(square(5)) #25
user = User("Anna")
print(user.name) # Anna
print(user.say_hello()) # hello

# Whenever we create a new file & execute it, the Python interpreter automatically creates the variable __name__ & is assigned a value
print(__name__) #__main__


if __name__ == "__main__": # this will print when parent.py is run
    print("the file is being executed directly")
else: # this will print when child.py is run
    print("The file is being executed because it is imported by another file. The file is called: ", __name__)

# Running parent.py, the terminal prints out: the file is being executed directly.