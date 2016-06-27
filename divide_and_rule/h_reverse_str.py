import threading

class ReverseStrThread(threading.Thread):
    sentence = ""
    lock = threading.Lock()

    def __init__(self, word):
        threading.Thread.__init__(self)
        self.word = word
        if not isinstance(word, str):
            raise Exception("word is not a string")

    def run(self):
        ReverseStrThread.lock.acquire()
        Reverse_str = self.word[::-1]
        ReverseStrThread.sentence += Reverse_str
        ReverseStrThread.sentence += " "
        ReverseStrThread.lock.release()
