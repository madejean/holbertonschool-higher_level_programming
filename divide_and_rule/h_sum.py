import threading

class Sum():
    total = 0
    def __init__(self, nb_threads, numbers):
        self.threads = []
        self.nb_threads = nb_threads
        if not isinstance(nb_threads, int):
            raise Exception("nb_threads is not an integer")
        self.numbers = numbers
        if not isinstance(numbers, list):
            raise Exception("numbers is not an array of integers")
        Sum.total = 0

        if len(numbers) >= nb_threads:
            part = nb_threads
        else:
            part = len(numbers)
        div = [len(numbers) // (part)] * part
        sub = len(numbers)-sum(div)
        div[:sub] = [i + 1 for i in div[:sub]]
        List = [numbers[sum(div[:d]):sum(div[:d+1])] for d in range(part)]
        for part in List:
            thread = SumThread(part)
            self.threads += [thread]
            thread.start()

    def isComputing(self):
        for thread in self.threads:
            if thread.isAlive():
                return True
        return False

    def __str__(self):
        return str(Sum.total)


class SumThread(threading.Thread):
    lock = threading.Lock()

    def __init__(self, numbers):
        threading.Thread.__init__(self)
        self.numbers = numbers
        if not isinstance(numbers, list):
            raise Exception("numbers is not an array of integers")

    def run(self):
        i = 0
        for n in self.numbers:
            i += n
        SumThread.lock.acquire()
        Sum.total += i
        SumThread.lock.release()
