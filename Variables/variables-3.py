# default variable

def myfunction(y=10):
    print('y=', y)


x = 20
myfunction(x)
# because of calling the variable x the result is printing 20 same as x
myfunction()
# here we didn't call any variable, but it's printing 10 because we mentioned y=10 in line 3
#  and it's called default variable
