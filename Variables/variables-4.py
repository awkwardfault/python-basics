# default variables 2

def myfunction(x, y=10, z):
    print('x=', x, 'y=', y, 'z=', z)


x = 5
y = 6
z = 7
myfunction(x, y, z)

# if we execute this program we'll get an error saying: 'SyntaxError: non-default argument follows default argument'
# that means if we want to define a default variable or parameter it should be in the last or all the variables after the
#  first defined variable should be defined as well.


# in order to define just y ; it should be in the last like this:

def myfunction1(x, z, y=10):
    print('x=', x, 'y=', y, 'z=', z)


a = 5
b = 6
c = 111
myfunction1(a, b)
