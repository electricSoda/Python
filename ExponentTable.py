# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 19:33:57 2019

@author: Justin
"""

max_exponent = int(input('What do you want the max exponent to be? >> '))
max_base = int(input('What do you want the max base to be? >> '))

for i in range(0, max_base+1):
    for x in range(0, max_exponent+1):
        print(str(i**x))