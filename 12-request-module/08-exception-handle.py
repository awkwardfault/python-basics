# try and except:
# In Python, exceptions can be handled using a try statement.
# The critical operation which can raise an exception is placed inside the try clause.
# The code that handles the exceptions is written in the except clause.
# We can thus choose what operations to perform once we have caught the exception.


num1 = int(input('Enter the number:'))
num2 = int(input('Enter another number:'))

try:
    print(num1/num2)
except ZeroDivisionError:
    print('Can not divide by zero')
except ValueError:
    print('Input should be int')
except TypeError:
    print('Invalid input')
