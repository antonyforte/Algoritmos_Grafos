from igraph import *
import numpy as np
from math import inf


g = Graph([(0,1),(0,2),(1,3),(2,4),(3,4),(3,5),(4,6),(5,7),(6,7),(7,8),(7,9),(8,9),(9,10)],directed = True)
g.es()['weight'] = [7,5,9,6,0,11,4,3,8,4,6,0,7]


print(g.summary())

n = len(g.vs())
f = []
critic = []
Rotulotc = []
Rotulott = []
Temp = []
for i in range(0,11):
    Temp.append(0)
    f.append(0)
    critic.append(0)
    Rotulotc.append(0)
    Rotulott.append(math.inf)

for e in g.es():
    if Rotulotc[e.target] < Rotulotc[e.source] + e['weight']:
        Rotulotc[e.target] = Rotulotc[e.source] + e['weight']


print(Rotulotc)

Rotulott[n-1] = Rotulotc[n-1]
print(Rotulott)

i=n-2
while (i >= 0):
    j=n-1
    while (j >= 0):
        if(g.are_connected(i,j) == True):
            if(Rotulott[i] > Rotulott[j] - g.es[g.get_eid(i,j)]['weight'] or Rotulott[i] == math.inf):
                Rotulott[i] = Rotulott[j] - g.es[g.get_eid(i,j)]['weight']
        j= j-1
    i= i-1

i=0
for i in range(0,11):
    f[i] = Rotulott[i] - Rotulotc[i]
    if Rotulott[i] == Rotulotc[i]:
        critic[i] = 1
    else:
        critic[i] = 0

#No vetor de caminho crítico, 1 significa se o vertice faz parte do caminho critico
print(Rotulotc)
print(Rotulott)
print(f)
print(critic)