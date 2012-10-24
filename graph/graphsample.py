class Node:
    def __init__(self):
        self.id = str('');
        self.neighbours = []

class Edge:
    def __init__(self, neighbor):
        self.neighbor = neighbor

class AdjacencyList:
    def __init__(self):
        self.innerlist = []

    def getneighbor(index):
        return innerlist[index]

    def setneighbor(index, value):
        innerlist[index] = value

class NodeList:
    def __init__(self):
        self.data = []

def find_path(graph, start, end, path=[]):
    path = path + [start]
    print path
    if start == end:
        return path

    if not graph.has_key(start):
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return None


def main():
    graph = {'80 Feet Road' : ['100 Feet Road','CMH Road'],
    'CMH Road' : ['Halasaru','D'],
    'Halasaru' : ['Trinity'],
    '100 Feet Road' : ['CMH Road','Domlur'],
    'Domlur' : ['Victoria Road'],
    'Victoria Road' : ['Trinity'],
    'Trinity' : ['MG Road']}
    path = []

    #data = find_path(graph,'80 Feet Road','MG Road',path)

    data = find_all_paths(graph,'80 Feet Road','MG Road',path)
    for route in data:
        print route
    #print data

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_key(start):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

if __name__ == '__main__':
    main()
