"""
dato un insieme di 20 punti su un piano cartesiano
rasdom compresi tra 1 e 10 ,calcolare il punto con
ascissa massima e il punto con cordinata minima
"""
import random

x=[]
y=[]
for i in range(0,20):
    x.append(random.randint(0,10))
    y.append(random.randint(0,10))
"""
ascissa massima?
scorrere la lista delle x e y, trovare il massimo e salvare l'indice,
visualizzare poi con un print il numero
"""
x_massima=0
massimo1=x[0]
for i in range(0,10):
    if x[i]>massimo1:
        massimo1=x[i]
        x_massima=i

y_massima=0
massimo2=y[0]
for i in range(0,10):
    if y[i]>massimo2:
        massimo2=y[i]
        y_massima=i
print("max","x=",massimo1, "y=",massimo2)

"""
ascissa minima?
scorrere la lista delle x e y,trovare il minimo e salvare l'indice,
visualizzare poi con un print il numero
"""
x_minima=0
minima1=x[0]
for i in range(0,10):
    if x[i]<minima1:
        minima1=x[i]
        x_minima=i
        y_minima=0
        
minima2=y[0]
for i in range (0,10):
    if y[i]<minima2:
        minima2=y[i]
        y_minima=i
print("min","x=",minima1,"y=",minima2)