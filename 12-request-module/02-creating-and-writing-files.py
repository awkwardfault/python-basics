# to create and write a file:

fp = open('test.txt', 'w')  # to create a .txt file we used the method 'open'
# then we named the file test.txt after that we wrote 'w' to indicate that
# we will be writing the file
# we used .write to write the line in the txt file that we created
fp.write('this file was created using python')
fp.close()  # then we used close() to close the file

# now a .txt file should be created in the folder and the following line should be in that file


# let's see what fp is:
print(type(fp))
# so fp is an object of _io module and textwrapper class.
