# string should always start and end with quotation
# string is immutable or non-mutable: that means string can't be changed
# len() function:
test = 'hello'
print(len(test))

# indexing: starts with position 0 not 1;
city = 'California'

print(city[0])
print(city[1])
print(city[6])

# using loop in string:
country = 'Qatar'
for c in country:
    print(c)
    # note: string can not be manipulted like list by indexing

# joinin strings:
city2 = 'New' + 'york'
print(city2)
x = '10' + '5'
print(x)  # should print 105

# find() method:
country2 = 'Brazil'
print(country2.find('z'))  # shows the position
print(country2.find('t'))  # should return -1 for being false

# replace() method:
name = "max smith"
new_name = name.replace('max', 'jax')
print(new_name)

# strip() method: (lstrinp,rstrip) ; removes space from a string
name2 = '  diana  '
print(name2)
print(name2.rstrip())
print(name2.strip())  # removes space from both side

# upper()/lower()
name3 = 'fifa'
print(name3.upper())
name4 = 'SONY'
print(name4.lower())

# split() method:
sen = 'I love python'
words = sen.split()
print(words)
# or
for word in words:
    print(word)

# count():
sen2 = 'lol is lol is lol is lol'

print(sen2.count('is'))

# endswith():
country3 = 'Bangladesh'
print(country3.endswith('sh'))
print(country3.endswith('zil'))
# startswith():
name5 = 'Mr. Max'
if name5.startswith('Mr.'):
    print('Dear Sir')
