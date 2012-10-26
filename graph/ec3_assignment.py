# Possible color values for each nodes
class Color:
    Black, Violet, Indigo, Blue, Green, Yellow, Orange, Red = range(8)

# Adjancecy represents the neighbors associated 
# with the a specific node. the data maintained an inner list
# the list holds the several edge classes which is a representation of edges associated 
# with each of the vertices
class AdjacencyList:
    def __init__(self):
        self.innerlist = []

    def get_neighbor(self,index):
        return self.innerlist[index]

    def set_neighbor(self, index, value):
        self.innerlist[index] = value

    def add_neighbor(self, edge):
        self.innerlist.append(edge)

class Vertex:
    def __init__(self, ID = str(), neighbors = AdjacencyList(), color = Color()):
        self.id = ID;
        if neighbors == None:
            self.neighbors = AdjacencyList()
        else:            
            self.neighbors = neighbors
        self.color = color

# represents the edge for a vertex. it contains the 
# edge to which it is connected 
class Edge:
    def __init__(self, neighbor = Vertex()):
        self.neighbor = neighbor

# graph contains the nodes which is a dictionary
# the dictionary's key is the vertex's id and the 
# node information is represented as the value
class Graph:
    def __init__(self):
        self.nodes = {}

    def add(self,node = Vertex()):
        self.nodes[node.id] = node

    def remove(self,node):
        self.nodes.remove(node);

    def contains_key(self,key):
        return self.nodes.has_key(key)

    def clear(self):
        self.nodes.clear()

    def getVertex(self,key):
        return self.nodes.get(key)

# creates an an empty graph object. (ADT) 
def createGraph():
    return Graph()

# adds two nodes the list and connects between the given two vertices
# the connection is from v1 -> v2
def addEdge(g = Graph(), v1 = Vertex(), v2 = Vertex()):
    v1.neighbors.add_neighbor(Edge(v2))

    if not g.contains_key(v1.id):
        g.add(v1)
    if not g.contains_key(v2.id):
        g.add(v2)

    return g

# get the list of the neighbors to the given graph and node
def getNeighbors(g = Graph()):
    return g

# sorts the given graph based on the degree of the vertices
def sortGraphbyDegree(g = Graph()):
    return g;

# returns the color chosen for the given vertex in the graph
def chooseColor(g = Graph(), v= Vertex()):
    return Color.Black

# assign colors will automatically colors and 
# find the suitable color for the given vertex
def assignColors(g = Graph(), v = Vertex()):
    return 0

def printGraph(g = Graph()):
    for n in g.nodes:
        print 

def main():

    g = createGraph()

    g = addEdge(g, Vertex("80 Feet Road", None, Color.Black), Vertex("100 Feet Road", None, Color.Black))
    g = addEdge(g, Vertex("100 Feet Road", None, Color.Black), Vertex("Domlur", None, Color.Black))
    g = addEdge(g, Vertex("Domlur", None, Color.Black), Vertex("Victoria Road", None, Color.Black))
    g = addEdge(g, Vertex("Victoria Road", None, Color.Black), Vertex("Trinity", None, Color.Black))
    g = addEdge(g, Vertex("Trinity", None, Color.Black), Vertex("MG Road", None, Color.Black))
    g = addEdge(g, Vertex("80 Feet Road", None, Color.Black), Vertex("CMH Road", None, Color.Black))
    g = addEdge(g, Vertex("100 Feet Road", None, Color.Black), Vertex("CMH Road", None, Color.Black))
    g = addEdge(g, Vertex("CMH Road", None, Color.Black), Vertex("Halasaru", None, Color.Black))
    g = addEdge(g, Vertex("Halasaru", None, Color.Black), Vertex("Trinity", None, Color.Black))

    printGraph(g);

if __name__ == '__main__':
    main()

#
#   graph = {'80 Feet Road' : ['100 Feet Road','CMH Road'],
#  'CMH Road' : ['Halasaru','D'],
# 'Halasaru' : ['Trinity'],
#'100 Feet Road' : ['CMH Road','Domlur'],
#   'Domlur' : ['Victoria Road'],
#   'Victoria Road' : ['Trinity'],
#  'Trinity' : ['MG Road']}
# path = []

#data = find_path(graph,'80 Feet Road','MG Road',path)

# data = find_all_paths(graph,'80 Feet Road','MG Road',path)
#for route in data:
#    print route
#print data
