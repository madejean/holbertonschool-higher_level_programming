import threading

class FibonacciThread(threading.Thread):

    def __init__(self, number):
        threading.Thread.__init__(self)
        self.number = number
        if not isinstance(number, int):
            raise Exception("number is not an integer")

    def run(self):
        a = 0
        b = 1
        for i in range(self.number):
            temp = a
            a = b
            b = temp + b
        print "%d => %d" % (self.number, a)
