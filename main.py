import itertools
import math

import networkx as nx

terminals = 6
color_map = []
G1 = nx.fast_gnp_random_graph(10, 0.5)
for node in G1:
    if node < terminals:
        color_map.append('red')
    else:
        color_map.append('blue')

pos_G1 = nx.random_layout(G1)
print(pos_G1)
terminals_pos = dict(itertools.islice(pos_G1.items(), terminals))
terminal_nodes = list(G1)[0:terminals]

nx.draw(G1, node_color=color_map, node_size=800, pos=pos_G1, with_labels=True)


def dot(v, w):
    x, y = v
    X, Y = w
    return x * X + y * Y


def length(v):
    x, y = v
    return math.sqrt(x * x + y * y)


def vector(b, e):
    x, y = b
    X, Y = e
    return (X - x, Y - y)


def unit(v):
    x, y = v
    mag = length(v)
    return (x / mag, y / mag)


def distance(p0, p1):
    return length(vector(p0, p1))


def scale(v, sc):
    x, y = v
    return (x * sc, y * sc)


def add(v, w):
    x, y = v
    X, Y = w
    return (x + X, y + Y)


def pnt2line(pnt, start, end):  # node position as input
    line_vec = vector(start, end)
    pnt_vec = vector(start, pnt)
    line_len = length(line_vec)
    line_unitvec = unit(line_vec)
    pnt_vec_scaled = scale(pnt_vec, 1.0 / line_len)
    t = dot(line_unitvec, pnt_vec_scaled)
    if t < 0.0:
        t = 0.0
    elif t > 1.0:
        t = 1.0
    nearest = scale(line_vec, t)
    dist = distance(nearest, pnt_vec)
    nearest = add(nearest, start)
    return dist


def dist_euclidean(p1, p2, pos):  # node name as input and pos to specify name of position variable for this graph
    x1, y1 = pos[p1]
    x2, y2 = pos[p2]
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)


def Human_gaze_algorithm_3(Graph, start_node, end_node, pos):
    current_node = start_node
    visited_nodes = [start_node]
    dead_nodes = []  # a node might be added multiple times to this know maybe as it was before might not be a problem
    while current_node != end_node:
        neighbors = list(Graph.neighbors(current_node))
        for i in visited_nodes:
            if i in neighbors:
                neighbors.remove(i)
        for i in dead_nodes:
            if i in neighbors:
                neighbors.remove(i)

        if len(neighbors) == 0:
            visited_nodes.remove(current_node)
            dead_nodes.append(current_node)

            while len(neighbors) == 0:

                current_node = visited_nodes[-1]

                neighbors = list(Graph.neighbors(current_node))
                # is this still necessary if we have dead_nodes conditional
                for i in visited_nodes:
                    if i in neighbors:
                        neighbors.remove(i)
                for i in dead_nodes:
                    if i in neighbors:
                        neighbors.remove(i)
                visited_nodes.remove(
                    current_node)  # instead of adding it again to visited nodes we want to take it away

            visited_nodes.append(current_node)

        options = {}

        for i in neighbors:
            options[i] = pnt2line(pos[i], pos[current_node], pos[end_node])
            options[i] += dist_euclidean(i, end_node, pos)
        current_node = min(options, key=options.get)
        visited_nodes.append(current_node)

    return visited_nodes


def cal_distance(p1, p2):
    return math.sqrt(math.pow((p2[0] - p1[0]), 2) + math.pow((p2[1] - p1[1]), 2))


def all_distance(pos):
    distance = {}
    for i in pos:
        for j in range(i + 1, len(pos)):
            distance[i, j] = cal_distance(pos[i], pos[j])
    return sorted(distance.items(), key=lambda kv: (kv[1], kv[0]))


def shortest_distance(pos):
    start = pos[0][0][0]
    end = pos[0][0][1]
    return start, end


def shortest_distance2(components, terminals_nodes):
    distance = {}
    for i in components:
        for j in terminals_nodes:
            distance[i, j] = cal_distance(pos_G1.get(i), pos_G1.get(j))
    return shortest_distance(sorted(distance.items(), key=lambda kv: (kv[1], kv[0])))


n = 0
start = 0
end = 0
components = []
while len(terminal_nodes) > 0:
    if n == 0:
        start, end = shortest_distance(all_distance(terminals_pos))
        components = Human_gaze_algorithm_3(G1, start, end, pos_G1)

    terminals_nodes = [i for i in terminal_nodes if i not in components]
    if len(terminals_nodes) == 0: break
    start, end = shortest_distance2(components, terminals_nodes)
    new_components = Human_gaze_algorithm_3(G1, start, end, pos_G1)
    components = list(set(components).union(set(new_components)))
    terminals_nodes.remove(end)
    n = n + 1

print(components)
