graph1 = {0: set([1]),
          1: set([0,2]),
          2: set([1])}

graph2 = {}

def node_count(graph):
    '''
    Return the number of nodes in a graph.

    Arguments:
    graph -- The graph to analyse.

    Returns:
    The number of nodes in the graph
    '''
    return len(graph.keys())


def edge_count(graph):
    '''
    Return the number of edges in a graph.

    Arguments:
    graph -- the graph to be analysed.

    Returns:
    The number of edges in the graph
    '''
    count = 0
    for node in graph.values():
        for edge in node:
            count += 1
    return count / 2

if __name__ == '__main__':
    print(node_count(graph1))
    print(node_count(graph2))
    print(edge_count(graph1))
    print(edge_count(graph2))
