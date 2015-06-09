digraph1 = {0: set([1]),
            1: set([2]),
            2: set([3]),
            3: set([4, 2]),
            4: set([5, 2]),
            5: set([0, 2])}

def in_degree(digraph, node):
    '''
    Computes the in-degree of a given node in a digraph.

    Arguments:
    digraph -- a dictionary representing the digraph.
    node    -- a key from the dictionary representing the node.

    Returns:
    The in-degree of the node.
    '''
    degree = 0
    for n in digraph.keys():
        if node in digraph[n]:
            degree += 1
    return degree


print(in_degree(digraph1, 2))
