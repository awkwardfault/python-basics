# inheritance comes from the word inherit...like inheritting someones will or property
# it is used for simplifying and shortening a big similar project to a small one
# for example there are many similarities in a smartphone and a laptop
# we can create a class for both of them that contains the similarities. which is called a parent class
# then we can create seperate classes for them which contains the features unique to them which is called a child class


class device:
    ''' Base or parent class for all devices '''

    def __init__(self, name, company, os):
        self.name = name
        self.company = company
        self.os = os

    def start(self):
        print(self.name, 'is turning on')
        print(self.name, 'runs on', self.os)

    def specs(self):
        print(self.name, 'is manufactured by',
              self.company, 'and runs on', self.os)

    def turnoff(self):
        print(self.name, 'is turning off')


if __name__ == '__main__':
    p1 = device('s22', 'samsung', 'android')
    p2 = device('se', 'iphone', 'ios')
    p3 = device('e72', 'nokia', 'symbian')

    p1.start()
    p2.specs()
    p3.specs()
    p3.turnoff()


if __name__ == '__main__':
    print('module ran directly')
else:
    print('module ran by importing')
