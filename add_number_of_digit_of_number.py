# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 07:48:33 2022

@author: EVOL
"""

n = int(input())

dig = 0

while n >0:
    
    rev = n%10
    
    dig += rev
    
    n = n//10
    
print(dig)

