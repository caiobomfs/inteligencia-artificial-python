# -*- coding: utf-8 -*- 

import numpy as np 

  
def degrau(v): 

    if v >=0: 

        return 1 

    else: 

        return 0 

     
def perceptron(x, w, b): 

    v = np.dot(w, x) + b  

    y = degrau(v) 

    return y 


def OR(x): 

    w = np.array([1,1]) 

    b = -0.5 

    return perceptron(x, w, b) 

  
n0 = np.array([0,1]) 

n1 = np.array([1,1]) 

n2 = np.array([0,0]) 

n3 = np.array([1,0]) 

  

print("OR ({} + {}) = {}".format(0,1, OR(n0))) 

print("OR ({} + {}) = {}".format(1,1, OR(n1))) 

print("OR ({} + {}) = {}".format(0,0, OR(n2))) 

print("OR ({} + {}) = {}".format(1,0, OR(n3)))

 