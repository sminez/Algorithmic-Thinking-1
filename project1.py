'''
This is the first project for Algorithmic Thinking (Part 1): Degree Distribution of Graphs

Author  -- Innes Morrison
Twitter -- @MrMorrisonMaths
'''

EX_GRAPH0 = {0: set([1, 2]),
             1: set(),
             2: set()}

EX_GRAPH1 = {0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3]),
             3: set([0]),
             4: set([1]),
             5: set([2]),
             6: set()}

EX_GRAPH2 = {0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3, 7]),
             3: set([7]),
             4: set([1]),
             5: set([2]),
             6: set(),
             7: set([3]),
             8: set([1, 2]),
             9: set([0, 3, 4, 5, 6, 7])}


def make_complete_graph(num_nodes):
    '''
    Construct and return a dictionary representation of the kth complete digraph.
    --> A complete digraph has all possible unique edges excluding loops.

    Arguments:
    num_nodes -- the number of required nodes (k for the kth complete graph)

    Returns:
    A dictionary representing the adjacency list of the complete graph if num_nodes
    is > 0 otherwise an empty dictionary.
    NOTE: Nodes are numbered 0 to num_nodes - 1.
    '''
    if num_nodes <= 0:
        # Can't have a negative number of nodes and k0 is the empty graph.
        return dict()
    else:
        k_graph = dict()
        for node in range(num_nodes):
            k_graph[node] = set([n for n in range(num_nodes) if n != node])

        return k_graph

def compute_in_degrees(digraph):
    '''
    For a given digraph, find the number of incoming edges for each node and return a
    new dictionary listing those values.

    Arguments:
    digraph -- the dictionary representation of a diagraph.

    Returns:
    A dictionary with the same keys as the digraph but with the degree of each node
    as the values.
    '''
    in_degrees = dict()
    for node in digraph:
        count = 0
        for nodes in digraph.values():
            if node in nodes:
                count += 1
        in_degrees[node] = count
    return in_degrees

def in_degree_distribution(digraph):
    '''
    Find the un-normalised distibution of in-degree values for a digraph.

    Arguments:
    digraph -- dictionary representation of a digraph

    Returns:
    A dictionary of in_degree, count (key, value) pairs.
    '''
    # A list of the individual node degrees in the digraph
    in_degrees = compute_in_degrees(digraph).values()
    # For each degree present in the list, find the frequency and add it to a dictionary
    return dict((degree, list(in_degrees).count(degree)) for degree in in_degrees)



if __name__ == '__main__':
    print(in_degree_distribution(EX_GRAPH0))
    print(in_degree_distribution(EX_GRAPH1))
    print(in_degree_distribution(EX_GRAPH2))
