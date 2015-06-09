"""
Provided code for Application portion of Module 1

Imports physics citation graph
"""

# general imports
from requests import request
from project1 import compute_in_degrees, in_degree_distribution


###################################
# Code for loading citation graph
# Given by the tutors.

CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"

def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph

    Returns a dictionary that models a graph
    """
    graph_file = request('GET', graph_url)
    graph_text = graph_file.text
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[:-1]

    print("Loaded graph with", len(graph_lines), "nodes")

    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph

#citation_graph = load_graph(CITATION_URL)

def ave_out_degree(digraph):
    count = 0
    for nodes in digraph.values():
        for node in nodes:
            count += 1
    degree = count / len(digraph)
    return degree

#print("average out degree of the citation graph is: {}".format(ave_out_degree(citation_graph)))


# print(in_degree_distribution(citation_graph))

distribution = {0: 4594, 1: 3787, 2: 2699, 3: 1994, 4: 1638, 5: 1327, 6: 1138,
                7: 901, 8: 824, 9: 690, 10: 591, 11: 527, 12: 483, 13: 447,
                14: 409, 15: 322, 16: 293, 17: 274, 18: 278, 19: 250, 20: 222,
                21: 185, 22: 185, 23: 162, 24: 160, 25: 136, 26: 128, 27: 126,
                28: 138, 29: 121, 30: 125, 31: 88, 32: 100, 33: 88, 34: 68, 35: 86,
                36: 66, 37: 82, 38: 75, 39: 66, 40: 52, 41: 72, 42: 53, 43: 69,
                44: 50, 45: 56, 46: 52, 47: 44, 48: 29, 49: 48, 50: 34, 51: 33,
                52: 32, 53: 31, 54: 33, 55: 29, 56: 35, 57: 29, 58: 27, 59: 29,
                60: 25, 61: 25, 62: 28, 63: 23, 64: 26, 65: 23, 66: 21, 67: 23,
                68: 24, 69: 19, 70: 22, 71: 21, 72: 10, 73: 17, 74: 13, 75: 19,
                76: 18, 77: 15, 78: 8, 79: 24, 80: 9, 81: 12, 82: 15, 83: 8, 84: 11,
                85: 14, 86: 7, 87: 13, 88: 10, 89: 14, 90: 6, 91: 7, 92: 10, 93: 5,
                94: 17, 95: 10, 96: 10, 97: 10, 98: 4, 99: 9, 100: 7, 101: 9, 102: 9,
                103: 4, 104: 6, 105: 8, 106: 10, 107: 8, 108: 6, 109: 8, 110: 5,
                111: 5, 112: 3, 113: 9, 114: 8, 115: 5, 116: 6, 117: 3, 118: 8,
                119: 5, 120: 2, 121: 5, 122: 3, 123: 4, 124: 6, 125: 5, 126: 5,
                127: 2, 129: 5, 130: 1, 131: 4, 132: 1, 133: 6, 134: 3, 135: 1,
                136: 6, 137: 3, 138: 3, 139: 4, 140: 1, 141: 4, 142: 6, 143: 3,
                144: 5, 145: 3, 146: 3, 147: 1, 148: 6, 149: 4, 150: 4, 151: 5,
                152: 2, 153: 3, 154: 4, 155: 4, 156: 2, 157: 4, 158: 3, 159: 5,
                160: 1, 295: 1, 162: 2, 164: 3, 165: 1, 167: 2, 168: 1, 169: 2,
                171: 2, 172: 6, 173: 2, 174: 2, 1199: 1, 176: 2, 177: 2, 178: 2,
                179: 2, 180: 1, 181: 1, 182: 1, 183: 1, 184: 1, 185: 1, 186: 3,
                187: 1, 188: 2, 701: 1, 190: 3, 191: 2, 192: 2, 193: 2, 194: 2,
                196: 3, 197: 2, 198: 1, 199: 1, 201: 3, 204: 3, 205: 4, 208: 2,
                1144: 1, 211: 1, 212: 1, 213: 1, 214: 1, 217: 1, 219: 1, 220: 2,
                222: 2, 223: 4, 224: 1, 225: 1, 228: 2, 229: 3, 230: 2, 232: 3,
                233: 2, 235: 1, 748: 1, 1775: 1, 240: 1, 242: 2, 244: 1, 189: 1,
                247: 2, 251: 1, 252: 1, 257: 2, 520: 1, 775: 1, 264: 1, 265: 1,
                268: 1, 273: 1, 274: 1, 1299: 1, 788: 2, 1032: 1, 282: 2, 290: 1,
                807: 1, 297: 1, 301: 3, 304: 1, 308: 1, 1641: 1, 315: 1, 651: 1,
                325: 2, 327: 2, 328: 2, 329: 2, 331: 1, 333: 1, 337: 1, 340: 1,
                341: 1, 344: 1, 347: 1, 314: 1, 2414: 1, 373: 1, 380: 2, 383: 1,
                385: 1, 388: 1, 1114: 1, 1006: 1, 406: 1, 411: 1, 421: 1, 424: 1,
                426: 1, 427: 1, 438: 1, 456: 1, 175: 1, 467: 1, 475: 1, 494: 1, 1155: 1}


normalised = dict()
for k,v in distribution.items():
    # The sum of the citations is 27770
    normalised[k] = v/27770.0


if __name__ == '__main__':
    from matplotlib import pyplot as plt
    norm_sorted = sorted(list(normalised.items()))
    xs = list()
    ys = list()
    for x, y in norm_sorted:
        xs.append(x)
        ys.append(y)

    plt.plot(xs, ys)
    plt.yscale('log')
    plt.xscale('log')
    plt.show()
