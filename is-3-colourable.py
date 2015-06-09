from itertools import combinations, chain


def powerset(iterable):
    '''
    Generate the powerset (set of all subsets) of a given iterable.
    '''
    initialSet = list(iterable)
    return chain.from_iterable(combinations(intialSet, subSetSize) for subSetSize in range(len(intialSet) + 1))


def contains_edges(graph, nodeset):
    '''
    Check for edges between selected nodes in a graph

    Return true if an edge is found, otherwise false.
    '''
    for node in nodeset:
        for neighbour in graph[node]:
            if neighbour in nodeset:
                return True
    return False


def isThreeColourable(graph):
    '''
    Determines whether a given graph is three colourable.

    Arguments:
      graph -- the adjacency list of a graph

    Returns:
      True if the graph is three colourable otherwise False
    '''
    V = set(graph.keys())
    for rnodes in powerset(V):
        rset = set(rnodes)
        if not contains_edges(graph, rset):
            for gnodes in powerset(V - rset):
                gset = set(gnodes)
                if not contains_edges(graph, gset):
                    bset = set(V - rset - gset)
                    if not contains_edges(graph, bset):
                        return True
    return False


if __name__ == '__main__':
    GRAPH1 = {0: set([1, 2]),
              1: set([0, 2]),
              2: set([0, 1])}

    GRAPH2 = {0: set([1, 2, 3]),
              1: set([0, 2, 3]),
              2: set([0, 1, 3]),
              3: set([0, 1, 2])}

    GRAPH3 = {0: set([1, 2, 4, 5]),
              1: set([0, 2, 3, 5]),
              2: set([0, 1, 3, 4]),
              3: set([1, 2, 4, 5]),
              4: set([0, 2, 3, 5]),
              5: set([0, 1, 3, 4])}

    GRAPH4 = {1: set([2, 8]),
              2: set([1, 3, 4, 6, 8]),
              3: set([2, 4]),
              4: set([2, 3, 5, 6, 8]),
              5: set([4, 6]),
              6: set([2, 4, 5, 7, 8]),
              7: set([6, 8]),
              8: set([1, 2, 4, 6, 7])}

    print(isThreeColourable(GRAPH1))
    print(isThreeColourable(GRAPH2))
    print(isThreeColourable(GRAPH3))
    print(isThreeColourable(GRAPH4))