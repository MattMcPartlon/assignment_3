#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import utils.datastructures.graph.Edge as Edge

class WeightedEdge(Edge.Edge):
    
    def __init__(self, u, v, weight, directed=False):
        super.__init__(u,v,directed=directed)
        self.weight = weight

    def get_weight(self):
        return self.weight

