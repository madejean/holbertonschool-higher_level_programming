#!/usr/bin/python

'''describe a Circle class with radius, center and color as private attributes and with a public name'''
import math   
class Circle:
    
    '''Constructor'''
    def __init__(self, radius):
      self.__radius = radius
      self.__center = [0,0]
      self.__color = ""
      self.name = ""

    '''Destructor'''
    def __del__(self):
        pass  

    '''setter/getter to update and retreive private attributes'''
    def get_color(self):
       return self.__color

    def set_color(self, color):
        self.__color = color   
         
    def get_center(self):
      return self.__center
    
    def set_center(self, center):
        self.__center = center
              
    def area(self):
        return math.pi * ((self.__radius ** 2))
                     
