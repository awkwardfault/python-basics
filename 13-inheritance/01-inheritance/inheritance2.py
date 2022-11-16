from inheritance1 import device


class laptop(device):  # child class
    '''laptop class'''

    def restart(self):
        '''method for restarting laptop'''
        print(self.name, 'is restarting')


c = laptop('vivobook', 'asus', 'windows')
c.start()
c.specs()
c.restart()


class tv(device):
    '''class for tv'''

    def change_channel(self, channel_no):
        '''method for changing channel'''
        print(self.company, self.name, 'tv is changing channel to', channel_no)


t1 = tv('led', 'lg', 'android')
t1.start()
t1.change_channel(72)
