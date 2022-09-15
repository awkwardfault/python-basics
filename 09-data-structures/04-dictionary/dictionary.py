import pprint
# let's say we want to assign marks of the students somewhere
# we can easily do that with list; like this:

# marks = [70, 80, 90, 100]
# roll = input('Enter roll number:')
# print('Your mark is:', marks[int(roll)-1])

# but like this we have to remember role numbers of all the stuednts; and if we want to add multiple numbers
#  for one roll we also have to remember which number belons to which subject;

# marks1 = [[70, 80], [80, 80], [90, 90], [90, 100]]
# print('Your mark is:', marks1[int(roll)-1])


# so we can use dictionaries for easily processing this datas
# data in dictionaries stays in pairs called 'key,value' pairs
# dictionary uses second brackets or curly brackets
# Dictionaries cannot have two items with the same key
# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
# Duplicate values will overwrite existing values


# example:
marks2 = {'21dh09': 70,
          '98lo78': 80
          }
# we can store complex student ids or names like this

#  we can also create empty dictionary:
dt = {}
print(type(dt))

# dictionary with multiple datas:
countries_info = {}
countries_info['Afghanistan'] = {'Capital': 'Kabul', 'Currency': 'Afghani'}
countries_info['Albania'] = {'Capital': 'Tirane', 'Currency': 'Lek'}
countries_info['Algeria'] = {'Capital': 'Algiers', 'Currency': 'Dinar'}
countries_info['Andorra'] = {
    'Capital': 'Andorra la Vella', 'Currency': 'Euro'}

pprint.pprint(countries_info)

# .keys() method:
country_names = countries_info.keys()
print(country_names)
# same thing using loop:
for country in country_names:
    print(country)
# printing capitals:
for country in country_names:
    print(country + ';', 'Capital:', countries_info[country]['Capital'])

# adding items in dictionary:
countries_info['Angola'] = {'Capital': 'Luanda', 'Currency': 'New Kwanza'}

pprint.pprint(countries_info)

# items() method: prints all the key value pairs
x = countries_info.items()
print(x)

# update() method:
dict1 = {'car': 'tesla', 'year': 1998}
print(dict1)
dict1.update({'car': 'ford'})
print(dict1)

# adding items:
dict1['color'] = 'red'
print(dict1)

# pop() method:
dict1.pop('color')
print(dict1)

# del mehtod:
del dict1['car']
print(dict1)
# to delete the full dictionary: del dict1

# clear() method: clears the whole dictionary making it empty
dict1.clear()
print(dict1)

# copy() method:
dict2 = dict1.copy()
pprint.pprint(dict2)  # lol
# or
dict3 = dict(dict2)

# nested dictionaries:
myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
