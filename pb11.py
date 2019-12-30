#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 17:45:43 2019
Using x*e^-x as p(x)
@author: chintan
"""
import statistics
import randomvariate as fn
import numpy as np
from matplotlib import pyplot as plt
N=1000
a=0
b=10
def p(x):
    return(x*np.exp(-x))
    
def f(x):
    return((27/(2*(np.pi)**2)*((1-np.exp(-x))/(1+np.exp(-3*x)))*x*np.exp(-x)))
I=[]    
for i in range(1000):
    r=fn.randomvariate(p,N,a,b)
    fun=f(r)
    I.append(sum(fun/p(r))/N)
bins=np.linspace(.8,1.3,100)    
plt.hist(I,bins)  
plt.show()
print('Mean:',statistics.mean(I))
print('Variance:',statistics.variance(I)) 
