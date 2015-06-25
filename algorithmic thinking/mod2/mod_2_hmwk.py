"""
Functions for implementing breadth-first search algorithm,
connected components algorithm and others

"""
# coding: utf-8

# In[3]:

from collections import deque


# In[88]:

def bfs_visited(ugraph,start_node):
    """
    Input: undirected graph [ugraph], node [start_node]
    Output: Visited = {all nodes visited}
    """
    visited = {start_node}
    queue = deque([start_node])
    nodes = ugraph.keys()
    while queue:
        popped = queue.pop()
        if popped in nodes:
            for neighbor in ugraph[popped]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    return visited
    


# In[89]:

def cc_visited(ugraph):
    """
    Takes the undirected graph ugraph
    and returns a list of sets, where
    each set consists of all the nodes 
    (and nothing else) in a connected
    component, and there is exactly one
    set in the list for each connected 
    component in ugraph and nothing else.
    """
    remaining_nodes = ugraph.keys()
    connected_components = []
    while remaining_nodes:
        popped_node = remaining_nodes.pop()
        visited_nodes = bfs_visited(ugraph,popped_node)
        if visited_nodes not in connected_components:
            connected_components.append(visited_nodes)
    return connected_components
    


# In[98]:

def compute_resilience(ugraph, attack_order):
    """
    Takes the undirected graph ugraph
    a list of nodes attack_order and
    iterates through the nodes in attack_order.
    For each node in the list, the function
    removes the given node and its edges from
    the graph and then computes the size of 
    the largest connected component for the 
    resulting graph.
    """
    max_cc = [largest_cc_size(ugraph)]
    for node in attack_order:
        ugraph.pop(node,None)
        for edges in ugraph.values():
            if node in edges:
                edges.remove(node)
        max_cc.append(largest_cc_size(ugraph))
    return sorted(max_cc,reverse=True)
    


# In[101]:

def largest_cc_size(ugraph):
    """
    returns the size of the largest connected component
    """
    cc = cc_visited(ugraph)
    if cc:
        return max(map(len,cc))
    else:
        return 0



