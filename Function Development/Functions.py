# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 12:07:45 2019

@author: Wian
"""
import control
import math
import numpy
import matplotlib.pyplot as plt

def Pade(deadtime, order):
    """
    Provides and nth order Pade approximation in the form of a control.tf
    object, to implement dead time.
    """
    
    Const_list_num = []
    Const_list_den = []
    for k in range(order, -1, -1):
        Pade_const_num = (-deadtime/2)**k/math.factorial(k)
        Pade_const_den = (deadtime/2)**k/math.factorial(k)
        Const_list_num.append(Pade_const_num)
        Const_list_den.append(Pade_const_den)
    return control.tf(Const_list_num, Const_list_den)
    
def Deadtime(G, deadtime = 1, order = 2):
    """
    Adds dead time to a control.tf transfer function.
    """
    
    G_deadtime = Pade(deadtime, order)
    return G*G_deadtime

t = numpy.linspace(0,7,1000)
G = control.tf(1, [1 , 1])
t, y = control.step_response(G , t)
td, yd = control.step_response(Deadtime(G, 10), t)

plt.plot(t, y)
plt.plot(td, yd)