import itertools
import math
import time

import networkx as nx


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


def shortest_distance2(components, terminals_nodes, pos):
    distance = {}
    for i in components:
        for j in terminals_nodes:
            distance[i, j] = cal_distance(pos.get(i), pos.get(j))
    return shortest_distance(sorted(distance.items(), key=lambda kv: (kv[1], kv[0])))


def shortest_distance3(components, terminals_nodes, G):
    distance = {}
    for i in components:
        for j in terminals_nodes:
            distance[i, j] = len(nx.dijkstra_path(G, i, j))
    return shortest_distance(sorted(distance.items(), key=lambda kv: (kv[1], kv[0])))


def shortest_distance4(components, terminals_nodes, pos, G):
    distance = {}
    for i in components:
        for j in terminals_nodes:
            distance[i, j] = len(Human_gaze_algorithm_3(G, i, j, pos))
    return shortest_distance(sorted(distance.items(), key=lambda kv: (kv[1], kv[0])))


def algorithm(G, pos, terminals):
    i = 0
    for key in pos.copy():
        pos[i] = pos.pop(key)
        i = i + 1

    terminals_pos = dict(itertools.islice(pos.items(), terminals))
    terminal_node = list(G)[0:terminals]
    n = 0
    components = []
    start_time = time.perf_counter()
    while len(terminal_node) > 0:
        if n == 0:
            start, end = shortest_distance(all_distance(terminals_pos))
            components = Human_gaze_algorithm_3(G, start, end, pos)

        terminals_node = [i for i in terminal_node if i not in components]
        if len(terminals_node) == 0:
            break
        start, end = shortest_distance2(components, terminals_node, pos)
        new_components = Human_gaze_algorithm_3(G, start, end, pos)
        components = list(set(components).union(set(new_components)))
        terminals_node.remove(end)
        n = n + 1
    end_time = time.perf_counter()
    print("Algorithm1 :")
    print(components)
    print(len(components))
    print("time cost:", float(end_time - start_time) * 1000.0, "ms")
    return components


def algorithm2(G, pos, terminals):
    i = 0
    for key in pos.copy():
        pos[i] = pos.pop(key)
        i = i + 1
    n = 0
    terminal_node = list(G)[0:terminals]
    components = []
    terminals_pos = dict(itertools.islice(pos.items(), terminals))
    start_time = time.perf_counter()
    while len(terminal_node) > 0:
        if n == 0:
            start, end = shortest_distance(all_distance(terminals_pos))
            components = Human_gaze_algorithm_3(G, start, end, pos)

        terminals_node = [i for i in terminal_node if i not in components]
        if len(terminals_node) == 0:
            break
        start, end = shortest_distance4(components, terminals_node, pos, G)
        new_components = Human_gaze_algorithm_3(G, start, end, pos)
        components = list(set(components).union(set(new_components)))
        terminals_node.remove(end)
        n = n + 1
    end_time = time.perf_counter()
    print("Algorithm2 :")
    print(components)
    print(len(components))
    print("time cost:", float(end_time - start_time) * 1000.0, "ms")
    return components

def sph(G, pos, terminals):
    i = 0
    for key in pos.copy():
        pos[i] = pos.pop(key)
        i = i + 1
    n = 0
    terminal_node = list(G)[0:terminals]
    components = []
    terminals_pos = dict(itertools.islice(pos.items(), terminals))
    start_time = time.perf_counter()
    while len(terminal_node) > 0:
        if n == 0:
            start, end = shortest_distance(all_distance(terminals_pos))
            components = nx.dijkstra_path(G, start, end)

        terminals_node = [i for i in terminal_node if i not in components]
        if len(terminals_node) == 0:
            break
        start, end = shortest_distance3(components, terminals_node, G)
        new_components = nx.dijkstra_path(G, start, end)
        components = list(set(components).union(set(new_components)))
        terminals_node.remove(end)
        n = n + 1
    end_time = time.perf_counter()
    print("Sph :")
    print(components)
    print(len(components))
    print("time cost:", float(end_time - start_time) * 1000.0, "ms")
    return components
