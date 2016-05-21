import datetime
import json

class Person():

    EYES_COLOR = ["Blue", "Green", "Brown"]
    GENRES = ["Female", "Male"]

    '''Constructor'''
    def __init__(self, id, first_name, date_of_birth, genre, eyes_color):
        self.__id = id
        if id < 0 and isinstance(id, int):
            raise Exception("id is not an integer")

        self.__first_name = first_name
        if first_name is " " and isinstance(first_name, str):
            raise Exception("string is not a string")

        self.__date_of_birth = date_of_birth #3 int
        if len(date_of_birth)  != 3 and isinstance (n, int):
            raise Exception("date_of_birth is not a valid date")

        self.__genre = genre
        if genre not in Person.GENRES:
            raise Exception("genre is not valid")

        self.__eyes_color = eyes_color
        if eyes_color not in Person.EYES_COLOR:
            raise Exception("eyes_color is not valid")

        self.last_name = ""
        
    '''Destructor'''    
    def __del__(self):
        pass

    '''getters for private attributes'''
    def get_id(self):
        return self.__id
            
    def get_first_name(self):
        return self.__first_name
                
    def get_date_of_birth(self):
        return self.__date_of_birth

    def get_genres(self):
        return self.__genres

    def get_eyes_color(self):
        return self.__eye_color

    '''returns strings fist name and last name'''
    def __str__(self):
        return "%s %s" %(self.__first_name , self.last_name)

    '''Check if Male'''
    def is_male(self):
        if self.__genre is "Male":
            return True
        else:
            return False

    def age(self):
        today = datetime.date.today()

        age = today.year - self.__date_of_birth[2]
        
        if today < datetime.date(today.year, self.__date_of_birth[0], self.__date_of_birth[1]):
            age -= 1

        self._age = age
        return age

    '''all comparators aroud age / what about cmp function?'''
    def __eq__(self, other):
        return self.age() == other.age()
    def __ne__(self, other):
        return self.age() != other.age()
    def __lt__(self, other):
        return self.age() < other.age()
    def __gt__(self, other):
        return self.age() > other.age()
    def __le__(self, other):
        return self.age() <= other.age()
    def __ge__(self, other):
        return self.age() >= other.age()

class Baby(Person):
    def can_run(self):
        return False
    def need_help(self):
        return True
    def is_young(self):
        return True
    def can_vote(self):
        return False


class Teenager(Person):
    def can_run(self):
        return True
    def need_help(self):
        return False
    def is_young(self):
        return True
    def can_vote(self):
        return False

class Adult(Person):
    def can_run(self):
        return True
    def need_help(self):
        return False
    def is_young(self):
        return False
    def can_vote(self):
        return True

class Senior(Person):
    def can_run(self):
        return False
    def need_help(self):
        return True
    def is_young(self):
        return False
    def can_vote(self):
        return True


def json(self):
    json = {'id': self.__id,
            'eyes_color' : self.__eyes_color,
            'genre' : self.__genre,
            'date_of_birth': self.__date_of_birth,
            'first_name' : self.__first_name,
            'last_name' : self.__last_name }
    return json


def load_from_json(self, json):
 if type(json) is not dict:
            raise Exception("json is not valid") 
 self.__id = json['id']
 self.__eyes_color = json['eyes_color']
 self.__genre = json['genre']
 self.__date_of_birth = json['date_of_birth']
 self.__first_name = json['first_name']
 self.__last_name = json['last_name']


def save_to_file(list, filename):
  with open(filename,'w') as outfile:
      strings  = []
      for i in list:
          strings.append(i.json())
          outfile.write(json.dumps(strings, indent = 2))

def load_from_file(filename):
    with open(filename) as data_file:
        json = []
        data = json.load(data_file)
        for line in data:
            p.load_from_json(line)
            json.append(p)
        return data
        
