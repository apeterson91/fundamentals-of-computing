http://www.codeskulptor.org/#user40_3PzfHA526P_28.py

"""
Graph exercises
"""
EX_GRAPH0 = {0: set([1,2]), 1: set([]), 2:set([])}
EX_GRAPH1 = {0: set([1,4,5]), 1:set([2,6]), 2:set([3]), 
             3:set([0]), 4:set([1]), 5:set([2]), 6:set([])}
EX_GRAPH2 = {0:set([1,4,5]), 1:set([2,6]), 2:set([3,7]), 3:set([7]),
             4:set([1]), 5:set([2]), 6:set([]), 7:set([3]), 8:set([1,2]),
             9:set([0,3,4,5,6,7])}


def make_complete_graph(num_nodes):
    """
    returns a 'complete graph' such that
    each node is adjacent to every other node 
    in the graph (adjacency-list representation)
    """
    if num_nodes <= 0:
        return {}
    else:
        complete_graph = {}
        for node in range(num_nodes):
            complete_graph[node]=set([adjacent_node for adjacent_node in set(range(num_nodes)).difference(set([node]))])
    return complete_graph

def compute_in_degrees(digraph):
    """
    returns dictionary where each key
    is a node, and its associated value
    is the integer representing the in-degree
    of that node
    """
    indegree_graph = {}
    nodes = set(digraph.keys())
    all_the_edges = []
    for edges in digraph.values():
        all_the_edges+= list(edges)
    for node in nodes:
        indegree_graph[node]= len([edge for edge in all_the_edges if edge == node])
    return indegree_graph

def in_degree_distribution(digraph):
    """
    computes the in_degree distribution of
    a digraph by returning a dictionary
    with each key representing an in_degree integer,
    the value, an integer representing the number
    of nodes with that in_degree value
    """
    indegree_graph = compute_in_degrees(digraph)
    indegree_distribution = {}
    in_degrees = []
    for val in indegree_graph.values():
        in_degrees.append(val)
    in_degrees = set(in_degrees)
    for in_degree in in_degrees:
        indegree_distribution[in_degree] = len([val for val in indegree_graph.values() if val==in_degree])
    return indegree_distribution