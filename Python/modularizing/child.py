import parent # running only this, the terminal prints out 25, Anna, hello

# Importing a module created a directory called __pycache__ which contains a .pyc file
# That .pyc file contains Python bytecode - the language the Python interpreter speaks.

# Namespace = which variables, functions, and classes are accessible to us at any given time during a program's execution.
print(locals()) # to see what variables are available at any given time

# running this, 'parent' is printed in the console since I added print(__name__) in parent.py

# Running this, the terminal prints out: The file is being executed because it is imported by another file. The file is called: parent