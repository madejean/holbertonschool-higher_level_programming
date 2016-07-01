import threading
import urllib2

lock = threading.Lock()

class LoripsumThread(threading.Thread):

    def __init__(self, filename):
        threading.Thread.__init__(self)
        self.filename = filename

    def run(self):
        lock.acquire()
        url = urllib2.urlopen("http://loripsum.net/api/1/short")
        r = url.read()
        f = open(self.filename, "aw")
        f.write(r)
        f.close()
        lock.release()
