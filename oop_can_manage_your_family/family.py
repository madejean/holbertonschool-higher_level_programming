import datetime
import json
import  os

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
        if len(date_of_birth)  != 3 and isinstance (n, int) or (date_of_birth[1] < 1 or date_of_birth[1] > 31) or(date_of_birth[0] < 1 or date_of_birth[0] > 12):
            raise Exception("date_of_birth is not a valid date")

        self.__genre = genre
        if genre not in Person.GENRES:
            raise Exception("genre is not valid")

        self.__eyes_color = eyes_color
        if eyes_color not in Person.EYES_COLOR:
            raise Exception("eyes_color is not valid")

        self.last_name = ""
        
        self.is_married_to = 0

        self.children = []

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

    def get_genre(self):
        return self.__genre

    def get_eyes_color(self):
        return self.__eyes_color

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
        today = [5, 20, 2016]
        return today[2] - self.__date_of_birth[2]

    '''all comparators overloading around age / what about cmp function?'''
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
        
    def json(self):
        json = {'kind' : self.__class__.__name__,
                'id': self.__id,
                'eyes_color' : self.__eyes_color,
                'genre' : self.__genre,
                'date_of_birth': self.__date_of_birth,
                'first_name' : self.__first_name,
                'last_name' : self.last_name, 
                'is_married_to' : self.is_married_to }
        return json

    def load_from_json(self, json):
        if type(json) is not dict:
            raise Exception("json is not valid")
        self.__class__.__name__ = json['kind']
        self.__id = json['id']
        self.__eyes_color = json['eyes_color']
        self.__genre = json['genre']
        self.__date_of_birth = json['date_of_birth']
        self.__first_name = json['first_name']
        self.__last_name = json['last_name']
        self.is_married_to = json['is_married_to']
        
class Baby(Person):
    def can_run(self):
        return False
    def need_help(self):
        return True
    def is_young(self):
        return True
    def can_vote(self):
        return False
    def can_be_married(self):
        return False
    def is_married(self):
        if self.is_married_to != 0:
            return True
        else:
            return False        
    def divorce(self, p):
        self.is_married_to = 0
        p.is_married_to = 0
    def just_married_with(self, p): 
        if self.is_married_to != 0 or p.is_married_to != 0:
            raise Exception("Already married")
        if not self.can_be_married() or not p.can_be_married():
            raise Exception("Can't be married")
        self.is_married_to = p.get_id()
        p.is_married_to = self.get_id()
        if self.get_genre() == "Female" and p.get_genre() == "Male":
            self.last_name = p.last_name
        else:
            if self.get_genre() == "Male" and p.get_genre() == "Female":
                p.last_name = self.last_name
    def can_have_child(self):
        return False
    def has_child_with(self, p, id, first_name, date_of_birth, genre, eyes_color = ''):
        if p is None or p.__class.__name__ != 'Adult' and p.__class__.name != 'Senior':
            raise Exception("p is not an Adult of Senior")
        if (not p.can_have_child()) or(not self.can_have_child()):
            raise Exception("Can't have baby")        
        if self.get_eyes_color() == 'Blue' and p.get_eyes_color() == 'Blue' :
            eyes_color = 'Blue'
        if self.get_eyes_color() == 'Green' and p.get_eyes_color() == 'Green' :
            eyes_color = 'Green'
        if self.get_eyes_color() == 'Blue' and p.get_eyes_color() == 'Green' :
            eyes_color = 'Blue'
        if p.get_eyes_color() == 'Brown' :
            eyes_color = 'Brown'
        b = Baby(id,first_name,date_of_birth,genre,eyes_color)
        if id not in p.children:
            p.children.append(id)
        if id not in self.children:
            self.children.append(id)        
        return b

    '''link 2 persons by adding c.get_id() to self.children'''
    def adopt_child(self, c):
       if (not self.can_have_child()):
            raise Exception("Can't adopt child")
       self.children.append(c.get_id())


 
class Teenager(Person):
    def can_run(self):
        return True
    def need_help(self):
        return False
    def is_young(self):
        return True
    def can_vote(self):
        return False
    def can_be_married(self):
        return False
    def is_married(self):
        if self.is_married_to != 0:
            return True
        else:
            return False
    def divorce(self, p):
        self.is_married_to = 0
        p.is_married_to = 0
    def just_married_with(self, p):
        if self.is_married_to != 0 or p.is_married_to != 0:
            raise Exception("Already married")
        if not self.can_be_married() or not p.can_be_married():
            raise Exception("Can't be married")
        self.is_married_to = p.get_id()
        p.is_married_to = self.get_id()
        if self.get_genre() == "Female" and p.get_genre() == "Male":
            self.last_name = p.last_name
        else:
            if self.get_genre() == "Male" and p.get_genre() == "Female":
                p.last_name = self.last_name
    def can_have_child(self):
        return False
    def has_child_with(self, p, id, first_name, date_of_birth, genre, eyes_color = ''):
        if p is None or p.kind != 'Adult' and p.kind !='Senior':
            raise Exception("p is not an Adult of Senior")
        if (not p.can_have_child()) or(not self.can_have_child()):
            raise Exception("Can't have baby")        
        if self.get_eyes_color() == 'Blue' and p.get_eyes_color() == 'Blue' :
            eyes_color = 'Blue'
        if self.get_eyes_color() == 'Green' and p.get_eyes_color() == 'Green' :
            eyes_color = 'Green'
        if self.get_eyes_color() == 'Blue' and p.get_eyes_color() == 'Green' :
            eyes_color = 'Blue'
        if p.get_eyes_color() == 'Brown' :
            eyes_color = 'Brown'
        if id not in p.children:
            p.children.append(id)
        if id not in self.children:
            self.children.append(id)        
        return Baby(id,first_name,date_of_birth,genre,eyes_color)

 
    '''link 2 persons by adding c.get_id() to self.children'''
    def adopt_child(self, c):
       if (not self.can_have_child()):
            raise Exception("Can't adopt child")
       self.children.append(c.get_id())

