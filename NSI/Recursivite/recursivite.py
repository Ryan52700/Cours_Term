# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 11:33:11 2022

@author: Elève
"""

from random import *

def exercice1(n):
    
    if n == 0:
        return 0
    
    else:
        return n + exercice1(n-1)
        
def exercice2(n):
    
    if n == 0:
        return None
    
    else:
        return exercice2(n-1) * n
    
def exercice4(x,y):
    
    if x == 0:
        return 0
    
    elif x % 2 == 0:
        return exercice4(x//2,y+y)
    
    elif x % 2 != 0:
        return exercice4(x//2, (y+y)) + y   

def exercice5(n):
    
    if n <= 1:
        return n
    
    else:
        return exercice5(n-1)+exercice5(n-2)
        
def exercice5bis(n):
    
    f0 = 0
    print("f0 = 0")
    f1 = 1
    print("f1 = 1")
    
    f = 0
    
    for i in range(2, n + 1):
        f = f0 + f1
        print("{} = {}".format(i, f))
        f0 = f1
        f1 = f
    return None

def exercice3(i,k):
    
    if i <= k:
        print(i)
        exercice3(i+1,k)
    
    else:
        return None
    
def exercice3bis(i,k):
    
    for i in range(i, k+1):
        print(i)
        
###################################################
        
def echange(lst,ind1,ind2):
    
    tmp = lst[ind2]
    lst[ind2] = lst[ind1]        
    lst[ind1] = tmp 
    
    return lst

def melange(lst,ind):
    
    ind_max = len(lst) - 1
    
    for i in range(len(lst)):
        
        print(lst)
        
        j = randint(0,ind_max)
        echange(lst,ind_max,j)
        
        ind_max -= 1
        
### Programme principal

lst = [0,1,2,3,4,5,6,7,8,9,10]

melange(lst,4)
print(lst)