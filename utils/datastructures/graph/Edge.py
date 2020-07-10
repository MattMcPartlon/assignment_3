from utils.datastructures.graph.Vertex import Vertex

class Edge:
    def __init__(self, u, v, data, directed=False):
        assert isinstance(u, Vertex) and isinstance(v, Vertex)
        self.u, self.v = u, v
        self.directed = directed
    
    def get_endpoints(self):
        return (self.u, self.v)
    
    def is_directed(self):
        return self.directed
    
    def get_data(self):
        return self.data
    
    def __str__(self):
        return str(self.u)+' , '+str(self.v)

