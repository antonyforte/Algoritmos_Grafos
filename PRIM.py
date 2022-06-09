from igraph import *
import numpy as np
from math import inf

g = Graph([(0,1),(0,5),(1,2),(1,5),(2,3),(2,6),(3,4),(4,6),(4,7),(5,6),(5,8),(6,7),(7,8)])
g.es()['weight'] = [4,5,7,3,5,6,3,2,4,7,5,6,8]

print(g.summary())

n = len(g.vs())
n1 = len(g.es())
T = Graph()
T.add_vertices(n)
T.es()['weight'] = []

print(T.summary())
Lista = []
next_source = 0
count = 0
for i in range(0,n):
    Lista.append(0)

i = 0
while (count < n):
    menor = math.inf
    for j in range(0, n):
        aux = True
        for e in T.es():
            if (e.source == j):
                aux = False

        if (g.are_connected(i, j) and not T.are_connected(i, j) and aux == True):
            if (g.es[g.get_eid(i, j)]['weight'] < menor):
                menor = g.es[g.get_eid(i, j)]['weight']
                next_source = j
        if (j == n - 1):
            Lista[count] = menor
            T.add_edges([(i, next_source)])
            i = next_source
    count = count + 1
T.es()['weight'] = Lista

print(len(T.es()))

T.delete_edges(T.es(len(T.es())-1))
print(T.es()['weight'])

layout = T.layout("kk")
plot(T,layout = layout)

for e in T.es():
    print(e['weight'], e.source,e.target)
