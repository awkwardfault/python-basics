# putting a list as a variable:

def myfunction(numbers):
    result = 0
    for number in numbers:
        result += number
    return result


result = myfunction([1, 2, 3, 4, 5])
print('sum of list is:', result)


# manipulating list with indexing:
def listfunction(li):
    li[0] = 10
# changing the index 0 to 10


mylist = [1, 2, 3, 4, 5]
print('before callin the function:', mylist)
listfunction(mylist)
print('after calling the function:', mylist)
# after calling the function it also manipulates the orinal list
