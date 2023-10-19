# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 15:47:53 2023

@author: Gabriel
"""

def S10_7() :
    import numpy as np
    import matplotlib.pyplot as plt
    x=np.linspace(0,3,100)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    y=np.exp(-x)
    plt.plot(x,y,label="exp(-x)")
    y2=np.sin(3*np.pi*x)*np.exp(-x)
    plt.plot(x,y2,label="sin(3pix)")
    plt.legend()
    plt.show()

S10_7()

def S10_6():
    import numpy as np
    import matplotlib.pyplot as plt
    import math as m
    numberdots=int(input("Enter the number of dots to draw"))
    startvalue=int(input("Enter the start value"))
    endvalue=int(input("Enter the end value"))
    x=np.linspace(startvalue,endvalue,numberdots)
    s=float(input("Enter the width (s)"))
    x0=int(input("Enter the center of the gaussian (x0)"))
    y = 1 / (s * np.sqrt(2 * np.pi)) * np.exp((-1/2) * ((x - x0) ** 2) / s ** 2)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.plot(x,y,label="Gaussienne")
    plt.legend()
    plt.show()
    
    
S10_6()


def S10_10():
    import numpy as np
    import matplotlib.pyplot as plt
    import math as m
    nbcourbe=int(input("How many fonctions ? : "))
    for i in range (nbcourbe):
        numberdots=int(input("Enter the number of dots to draw"))
        startvalue=int(input("Enter the start value"))
        endvalue=int(input("Enter the end value"))
        x=np.linspace(startvalue,endvalue,numberdots)
        s=float(input("Enter the width (s)"))
        x0=int(input("Enter the center of the gaussian (x0)"))
        y = 1 / (s * np.sqrt(2 * np.pi)) * np.exp((-1/2) * ((x - x0) ** 2) / s ** 2)
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.plot(x,y,label="Gaussienne "+str(i)+": x0="+str(x0)+", s="+str(s))
    
    plt.legend()
    plt.show()
    
    


S10_10()














