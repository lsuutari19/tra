# Python code to perform Dijkstra's algorithm
# in a non-directed graph
import math, time
from collections import deque

INF = float("inf")

class WeightedEdgeNode:
	def __init__(self,nde,wght=0):
		self.node = nde
		self.weight = wght


class WeightedGraph:

	def __init__(self,nVerts):
		self.nVertices = nVerts
		self.adj_list = {}
		self.vertices = []

		for x in range(1,nVerts+1):
			self.adj_list[x] = []
			self.vertices.append(x)

		self.dist = {}
		for x in range(1,nVerts+1):
			self.dist[x] = INF

		self.pred = {}
		for x in range(1,nVerts+1):
			self.pred[x] = None


def add_edge(g,x,y,wght):	
	g.adj_list[x].append(WeightedEdgeNode(y,wght))
	g.adj_list[y].append(WeightedEdgeNode(x,wght))	


def dijkstra(g,s):

    for i in g.vertices:
        g.dist[i] = INF
        g.pred[i] = 0

    g.dist[s] = 0

    queue = [i for i in g.vertices]

    while len(queue) > 0:
        minval = INF
        u = 0
        for vert in queue:
            if g.dist[vert] < minval:
                minval = g.dist[vert]
                u = vert
        queue.remove(u)                            

        for edge in g.adj_list[u]:
            v = edge.node
            maks = max(g.dist[u], edge.weight)    
            if g.dist[v] > maks:        # Verrataan nykyistä maksimikorkeutta ja kaupungista seuraavaan lähteviä korkeuksia
                g.dist[v] = maks        # Jos löytyy suurempi korkeus, niin korvataan aikaisempi.
                g.pred[v] = u           
                


def print_path(g,u):
    if g.pred[u] != 0:
        print_path(g,g.pred[u])
    print(u,":",g.dist[u])


def main():

    source = input("Input file name: ")
    with open(source, "r") as data:

        start_time = time.time()

        listData = data.readlines()

        x = [i.strip("\n") for i in listData]
        y = [i.split(" ") for i in x]

        cities, end = y[0][0], y[-1][0]    
        y.pop(0)
        y.pop(-1)

        gCities = str(cities)
        gCities = cities.strip("[]")        # Poistetaan turhat merkit jatko tutkimusta varten
        gCities = cities.strip(" ' ")
        gCities = int(gCities)              # Muutetaan integeriksi, jotta kyetään luomaan WeightedGraph
        g = WeightedGraph(gCities)

        h = len(y)

        for i in range(h):
            add_edge(g, int(y[i][0]), int(y[i][1]), int(y[i][2]))

        dijkstra(g,1)
        print("Path from 1 to {}  with cumulative weights:".format(cities))
        print_path(g,int(end))
        print(round(time.time() - start_time, 5))


main()

'''

1/24/2021:
-Aloitin työn alusta esimerkkiohjelmien avulla!
2/24/2021:
-poistelin välilyöntejä koodista ongelmaa kuitenkin
ulommissa indentaatioissa?

'''