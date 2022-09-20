# we are going to create a function to know if a number is even or not
if __name__ == "__main__":
    print("Module1 ran directly")
else:
    print('Module1 ran by importing')
# we'll discuss the upper part later


def even_num(n):
    if n % 2 == 0:
        print(n, 'is a even number')
    else:
        print(n, 'is not a even number')


even_num(4)
# now we are going to use ths code block in an another .py file in this case module2.py


# __name__ == __main__ means the code after that will execute when running the main file in this case  module1.py
#   and if we also give a else statement; the later code will execute when the code is ran by importing to another
#       .py file, in this case module2.py
