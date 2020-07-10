#!/usr/bin/env python
# coding: utf-8

# In[3]:


from abc import ABC, abstractmethod
import utils.datastructures.graph.Vertex as Vertex

class AdjacencyListABC(ABC):
    
    def __init__(self, adj):
        self.adj = adj

    @abstractmethod
    def __contains__(self, u):
        """
        returns true iff u is a member of this adjacency list
        allows for use of 'in' operator, e.g. (syntactically)
        'u in adj_list' will return True iff u is a member of this list
        """
        pass

    @abstractmethod
    def __len__(self):
        """
        returns the length of the list (e.g. number of vertices)
        """
        pass
        
    def add(self, u):
        """
        Adds u to the adjacency list
        raises exception if the list already contains u,
        or if u does not stem from the Vertex base class
        """
        assert isinstance(u, Vertex.Vertex)
        assert u not in self.adj
        self._add(u)

    @abstractmethod
    def _add(self, u):
        """
        Adds u to the adjacency list
        :param u: vertex to add
        :return: the vertex u
        """
        
        
    def remove(self, u):
        """
        removes u from the adjacency list
        raises assertion error if u is not a member of this list
        """
        assert self.contains(u)
        self._remove(u)


    @abstractmethod
    def _remove(self,u):
        """
        remove vertex u from adjacency list
        :param u:
        :return:
        """
        pass


    @abstractmethod
    def get_adjacencies(self):
        """
        should return an enumerable object containing all objects in adjacency list
        """
        pass
    
        


# In[ ]:





# In[ ]:




