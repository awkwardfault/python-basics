# list is mutable; meaning it can be changed

# append() ; to add an element to the list:
my_list = ['Germany', 'Poland', 'Belgium']
my_list.append('Italy')
print(my_list)

# sort() ; for sorting the list:
mylist = [8, 5, 3, 2]
mylist.sort()
print(mylist)

# reverse() ; prints the list in reverse:
list = [1, 6, 4, 8]
list.reverse()
print(list)

# insert(index, item) ; to add an item in a specific place:
li = ['apple', 'banana']
li.insert(1, 'mango')
print(li)

# remove():
li1 = ['apple', 'banana', 'jackfruit']
li1.remove('jackfruit')
print(li1)

# pop(); removes the last item by default and prints it, but if given the index removes the item accordingly:
li2 = ['max', 'jack', 'oggy']
li2.pop()
print(li2)
li2.pop(1)
print(li2)

# extend(); to join two lists:
li3 = [1, 2, 3, 4]
li4 = [5, 6, 7, 8]
li3.extend(li4)
print(li3)

# count(); shows how many times an item is mentioned in the list:
li5 = [1, 3, 3, 3, 3, 4, 5]
print(li5.count(3))

# del(); to delete a whole list or an item by indexing:
li6 = [1, 2, 3, 4]
del (li6[1])
print(li6)
# del (li6)
# print(li6)  # NameError: name 'li6' is not defined

# empty list:
li7 = []
for x in range(10):
    li7.append(x)
print(li7)

# join() method:
li8 = ['a', 'b', 'c']
li8_new = '-'.join(li8)
print(li8_new)
