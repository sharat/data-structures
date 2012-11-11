
# Problem : Breadth first search
# Author : Sarath

class Queue:
    
    def __init__(self):
        self.holder = []
        
    def enqueue(self, v):
        self.holder.append(v)
    
    def dequeue(self):
        
        val = None
        
        try:
            val = self.holder[0]
            if len(self.holder) == 1:
                self.holder = []
            else:
                self.holder = self.holder[1:] #remove the first element
        except:
            pass
        
        return val
    
    def isempty(self):
        if len(self.holder) > 0:
            return False 
        else:
            return True

def BFS(graph, start, end, queue):
    
    temp_path = [start]
    queue.enqueue(temp_path)
    
    while queue.isempty() == False:
        print 'queue is not empty'
        t_path = queue.dequeue()
        last_node = t_path[len(t_path)-1]

        if last_node == end:
            print "Valid Path : ", t_path
            
        for link_node in graph[last_node]:
            if link_node not in t_path:
                new_path = []
                new_path = t_path + [link_node]
                queue.enqueue(new_path)
    
def testBFS():
    
    graph = {'A': ['B', 'C','E'],
             'B': ['A','C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F','D'],
             'F': ['C']}
    
    print graph
    path_queue = Queue()
    
    BFS(graph, 'A', 'D', path_queue)
    
    
def main():
    testBFS()
    


    
if __name__ == '__main__':
    main()
