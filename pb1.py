#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 13:54:28 2019

@author: chintan
"""

import numpy as np
from numpy import random
from matplotlib import pyplot as plt
N=1000
a=0
b=10
def f(x):
    return((27/(2*(np.pi)**2)*((1-np.exp(-x))/(1+np.exp(-3*x)))*x*np.exp(-x)))
I=[]    
for i in range(1000):
    r=random.uniform(a,b,N)
    fn=f(r)
    I.append(sum(fn)*(b-a)/N)
plt.hist(I)    
plt.show()
    
                 
