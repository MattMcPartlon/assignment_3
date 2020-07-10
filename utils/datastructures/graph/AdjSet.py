#!/usr/bin/env python
# coding: utf-8

# In[3]:


from utils.datastructures.graph.AdjacencyListABC import AdjacencyListABC


class AdjSet(AdjacencyListABC) :

    def __init__(self) :
        super().__init__(set())

    def __contains__(self, u) :
        return u in self.adj

    def __len__(self) :
        return len(self.adj)

    def _add(self, u) :
        assert u.has_hash()
        return self.adj.add(u)

    def _remove(self, u) :
        """
        removes u from the adjacency list
        raises assertion error if u is not a member of this list
        """
        assert u.has_hash()
        return self.adj.remove(u)

    def get_adjacencies(self) :
        """
        should return an enumerable object containing all objects in adjacency list
        """
        return self.adj

# In[ ]:


# In[ ]:




