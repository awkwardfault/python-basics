# local and global function:
# x = 20

def myfunction(x):
   # the first x is not defined inside the function so it prints the global value or outside value of x
    print(x)
   # now we are going to give x a value:
    x = 100
    print(x)
   #  the second x prints 100 as defined in previous line


# this is the global or outside x >>>>>>> note: we can also define the x before the function begins
x = 20
myfunction(x)
# this is the third print function
print(x)
# it's printing 20 because it's outside the function
# Note: we can also use the keyword 'global' to define a global variable inside the function
