# -*- coding: utf-8 -*-
"""Minimoausente.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nM2O3h9kQ5YNdJFCBYwfbZCC_ks4Ls5U
"""

#Mínimo ausente en lista
import random
lista = []
for i in range(0,5,1):
  lista.append(random.randint(0,6))
print(lista)

#Iniciode programa como tal
max = lista[0]
for i in range(0,len(lista),1):
  if(max<lista[i]):
    max = lista[i]

print("El mayor es: " + str(max))

for i in range(0,max,1):
  if(i not in lista):
    print("El elemento más pequeño faltante es: " + str(i))
    break;