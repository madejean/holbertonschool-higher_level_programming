import threading
import requests
import json

class IPThread(threading.Thread):

    def __init__(self, ip, callback):
        threading.Thread.__init__(self)
        self.ip = ip
        self.callback = callback
        
        def run(self):
            print "Search: ", self.ip
            url = "https://api.ip2country.info/ip?" + self.ip
            r = requests.get(url)
            countryName = json.loads(r)['countryName']
            self.callback(country_name)
            print "countryName:", country_name
