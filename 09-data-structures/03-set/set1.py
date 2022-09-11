# set starts and ens with second brackets or curly brackets
# we can't keep same item twice in set
# we can create empty sets:
a = set()
print(type(a))
# we can create set from a list or tuple:
li = [1, 2, 3, 4]
tpl = ('a', 'b', 'c')

aset = set(li)
bset = set(tpl)
print(type(aset), aset)
print(type(bset), bset)

# we can aslo create set from strings but all the elements of a string will store separately in set:
country = 'Portugal'
cset = set(country)
print(type(cset), cset)  # the elements in set also places itself by order

# we can also check if an item is in a set or not:
numset = {1, 2, 3, 4}
print(1 in numset, 10 in numset)

# set intersection: creates a new set with the similar items in two sets:
x = {1, 2, 3, 4}
y = {1, 4, 7, 8}

z = x & y
print(type(z), z)

# set union; creates a new set with by joining two sets:
union = x | y
print(union)

# to create a set with the unique items:
unique = x ^ y
print(unique)

# unique only to set x:
xuq = x - y
print(xuq)
