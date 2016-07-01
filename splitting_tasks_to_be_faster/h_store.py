import threading
from time import sleep
from random import randint
 
class Store:
    
    def __init__(self, item_number, person_capacity):
        #number of items available
        self.item_number = item_number
        #store capacity
        self.person_capacity = person_capacity
        self.semaphore = threading.Semaphore(self.person_capacity)

    def enter(self):
        self.semaphore.acquire()
    
    def buy(self):
        sleep(randint(5,10))
        if self.item_number >= 0 :
            self.item_number -= 1
        if self.item_number < 0:
            return False
        self.semaphore.release()
        return True
