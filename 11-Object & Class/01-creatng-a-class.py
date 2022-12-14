# to create a class in python we just have to write the word class then give a space and then write the name of the class
# exmaple:
class Rocket:  # we should always start the name of the class with a capital letter
    name = 'Venus777'
    color = 'Beige'  # these are attributes we created for the class

    def launch():  # now we created a method called launch
        # and instructed the method what to do next
        print('Launching', Rocket.name)
        # the method will not print or work if we stop here. we have to call the object


print('Name of the rocket:', Rocket.name)
print('Color of the rocket:', Rocket.color)
# these two lines will print because we called the attributes of the class
Rocket.launch()  # calling the object

# what if we wanted to name the attributes later or update them:
Rocket.name = 'Europha'
Rocket.color = 'White'
print('Name of the new rocket:', Rocket.name)
print('Color of the new rocket:', Rocket.color)
Rocket.launch()  # calling the object
# we can also leave the attributes empty and update them later
