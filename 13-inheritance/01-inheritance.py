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
