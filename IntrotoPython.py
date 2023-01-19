# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 14:33:36 2022

@author: DELL
"""

print('hello world')
print(2)

#this is how we write comments on python
# vsdvkdkdvsvdjskvsdjkv

# this is how we write comments on python
# this is another comment

x=25
y='Hi, my name is wasim'


x = 12

y = 50

lists = ['apple','banana','pear','pear']

# append to a list
lists.append('cherry')

# insert item into a specific position
lists.insert(1, 'grape')

# remove items in a list
lists.remove('pear')

# remove the last item in a list
lists.pop()

# working with dictionaries

mydict = {
    'name':'Wasim',
    'location':'India',
    'favcolor':'Blue',
    'luckynumber': 15
    }

# access other keys
color = mydict['favcolor']
print(color)

# to get a list of keys
print(mydict.keys())

# to get a list of values
print(mydict.values())

# to get a list of items
print(mydict.items())

# to add a new key/ variable
mydict['gender'] = 'female'
print(mydict)

# Working with arrays

import numpy as np

# 1D array
arr = np.array([1, 2, 3, 4])

# 0D array
arr = np.array(43)

# 2D array

arr = np.array([[1,2,3], [4,5,6]])



# Playing around with classes

class Car:
    type = 'Automobile' #class attributes
    def __init__(self, name, make, color):
        self.carname = name    #instance attributes
        self.carmake = make    #instance attributes
        self.carcolor = color  #instance attributes
        
mycar = Car('gclass','mercedes','black')

# for attributes in a class

carname = mycar.carname
carmake = mycar.carmake
carcolor = mycar.carcolor



    


























