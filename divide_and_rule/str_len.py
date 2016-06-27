import threading
import sys

class StrLengthThread(threading.Thread):

    def __init__(self, word):
        threading.Thread.__init__(self)
        self.word = word
        if not isinstance(word, str):
            raise Exception("word is not a string")

    def run(self):
        global total_str_length
        StrLengthThread.total_str_length += len(self.word)

text = sys.argv[1]
thread = []

if len(text) is not None:
     total_str_length = len(text)

for w in text:
    str_length_thread = StrLengthThread(w)
    thread += [str_length_thread]
    str_length_thread.start()

for t in thread:
    t.join()

print "%d" % total_str_length
