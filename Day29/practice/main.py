from lib2to3.pytree import Base
from random import randint
from re import S
from tkinter import Y

# random.seed(10)

# for i in range(0,60):
#     print(random())
#     print(random() + "**")
######################################################################################

# from platform import (
#     version,
#     platform,
#     processor,
#     system,
#     machine,
#     python_implementation,
#     python_version_tuple,
# )

# print(platform() + "-----> platform")
# print(processor() + "-----> processor")
# print(system() + "-----> system")
# print(machine() + "-----> machine")
# print(version() + "-----> version")
# print(python_implementation() + "-----> Python Implementation")
# for atr in python_version_tuple():
#     print(atr + "-----> tuple")

# print(__name__ + "-----> file name")

# array_1 = [1, 1, 1, 3, 6, 96, 5]
# filter(lambda a: a != 2, array_1)
# print(array_1)

######################################################################################
# Caesar's Cipher 2.0


# def cipher_fun():
#     cipher = ""

#     phrase = input("Please enter phrase to be encoded: ")

#     try:
#         for char in phrase:
#             cipher += chr(ord(char) + randint(1, 26))

#         print(cipher)
#     except:
#         print("You have entered non-alphabet character, try again")
#         cipher_fun()
######################################################################################

# Sudoku Row Checker


# def sudoku_checker(w):

#     for row in w:
#         row = str(row)
#         for value in row:
#             if row.count(value) == 1:
#                 continue
#             else:
#                 print("Invalid Game!")
#                 return

#     print("Game Valid!")


# sudoku_checker(
#     [
#         195743862,
#         431866927,
#         876192543,
#         387459216,
#         612387495,
#         549216738,
#         763524189,
#         928671354,
#         254938671,
#     ]
# )

######################################################################################

# class Car:
#     def __init__(self):
#         self.__wheels = 4
#         self.__windshield = 1
#         self.__windows = 5

#     def getwheels(self):
#         return self.__wheels

#     def getwindshield(self):
#         return self.__windshield

#     def getwindows(self):
#         return self.__windows


# class SUV(Car):
#     def __init__(self):
#         super().__init__()
#         self.__towpackage = 1

# suv1 = SUV()

# print(issubclass(suv1,Car()))

######################################################################################
# import math


# class Point:
#     def __init__(self, x=0.0, y=0.0):
#         self.__x = x
#         self.__y = y

#     def getx(self):
#         return self.__x

#     def gety(self):
#         return self.__y

#     def distance_from_xy(self, x, y):
#         return math.dist([self.__x, self.__y],[x,y])

#     def distance_from_point(self, point):
#         return math.dist([self.__x, self.__y],[point.getx(),point.gety()])


# point1 = Point(0, 0)
# point2 = Point(1, 1)
# print(point1.distance_from_point(point2))
# print(point2.distance_from_xy(2, 0))

# print(point1.__str__)
######################################################################################

# class Ex(Exception):
#     def __init__(self, msg):
#         Exception.__init__(self + msg)
#         self.args = (msg,)
        
# try:
#     raise Ex('ex')
# except Ex as e:
#     print(e)
# except Exception as e:
#     print(e)

######################################################################################

# class A:
#     X = 0
#     def __init__(self, v=0):
#         self.Y = v
#         A.X += v

# a = A()
# b = A(1)
# c = A(2)
# print(c.X)

######################################################################################

#Lambda
# double = lambda n:n*2
# larger = lambda a,b: a if a > b else b
# smaller = lambda a,b:a if a < b else b

# def expo_base(n):
#     return lambda a : a**n

# expo_3 = expo_base(3)
# expo_4 = expo_base(4)
# expo_5 = expo_base(5)


# items = ["Saif", "Samir","Mohammed","Asil","Inas"]
# items.sort(key = lambda a: len(a))

# print(double(10))
# print(larger(10,60))
# print(smaller(10,60))

# print(items)

# print(expo_3(10))
# print(expo_4(10))
# print(expo_5(10))

######################################################################################

# import os

# os.mkdir('thumbnails')
# os.chdir('thumbnails')

# sizes = ['small', 'medium', 'large']

# for size in sizes:
#     os.mkdir(size)

# print(os.listdir())
    
######################################################################################

# import random

# a=random.randint(0,100)
# b=random.randrange(10,100,3)
# c=random.choice((0,100,3))

# print(a,b,c)

######################################################################################

# numbers = [0,2,7,9,10]
# foo = map(lambda num:num **2, numbers)
# print(list(foo))

######################################################################################

# lst = [[x for x in range(3)] for y in range(3)]

# for r in range(3):
#     for c in range(3):
#         if lst[r][c]% 2 != 0:
#             print('#')

######################################################################################

# x=1
# y=0
# x = x ^ y
# y = x ^ y
# x = x ^ y

# print(x,y)
######################################################################################
lst = [i for i in range(-1,-2)]
print(len(lst))