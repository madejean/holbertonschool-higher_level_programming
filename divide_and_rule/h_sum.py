import threading

class Sum:

    def __init__(self, nb_threads, numbers):
        self.nb_threads = nb_threads
        if not isinstance(nb_threads, int):
            raise Exception("nb_threads is not an integer")
        self.numbers = numbers
        if not isinstance(numbers, list):
            raise Exception("numbers is not an array of integers")

    def isComputing(self):

    def __str__(self):
        return Sumstr

class SumThread(threading.Thread):

    def __init__(self, numbers):
        self.numbers = numbers
        if not isinstance(numbers, int):
            raise Exception("numbers is not an array of integers")

    def run(self):
        """compute the sum of all integers inside numbers array"""
