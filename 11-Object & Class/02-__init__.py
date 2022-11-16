# __init__ is a method
# and the first parameter of this method is 'self'

class Rocket:
    def __init__(self, n, c):
        self.name = n
        self.color = c

    def launch(self):
        print('Lanuching the Rocket', self.name, 'in t minus seconds')


new_rocket = ('Europha', 'White')
# print(self.n, self.c)
new_rocket.launch()
