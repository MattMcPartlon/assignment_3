#!/usr/bin/env python
# coding: utf-8

# In[3]:


from utils.datastructures.graph.AdjacencyListABC import AdjacencyListABC

class AdjMatrix(AdjacencyListABC) :

    def __init__(self, n) :
        super().__init__([None]*n)
        self.size = 0

    def __contains__(self, u) :
        assert u.has_index()
        return self.adj[u.get_index()] == 1

    def __len__(self) :
        return self.size

    def _add(self, u) :
        self.adj[u.get_index()]=1
        self.size+=1


    def _remove(self, u) :
        """
        removes u from the adjacency list
        raises assertion error if u is not a member of this list
        """
        assert u.has_index()
        self.adj[u.get_index()]=None
        self.size-=1

    def get_adjacencies(self) :
        """
        should return an enumerable object containing all objects in adjacency list
        """
        return [u for u in self.adj if u is not None]





