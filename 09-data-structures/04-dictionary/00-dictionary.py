# let's say we want to assign marks of the students somewhere
# we can easily do that with list; like this:

marks = [70, 80, 90, 100]
roll = input('Enter roll number:')
print('Your mark is:', marks[int(roll)-1])

# but like this we have to remember role numbers of all the stuednts; and if we want to add multiple numbers
#  for one roll we also have to remember which number belons to which subject;

marks1 = [[70, 80], [80, 80], [90, 90], [90, 100]]
print('Your mark is:', marks1[int(roll)-1])
