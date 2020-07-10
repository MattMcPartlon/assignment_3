import numpy as np
from utils.datastructures.graph.SimpleGraph import SimpleGraph
from utils.datastructures.graph.WeightedVertex import WeightedVertex
from utils.datastructures.graph.WeightedEdge import WeightedEdge
from utils.datastructures.graph.Edge import Edge
from utils.datastructures.graph.Vertex import Vertex



def gen_edge_weighted_graph(n: int, p=0.5, mn=0, mx=1, directed=False) -> SimpleGraph:
    """
    Generates an edge weighted graph with edge probability p
    and min/max weight uniformly distributed between mn and mx
    :param n: number of vertices
    :param p: edge probability
    :param mn: min edge weight
    :param mx: max edge weight
    :return: SimpleGraph with weighed edges on n vertices w/ edge prob. p
    """
    adj = _gen_adjs(n, p, mn, mx, directed, weighted=True)
    G = SimpleGraph()

    #Add vertices to graph
    vertices = [Vertex(idx = i) for i in range(n)]
    for i in range(n):
        G.add_vertex(vertices[i])

    for i in range(n) :
        start = i+1
        if directed :
            start = 0
        for j in range(start,n) :
            if adj[i, j] > 0 :
                u, v = vertices[i], vertices[j]
                w = adj[i, j]
                e = WeightedEdge(u, v, w, directed)
                G.add_edge(e)

    return G

def gen_vtx_weighted_graph(n: int, p=0.5, mn=0, mx=1, directed=False) -> SimpleGraph:
    """
    Generates a vertex weighted graph  on n vertices with edge probability p,
    and min/max weight distributed UAR between mn and mx.
    :param n: number of vertices
    :param p: edge probability
    :param mn: min vtx weight
    :param mx: max vtx weight
    :return: SimpleGraph on n vertices w/ edge prob. p, and weighted vertices
    """
    adj = _gen_adjs(n, p, directed=directed, weighted=False)
    G = SimpleGraph()
    wts = np.random.uniform(mn,mx,n)
    # Add vertices to graph
    vertices = [WeightedVertex(wts[i],i) for i in range(n)]
    for i in range(n):
        G.add_vertex(vertices[i])

    for i in range(n) :
        start = i+1
        if directed :
            start = 0
        for j in range(start, n) :
            if adj[i, j] > 0 :
                u, v = vertices[i], vertices[j]
                e = Edge(u, v, directed)
                G.add_edge(e)

    return G

def gen_knapsack_instance(n, capacity = 10, min_wt=0, max_wt=1,
                      min_val=0, max_val=1):
    """
    Generates a knapsack instance with n items, having values
    distributed UAR from min_val to max_val, and weights distributed
    UAR from min_wt to max_wt
    """
    vs = np.random.uniform(min_val, max_val, n)
    ws = np.random.uniform(min_wt, max_wt, n)
    return (capacity, vs, ws)


def _gen_adjs(n: int, p=0.5, mn=0, mx=1, directed=False, weighted =False):
    """
    method used for generating base graph - can be ignored.
    """
    adj = np.random.uniform(mn,mx,(n,n))
    edge_msk = np.random.uniform(0,1,(n,n))>p
    if not directed:
        adj = np.tril(adj)
        assert adj.shape == (n,n)
        adj += adj.T
        edge_msk = np.tril(edge_msk)
        edge_msk += edge_msk.T
        rows, cols = np.indices((n, n))
        rvs, cvs = np.diag(rows), np.diag(cols)
        edge_msk[rvs,cvs], adj[rvs,cvs] = 0,0
    adj[edge_msk]=0
    if not weighted:
        adj[adj>0]=1
    assert np.allclose(np.linalg.norm(np.diag(adj)),0)
    return adj