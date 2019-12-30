#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 19:22:07 2019

@author: chintan
"""
import statistics
import numpy as np
import randomvariate as fn
from numpy import random
from matplotlib import pyplot as plt
#1) Uniform distribution
N=1000
a=0
b=10
def f(x):
    return((27/(2*(np.pi)**2)*((1-np.exp(-x))/(1+np.exp(-3*x)))*x*np.exp(-x)))
I1=[]    
for i in range(1000):
    r=random.uniform(a,b,N)
    fun=f(r)
    I1.append(sum(fun)*(b-a)/N)
#2) p(x)=x e^-x:
def p(x):
    return(x*np.exp(-x))
I2=[]    
for i in range(1000):
    r=fn.randomvariate(p,N,a,b)
    fun=f(r)
    I2.append(sum(fun/p(r))/N)
bins=np.linspace(.8,1.3,100)
plt.hist(I1,bins,label='Uniform')
plt.hist(I2,bins,label='x e^-x')
plt.legend()
plt.show()       