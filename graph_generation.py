from random import random, choice
from itertools import combinations, permutations
from project1 import compute_in_degrees, in_degree_distribution
from application1 import load_graph
from undirectedGraphs import node_count, edge_count


def is_undirected_graph_valid(graph):
    '''
    Tests whether the given graph is logically valid.

    Asserts for every unordered pair of distinct nodes {n1, n2} that
    if n2 appears in n1's adjacency set then n1 also appears in
    n2's adjacency set. Also asserts that no node appears in
    its own adjacency set and that every value that appears in
    an adjacency set is a node in the graph.

    Arguments:
      graph -- The graph in dictionary form to test.

    Returns:
      True if the graph is logically valid.  False otherwise.
    '''
    # Check that all values are valid nodes
    all_values = set()
    for node_set in graph.values():
        for node in node_set:
            all_values.add(node)

    for node in all_values:
        try:
            graph[node]
        except:
            print('Found {} in adjacency set: this is not a node in the graph!'.format(node))
            return False

    # Check for self loops
    for node in graph:
        if node in graph[node]:
            print('Self loop found on node {}'.format(node))
            return False

    # Check that edges are recorded on both nodes that they connect
    for node in graph:
        for neighbour in graph[node]:
            if node not in graph[neighbour]:
                print('Invalid edge representation between {} and {}'.format(node, neighbour))
                return False

    return True


def find_popular(graph):
    '''
    Determine the 'popular' nodes in a given graph.
    (A node is popular if its degree is greater than the
    mean degree of the graph.)

    Arguments:
      graph -- adjacency list of a graph
    Returns:
      a list of the popular nodes.
    '''
    mean_deg = 2 * edge_count(graph) / node_count(graph)
    popular = list()
    for node in graph:
        degree = 0
        for neighbour in graph:
            if node in graph[neighbour]:
                degree += 1
        if degree > mean_deg:
            popular.append(node)

    return popular


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


def ER_random_graph(num_nodes, prob, directed=False):
    '''
    Generate a random undirected graph using the Erdos-Renyi method.

    Arguments:
    num_nodes -- number of nodes in final graph
    prob -- probability of adding an edge

    Returns:
    A dictionary representation of the adjacency-list for the graph.
    '''
    # Run the ER algorithm to generate the list of edges selected
    V = range(num_nodes)
    E = list()

    # Cover special cases
    if prob <= 0:
        # Return a graph of num_nodes nodes and no edges
        return {node: {} for node in V}
    elif prob >= 1:
        # All edges will be selected to return a complete graph
        return make_complete_graph(num_nodes)

    # Generate candidate edges for a graph or digraph
    if directed:
        pairings = permutations(range(num_nodes), 2)
    else:
        pairings = combinations(range(num_nodes), 2)

    for edge in pairings:
        if random() < prob:
            E.append(edge)

    # Convert the two sets V and E into a python dictionary representation of
    # the graph's adjacency-list.
    G = dict()
    for edge in V:
        edges = list()
        for pair in E:
            if edge in pair:
                for e in pair:
                    if e != edge:
                        edges.append(e)
        G[edge] = set(edges)

    return G


def DPA_random_graph(num_nodes, k_graph_size):
    '''
    Generate a random undirected graph using the Degree Proximity Algorithm.

    Arguments:
      num_nodes -- number of nodes in final graph
      k_graph_size -- size of the initial complete graph.

    Returns:
      A dictionary representation of the adjacency-list for the random graph.
    '''
    # Check for valid input before running
    try:
        assert(k_graph_size <= num_nodes)
    except:
        print("Invalid input, comp_size must be less than or equal to num_nodes")

    # Build the complete graph of m nodes
    output_graph = make_complete_graph(k_graph_size)
    # This essentially keeps track of the current in degree of each node, allowing us to use random.choice()
    # to perform a weighted selection
    weighted_node_list = [node for node in range(k_graph_size) for dummy in range(k_graph_size)]

    for node in range (k_graph_size, num_nodes):
        new_node_neighbours = set()
        for dummy in range(k_graph_size):
            new_node_neighbours.add(choice(weighted_node_list))
        # Update the weighted_node_list to correct ratios
        weighted_node_list.append(node)
        weighted_node_list.extend(list(new_node_neighbours))
        output_graph[node] = set(new_node_neighbours)

    return output_graph


if __name__ == '__main__':
    pop1 = load_graph("http://storage.googleapis.com/codeskulptor-alg/random10.txt")
    pop2 = load_graph("http://storage.googleapis.com/codeskulptor-alg/random100.txt")
    pop3 = load_graph("http://storage.googleapis.com/codeskulptor-alg/random1000.txt")
    pop4 = load_graph("http://storage.googleapis.com/codeskulptor-alg/random10000.txt")
    print(find_popular(pop1))
    print(find_popular(pop2))
    print(find_popular(pop3))
    print(find_popular(pop4))
'''
    print('Expected output is True, False, True, False, False.')

    graph1 = { "0" : set(["1","2"]),
               "1" : set(["0","2"]),
               "2" : set(["1","0"]) }
    print('  Graph1, ', is_undirected_graph_valid(graph1))    # should return true

    graph2 = { "0" : set(["1","2"]),
               "1" : set(["0","2"]),
               "2" : set(["1"]) }
    print('  Graph2, ', is_undirected_graph_valid(graph2))    # should return false

    graph3 = make_complete_graph(100)
    print('  Graph3, ', is_undirected_graph_valid(graph3))    # should return true

    graph4 = { "0" : set(["1","2"]),
               "1" : set(["0","2"]),
               "2" : set(["1","3"]) }
    print('  Graph4, ', is_undirected_graph_valid(graph4))    # should return false

    graph5 = { "0" : set(["0"]) }
    print('  Graph5, ', is_undirected_graph_valid(graph5))    # should return false
'''
