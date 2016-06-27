import threading

class OrderedArray:
    array = []

    def __init__(self):
        self.threads = []

    def add(self, number):
        self.number = number
        if not isinstance(number, int):
            raise Exception("number is not an integer")
        thread = OrderedArrayThread(number)
        self.threads += [thread]
        thread.start()

    def isSorting(self):
        for thread in self.threads:
            if thread.isAlive():
                return True
        return False

    def __str__(self):
        return str(OrderedArray.array)

class OrderedArrayThread(threading.Thread):
    lock = threading.Lock()

    def __init__(self, number):
        threading.Thread.__init__(self)
        self.number = number
        if not isinstance(number, int):
            raise Exception("number is not an integer")

    def run(self):
        OrderedArrayThread.lock.acquire()
        OrderedArray.array.append(self.number)
        OrderedArray.array.sort()
        OrderedArrayThread.lock.release()
