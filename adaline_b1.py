# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 14:09:39 2021

@author: rodri
"""

from __future__ import division
from collections import Counter
from functools import partial
from linear_algebra import dot
import matplotlib 
import matplotlib.pyplot as plt
import numpy as np 
import math
from numpy import random


def saida_adaline(pesos, entradas):
    y = dot(pesos, entradas)
    return y

def linear(sinapses):
    pesos_sinapses = sinapses
    taxa_aprendizagem = 0.1 
    termo_proporcionalidade = 1
    #funcoes combinacao linear
    seno = [i for i in range(45)]
    coseno = [i for i in range(45)]
    coeficiente = [i for i in range(45)]
    entradas = [i for i in range(45)]
    saida_parcial = [i for i in range(45)]
    
    for x in range(45):
        f[x] = -math.pi + 0.565 * math.sin(math.pi/180 * x) + 2.657 * math.cos( math.pi/180 * x ) + 0.674 * math.pi/180 * x
        seno[x] = math.sin(math.pi/180*x)
        coseno[x] = math.cos(math.pi/180*x)
        coeficiente[x] = math.pi/180*x
        entradas[x] = [termo_proporcionalidade, seno[x], coseno[x], coeficiente[x]]
        saida_parcial[x] = saida_adaline(pesos_sinapses, entradas[x])
        pesos_sinapses[0] = pesos_sinapses[0] + taxa_aprendizagem * ( (f[x] - saida_parcial[x]) * (f[x] - saida_parcial[x])) *0.5 * termo_proporcionalidade
        pesos_sinapses[1] = pesos_sinapses[1] + taxa_aprendizagem * ( (f[x] - saida_parcial[x]) * (f[x] - saida_parcial[x])) *0.5 * math.sin(math.pi/180 * x)
        pesos_sinapses[2] = pesos_sinapses[2] + taxa_aprendizagem * ( (f[x] - saida_parcial[x]) * (f[x] - saida_parcial[x])) *0.5 * math.cos(math.pi/180 * x)
        pesos_sinapses[3] = pesos_sinapses[3] + taxa_aprendizagem * ( (f[x] - saida_parcial[x]) * (f[x] - saida_parcial[x])) *0.5 * math.pi/180 * x
        
        return pesos_sinapses, saida_parcial
    
def teste_generalizacao(sinapses):
    pesos_sinapses = sinapses
    
    termo_proporcionalidade = 1
    #funcoes combinacao linear
    seno = [i for i in range(359)]
    coseno = [i for i in range(359)]
    coeficiente = [i for i in range(359)]
    entradas = [i for i in range(359)]
    saida_parcial = [i for i in range(359)]
    
    for x in range(359):
        f[x] = -math.pi + 0.565 * math.sin(math.pi/180 * x) + 2.657 * math.cos( math.pi/180 * x ) + 0.674 * math.pi/180 * x
        seno[x] = (math.sin(x*math.pi/180))
        coseno[x] = (math.sin(x*math.pi/180))
        coeficiente[x] = (x*math.pi/180) * random.rand()
        entradas[x] = [termo_proporcionalidade, seno[x], coseno[x], coeficiente[x]]
        saida_parcial[x] = saida_adaline(pesos_sinapses, entradas[x])
     
    saida = saida_parcial
    return sinapses, saida    

#funcoes da combinacao linear
t = np.arange(0, 359, 1)
seno_0 = 0 + np.sin(np.pi/180 * t)
coseno_0 = 0 + np.cos(np.pi/180*t)
coeficiente_0 = np.pi/180 * t
f = -np.pi + 0.565*seno_0 + 2.657*coseno_0 + 0.674*coeficiente_0   

neuronio = [-2.4013, 0.393, 1.902, 0.429]

#20 ciclos de treinamento

for _ in range(20):
    neuronio, funcao_saida = linear(neuronio)
    print(neuronio)
    
fig,ax =plt.subplots()
ax.plot(t, seno_0)
ax.plot(t, coseno_0)
ax.plot(t, coeficiente_0)
ax.plot(t, f)

ax.plot([0, 50, 100, 150, 200, 250, 300, 350] ,[4, 4, 4, 4 , 4 ,4,4,4] ,color = 'black', marker = '*', linestyle= '--')
ax.plot([0, 50, 100, 150, 200, 250, 300, 350] ,[-4, -4, -4, -4 , -4 , -4, -4, -4], color = 'black', marker = '*', linestyle= '--')

ax.set(xlabel='angulo(??)', ylabel='funcoes', title="neuronio Adaline")
ax.grid()

fig.savefig('adaline.png')

neuronio, funcao = teste_generalizacao(neuronio)
ax.plot(t, funcao)
plt.show()



    



