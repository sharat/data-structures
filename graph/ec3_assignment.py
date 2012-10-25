class Color:
    Black, Violet, Indigo, Blue, Green, Yellow, Orange, Red = range(8)

class AdjacencyList:
    def __init__(self):
        self.innerlist = []

    def get_neighbor(index):
        return innerlist[index]

    def set_neighbor(index, value):
        innerlist[index] = value

    def add_neighbor(edge):
        innerlist.append(edge)

class Vertex:
    def __init__(self):
        self.id = str('');
        self.neighbours = AdjacencyList()
        self.color = Color()

    def __init__(self, id = str(), neighbours = AdjacencyList(), color = Color()):
        self.id = id;
        self.neighbours = neighbours
        self.color = color

class Edge:
    def __init__(self, neighbor = Vertex()):
        self.neighbor = neighbor

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


def createGraph():
    return Graph()

def addEdge(g = Graph(), v1 = Vertex(), v2 = Vertex()):
    v1.neighbours.add_neighbor(Edge(v2))

    if not g.contains_key(v1.id):
        g.add(v1)
    if not g.contains_key(v2.id):
        g.add(v2)

    return g

def getNeighbors(g = Graph()):
    return g

def sortGraphbyDegree(g = Graph()):
    return g;

def chooseColor(g = Graph(), v= Vertex()):
    return Color.Black

def assignColors(g = Graph(), v = Vertex()):
    return 0

def printGraph(g = Graph()):
    print g.nodes

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
