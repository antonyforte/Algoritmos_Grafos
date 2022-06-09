from igraph import *
import numpy as np
from math import inf

g = Graph([(0,1),(0,4),(1,2),(1,3),(2,3),(2,4),(3,0),(4,0),(4,3)], directed = True)
g.es()['weight'] = [1,2,1,2,4,2,3,1,1]

print(g.summary())

n = len(g.vs())
D = []
Rotas = []
infinito = math.inf
for i in range(0, n):
    D.append(infinito)
    Rotas.append(0)
D[0] = 0
print(D)
print(Rotas)

flag = True
while flag == True:
    flag = False
    for e in g.es():
        if D[e.target] > D[e.source]+e['weight']:
            D[e.target] = D[e.source] + e['weight']
            Rotas[e.target] = e.source
            flag = True

### You will need Pycairo to run the graph layout
layout = g.layout("kk")
plot(g,layout = layout)


print("Distancia ", D)
print("Rota ", Rotas)