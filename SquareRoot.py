# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 19:47:53 2019

@author: Justin
"""
import math

def sqroot():
    root = int(input('Root number (squared, cubed: 2, 3) >> '))
    num = int(input('Base root (√9, √25) >> '))
    
    num1 = str(num)
    if root == 2:
        print('√' +  num1, '↓')
        result = math.sqrt(num)
        resulta = round(result)
        print(str(resulta))
    else:
        print(root, '√' + num1, '↓')
        result2 = num **(1/root)
        resulta1 = round(result2)
        print(str(resulta1))
        
sqroot()        

a = str(input('Continue? [{Y}] or [{N]}  '))
if a == 'Y' or 'y':
    sqroot()
if a == 'N' or 'n':
    exit()
    