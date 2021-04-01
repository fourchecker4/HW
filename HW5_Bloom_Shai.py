class Clock():
    def __init__(self, time):
        self.time = time
    def print_time(self):
        time = '6:30'
        print(self.time)
        
clock = Clock('5:30')
clock.print_time()

class Clock():
    def __init__(self, time):
        self.time = time
    def print_time(self, time):
        print(time)
        
clock = Clock('5:30')
clock.print_time('10:30')

class Clock():
    def __init__(self, time):
        self.time = time
    def print_time(self):
        print(self.time)
        
class Clock1(Clock):
    pass

boston_clock = Clock('5:30')
paris_clock = Clock1('10:30')

boston_clock.print_time()
paris_clock.print_time()

class Queue:
    def __init__(self):
        self = self
    value = []
    def insert(self, number):
        self.value.append(number)
    def remove(self):
        if self.value == []:
            print('queue is empty now.')
        else:
            self.value.pop(0)
    def print(self):
        print(self.value)
        
        
queue = Queue()
queue.insert(5)
queue.insert(6)
queue.print()

queue.insert(7)
queue.remove()
queue.print()

queue.remove()
queue.remove()
queue.remove()
