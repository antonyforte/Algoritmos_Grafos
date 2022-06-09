from igraph import *
import numpy as np
from math import inf

g = Graph([(0,1),(0,5),(1,2),(1,5),(2,3),(2,6),(3,4),(4,6),(4,7),(5,6),(5,8),(6,7),(7,8)])
g.es()['weight'] = [4,5,7,3,5,6,3,2,4,7,5,6,8]

print(g.summary())

n = len(g.es())
n1 = len(g.vs())
T = Graph()
T.add_vertices(n1)
List = g.es()['weight']
Pos_g = [0,1,2,3,4,5,6,7,8,9,10,11,12]

for i in range(1,n):
    for j in range(i,0,-1):
        if(List[j-1] > List[j]):
            List[j-1],List[j] = List[j],List[j-1]
            Pos_g[j-1],Pos_g[j] = Pos_g[j],Pos_g[j-1]

print(List)
print(Pos_g)


reach = True
for i in Pos_g:
    cont = 0
    for e in g.es():
        if(cont == Pos_g[i]):
            reach = True
            for h in T.es():
                if(h.target == e.target):
                    reach = False
            if(reach == True):
                T.add_edge(e.source,e.target)
        cont = cont + 1


##You will need pycairo to run the layout
layout = T.layout("kk")
plot(T,layout = layout)