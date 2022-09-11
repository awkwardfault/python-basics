# tuple uses first brackets or parenthesis ()
# empty tuples can be created just like empty list
# we can access all the items in a tuple with indexing
# tuples are not mutable or immutable; meaning they can't be changed

# packing in tuple:
numbers = (1, 2, 3, 4, 5)
n1, n2, n3, n4, n5 = numbers
print(n1)
print(n5)

# A tuple can contain different data types; and we can also use loops:
items = (1, 2, 5.5, ['a', 'b'], ('apple', 'banana'), True)
for item in items:
    print(item, type(item))