class Adult(Person):
    def can_run(self):
        return True
    def need_help(self):
        return False
    def is_young(self):
        return False
    def can_vote(self):
        return True
    def can_be_married(self):
        return True
    def is_married(self):
        if self.is_married_to != 0:
            return True
        else:
            return False
    def divorce(self, p):
        self.is_married_to = 0
        p.is_married_to = 0
    def just_married_with(self, p):
        if self.is_married_to != 0 or p.is_married_to != 0:
            raise Exception("Already married")
        if not self.can_be_married() or not p.can_be_married():
            raise Exception("Can't be married")
        self.is_married_to = p.get_id()
        p.is_married_to = self.get_id()
        if self.get_genre() == "Female" and p.get_genre() == "Male":
            self.last_name = p.last_name
        else:
            if self.get_genre() == "Male" and p.get_genre() == "Female":
                p.last_name = self.last_name
    def can_have_child(self):
        return True
    def has_child_with(self, p, id, first_name, date_of_birth, genre, eyes_color = ''):
        if p is None or p.__class__.__name__ != 'Adult' and p.__class__.__name__ !='Senior':
            raise Exception("p is not an Adult of Senior")
        if (not p.can_have_child()) or(not self.can_have_child()):
            raise Exception("Can't have baby")        
        if self.get_eyes_color() == 'Blue' and p.get_eyes_color() == 'Blue' :
            eyes_color = 'Blue'
        if self.get_eyes_color() == 'Green' and p.get_eyes_color() == 'Green' :
            eyes_color = 'Green'
        if self.get_eyes_color() == 'Blue' and p.get_eyes_color() == 'Green' :
            eyes_color = 'Blue'
        if p.get_eyes_color() == 'Brown' :
            eyes_color = 'Brown'

        if id not in p.children:
            p.children.append(id)
        if id not in self.children:
            self.children.append(id)        
        return Baby(id,first_name,date_of_birth,genre,eyes_color)

 
    '''link 2 persons by adding c.get_id() to self.children'''
    def adopt_child(self, c):
       if (not self.can_have_child()):
            raise Exception("Can't adopt child")
       self.children.append(c.get_id())    

class Senior(Person):
    def can_run(self):
        return False
    def need_help(self):
        return True
    def is_young(self):
        return False
    def can_vote(self):
        return True
    def can_be_married(self):
        return True
    def is_married(self):
        if self.is_married_to != 0:
            return True
        else:
            return False
    def divorce(self, p):
        self.is_married_to = 0
        p.is_married_to = 0
    def just_married_with(self, p):
        if self.is_married_to != 0 or p.is_married_to != 0:
            raise Exception("Already married")
        if not self.can_be_married() or not p.can_be_married():
            raise Exception("Can't be married")
        self.is_married_to = p.get_id()
        p.is_married_to = self.get_id()
        if self.get_genre() == "Female" and p.get_genre() == "Male":
            self.last_name = p.last_name
        else:
            if self.get_genre() == "Male" and p.get_genre() == "Female":
                p.last_name = self.last_name
    def can_have_child(self):
        return False
    def has_child_with(self, p, id, first_name, date_of_birth, genre, eyes_color = ''):
        if p is None or p.kind != 'Adult' and p.kind !='Senior':
            raise Exception("p is not an Adult of Senior")
        if not p.can_have_child() or not self.can_have_child():
            raise Exception("Can't have baby")        
        if self.get_eyes_color() == 'Blue' and p.get_eyes_color() == 'Blue' :
            eyes_color = 'Blue'
        if self.get_eyes_color() == 'Green' and p.get_eyes_color() == 'Green' :
            eyes_color = 'Green'
        if self.get_eyes_color() == 'Blue' and p.get_eyes_color() == 'Green' :
            eyes_color = 'Blue'
        if p.get_eyes_color() == 'Brown' :
            eyes_color = 'Brown'
        if id not in p.children:
            p.children.append(id)
        if id not in self.children:
            self.children.append(id)        
        return Baby(id,first_name,date_of_birth,genre,eyes_color)

 
    '''link 2 persons by adding c.get_id() to self.children'''
    def adopt_child(self, c):
       if (not self.can_have_child()):
            raise Exception("Can't adopt child")
       self.children.append(c.get_id())

'''takes list of Person and write to json file'''
def save_to_file(list, filename):
   for i in range(0, len(list)):
            list[i] = list[i].json()
   with open(filename, 'w') as outfile:
       json.dump(list, outfile)
   outfile.close()

def load_from_file(filename):
    if type(filename) is not str or not os.path.isfile(filename):
        raise Exception("filename is not valid or doesn't exist")
    with open(filename) as json_file:
        data = json.load(json_file)
    json_file.close()
    Person = []
    person_dict = {"Person": Person, "Senior": Senior, "Adult": Adult, "Teenager": Teenager, "Baby": Baby}
    for i in range(0, len(data)):
        a = data[i]
        p = person_dict[a['kind']](a['id'], str(a['first_name']), a['date_of_birth'], str(a['genre']), str(a['eyes_color']))
        Person.append(p)
    return Person
