# list comprehensions reduces the use of loops making the code faster and reliable:
# Example:
# # to multiply every item on a list we have to do this:
li = [1, 2, 3, 4]
newli = []
for x in li:
    newli.append(2*x)
print(newli)
# but we can do this task easily with list comprehensions:
lii = [1, 2, 3, 4]
newlii = [2 * x for x in lii]
print(newlii)
# Example2:
# if we want to get all the even numbers from 1 to 10:
li2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evennums = []
for x in li2:
    if x % 2 == 0:
        evennums.append(x)
print(evennums)
# with list comprehensions:
even_nums = [x for x in range(1, 11) if x % 2 == 0]
print(even_nums)
