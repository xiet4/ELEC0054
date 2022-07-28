import networkx as nx
from matplotlib import pyplot as plt
from networkx.algorithms.approximation import steiner_tree

import main
# Graph 5  Europe
terminals = 10
color_map = []
G5 = nx.Graph()

G5.add_nodes_from(["Amsterdam", "Athens", "Barcelona", "Belgrade", "Berlin", "Birmingham", "Bordeaux", "Brussels",
                   "Budapest", "Copenhagen", "Dublin", "Dusseldorf", "Frankfurt", "Glasgow", "Hamburg", "Helsinki",
                   "Krakow", "Lisbon", "London", "Lyon", "Madrid", "Marseille", "Milan", "Munich", "Oslo", "Palermo",
                   "Paris", "Prague", "Rome", "Seville", "Sofia", "Stockholm", "Strasbourg", "Vienna", "Warsaw",
                   "Zagreb", "Zurich"])

pos_G5 = {
    "Amsterdam": (4.90, 52.35),
    "Athens": (23.73, 38.00),
    "Barcelona": (2.18, 41.37),
    "Belgrade": (20.50, 44.83),
    "Berlin": (13.40, 52.52),
    "Birmingham": (-1.88, 52.47),
    "Bordeaux": (-0.57, 44.85),
    "Brussels": (4.35, 50.83),
    "Budapest": (19.08, 47.50),
    "Copenhagen": (12.57, 55.72),
    "Dublin": (-6.25, 53.33),
    "Dusseldorf": (6.78, 51.23),
    "Frankfurt": (8.67, 50.10),
    "Glasgow": (-4.25, 55.85),
    "Hamburg": (10.02, 53.55),
    "Helsinki": (24.97, 60.17),
    "Krakow": (19.95, 50.05),
    "Lisbon": (-9.13, 38.73),
    "London": (-0.17, 51.50),
    "Lyon": (4.83, 45.73),
    "Madrid": (-3.72, 40.42),
    "Marseille": (5.37, 43.30),
    "Milan": (9.17, 45.47),
    "Munich": (11.57, 48.13),
    "Oslo": (10.75, 59.93),
    "Palermo": (13.35, 38.12),
    "Paris": (2.33, 48.87),
    "Prague": (14.43, 50.08),
    "Rome": (12.50, 41.88),
    "Seville": (-5.98, 37.38),
    "Sofia": (23.33, 42.75),
    "Stockholm": (18.05, 59.33),
    "Strasbourg": (7.77, 48.58),
    "Vienna": (16.37, 48.22),
    "Warsaw": (21.00, 52.25),
    "Zagreb": (16.02, 45.83),
    "Zurich": (8.55, 47.38)
}

G5.add_edges_from([('Amsterdam', 'Brussels', {'weight': 1}), ('Amsterdam', 'Glasgow', {'weight': 1}),
       ('Amsterdam', 'Hamburg', {'weight': 1}), ('Amsterdam', 'London', {'weight': 1}),
       ('Athens', 'Palermo', {'weight': 1}), ('Athens', 'Sofia', {'weight': 1}), ('Athens', 'Zagreb', {'weight': 1}),
       ('Barcelona', 'Madrid', {'weight': 1}), ('Barcelona', 'Marseille', {'weight': 1}),
       ('Barcelona', 'Seville', {'weight': 1}), ('Belgrade', 'Budapest', {'weight': 1}),
       ('Belgrade', 'Sofia', {'weight': 1}), ('Belgrade', 'Zagreb', {'weight': 1}),
       ('Berlin', 'Copenhagen', {'weight': 1}), ('Berlin', 'Hamburg', {'weight': 1}),
       ('Berlin', 'Munich', {'weight': 1}), ('Berlin', 'Prague', {'weight': 1}), ('Berlin', 'Warsaw', {'weight': 1}),
       ('Birmingham', 'Glasgow', {'weight': 1}), ('Birmingham', 'London', {'weight': 1}),
       ('Bordeaux', 'Madrid', {'weight': 1}), ('Bordeaux', 'Marseille', {'weight': 1}),
       ('Bordeaux', 'Paris', {'weight': 1}), ('Brussels', 'Dusseldorf', {'weight': 1}),
       ('Brussels', 'Paris', {'weight': 1}), ('Budapest', 'Krakow', {'weight': 1}),
       ('Budapest', 'Prague', {'weight': 1}), ('Copenhagen', 'Oslo', {'weight': 1}),
       ('Copenhagen', 'Stockholm', {'weight': 1}), ('Dublin', 'Glasgow', {'weight': 1}),
       ('Dublin', 'London', {'weight': 1}), ('Dusseldorf', 'Frankfurt', {'weight': 1}),
       ('Frankfurt', 'Hamburg', {'weight': 1}), ('Frankfurt', 'Munich', {'weight': 1}),
       ('Frankfurt', 'Strasbourg', {'weight': 1}), ('Helsinki', 'Oslo', {'weight': 1}),
       ('Helsinki', 'Stockholm', {'weight': 1}), ('Helsinki', 'Warsaw', {'weight': 1}),
       ('Krakow', 'Warsaw', {'weight': 1}), ('Lisbon', 'London', {'weight': 1}), ('Lisbon', 'Madrid', {'weight': 1}),
       ('Lisbon', 'Seville', {'weight': 1}), ('London', 'Paris', {'weight': 1}), ('Lyon', 'Marseille', {'weight': 1}),
       ('Lyon', 'Paris', {'weight': 1}), ('Lyon', 'Zurich', {'weight': 1}), ('Marseille', 'Rome', {'weight': 1}),
       ('Milan', 'Munich', {'weight': 1}), ('Milan', 'Rome', {'weight': 1}), ('Milan', 'Zurich', {'weight': 1}),
       ('Munich', 'Vienna', {'weight': 1}), ('Palermo', 'Rome', {'weight': 1}), ('Paris', 'Strasbourg', {'weight': 1}),
       ('Prague', 'Vienna', {'weight': 1}), ('Rome', 'Zagreb', {'weight': 1}), ('Strasbourg', 'Zurich', {'weight': 1}),
       ('Vienna', 'Zagreb', {'weight': 1})])

for i in range(0, len(G5)):
    if i < terminals:
        color_map.append('red')
    else:
        color_map.append('blue')

nx.draw(G5, node_color=color_map, node_size=200, pos=pos_G5, with_labels=True)
plt.show()

G = nx.convert_node_labels_to_integers(G5, first_label=0, ordering='default', label_attribute=None)
terminal_nodes = list(G)[0:terminals]
print(steiner_tree(G,terminal_nodes))
main.sph(G, pos_G5, terminals)
main.algorithm(G, pos_G5, terminals)
main.algorithm2(G, pos_G5, terminals)
print("-------------------------")