from utils.datastructures.graph.Vertex import Vertex
"""
Weighted vertex
"""
class WeightedVertex(Vertex):

    def __init__(self, weight: float, idx: int):
        super().__init__(data = (weight, idx))
        self.weight = weight
        self.idx = idx

    def get_weight(self):
        return self.weight

    def get_idx(self):
        return self.idx

    def __hash__(self):
        return self.idx

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.idx == other.idx

    def has_hash(self):
        return True

    def __str__(self):
        return 'vtx : ('+str(self.idx)+', ' +str(self.weight)+')'




