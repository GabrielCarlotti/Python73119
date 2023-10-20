# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 13:29:43 2023

@author: Gabriel
"""

#Numpy pb 2

import numpy as np
import math as m
import matplotlib.pyplot as plt

def exo1():
    a=np.arange(0,21)
    for i in range(9,16):
        a[i]=-a[i]
    print (a)
    
exo1()
    
def exo2():
    a=np.arange(15,56)
    txt=""
    for i in range (1,len(a)-1):
        txt=txt+", "+str(a[i])
    print (txt)
    
exo2()

def exo3():
    a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    for i in range (len(a)):
        for j in range (len(a[0])):
            print(a[i,j],end=" ")
        print("")

exo3()

def exo4():
    a=np.linspace(5, 50,10)
    print(a)

exo4()


def exo5():
    a=np.random.randint(0,10,5)
    print(a)
    return a

exo5()


def exo6(vector1, vector2):
    return np.multiply(vector1, vector2)

v1 = exo5()
v2 = exo5()

result = exo6(v1, v2)
print(result)

def exo7():
    def rand():
        a=np.random.randint(10,21,4)
        return a
    a=np.array([rand(),rand(),rand()])
    for i in range (len(a)):
        for j in range (len(a[0])):
            print(a[i,j],end=" ")
        print("")
    return a

exo7()

def exo8(matrix):
    print("nb rows : "+str(len(matrix)))
    print("nb columns : "+str(len(matrix[0])))

#test :
exo8(exo7())

def exo9():
    matrix = np.ones((4,4))
    matrix -= np.eye(4)

    print(matrix)
    
exo9()

def exo10(a1,a2):
    common=np.intersect1d(a1,a2)
    print(common)
    
exo10(exo5(),exo5())

def exo11(a1):
    a=np.unique(a1)
    print(a)
    
exo11(np.array([[10,10,20,20,30,30]]))
    
def exo12():
    def rand():
        b=np.random.randint(10,21,3)
        return b
    a=np.cross(rand(),rand())
    print (a)

exo12()

def exo13():
    cart=np.random.rand(10, 2)
    r=np.sqrt(cart[:, 0]**2+cart[:, 1]**2)
    th=np.arctan2(cart[:, 1],cart[:, 0])
    pol= np.column_stack((r,th))
    print("Cartesian:\n",cart)
    print("\nPolar:\n",pol)

exo13()

def exo14(a,scalar):
    diff=np.abs(a-scalar)
    index=np.argmin(diff)
    print (a[index])

exo14()                
                 
                 