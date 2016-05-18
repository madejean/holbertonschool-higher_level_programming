#!/usr/bin/python
'''describe a Circle class with radius, center and color as private attributes and with a public name'''
import math   
class Circle:

   def __init__(self, radius):
      self.__radius = radius
      
#setter/getter to update and retreive private attributes
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
                     
