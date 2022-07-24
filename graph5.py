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

G5.add_edges_from([
    ("Amsterdam", "Brussels", {"weight": 2.59}),
    ("Amsterdam", "Glasgow", {"weight": 10.67}),
    ("Amsterdam", "Hamburg", {"weight": 5.52}),
    ("Amsterdam", "London", {"weight": 5.40}),
    ("Athens", "Palermo", {"weight": 13.63}),
    ("Athens", "Sofia", {"weight": 7.94}),
    ("Athens", "Zagreb", {"weight": 15.00}),
    ("Barcelona", "Madrid", {"weight": 7.60}),
    ("Barcelona", "Marseille", {"weight": 5.08}),
    ("Barcelona", "Seville", {"weight": 12.44}),
    ("Belgrade", "Budapest", {"weight": 4.74}),
    ("Belgrade", "Sofia", {"weight": 4.87}),
    ("Belgrade", "Zagreb", {"weight": 5.51}),
    ("Berlin", "Copenhagen", {"weight": 5.40}),
    ("Berlin", "Hamburg", {"weight": 3.81}),
    ("Berlin", "Munich", {"weight": 7.57}),
    ("Berlin", "Prague", {"weight": 4.20}),
    ("Berlin", "Warsaw", {"weight": 7.75}),
    ("Birmingham", "Glasgow", {"weight": 6.10}),
    ("Birmingham", "London", {"weight": 2.39}),
    ("Bordeaux", "Madrid", {"weight": 8.34}),
    ("Bordeaux", "Marseille", {"weight": 7.56}),
    ("Bordeaux", "Paris", {"weight": 7.47}),
    ("Brussels", "Dusseldorf", {"weight": 2.64}),
    ("Brussels", "Paris", {"weight": 3.93}),
    ("Budapest", "Krakow", {"weight": 4.36}),
    ("Budapest", "Prague", {"weight": 6.68}),
    ("Copenhagen", "Oslo", {"weight": 7.22}),
    ("Copenhagen", "Stockholm", {"weight": 7.77}),
    ("Dublin", "Glasgow", {"weight": 4.62}),
    ("Dublin", "London", {"weight": 6.90}),
    ("Dusseldorf", "Frankfurt", {"weight": 2.75}),
    ("Frankfurt", "Hamburg", {"weight": 5.92}),
    ("Frankfurt", "Munich", {"weight": 4.56}),
    ("Frankfurt", "Strasbourg", {"weight": 2.71}),
    ("Helsinki", "Oslo", {"weight": 11.82}),
    ("Helsinki", "Stockholm", {"weight": 5.97}),
    ("Helsinki", "Warsaw", {"weight": 13.70}),
    ("Krakow", "Warsaw", {"weight": 3.83}),
    ("Lisbon", "London", {"weight": 19.77}),
    ("Lisbon", "Madrid", {"weight": 7.51}),
    ("Lisbon", "Seville", {"weight": 4.71}),
    ("London", "Paris", {"weight": 5.14}),
    ("Lyon", "Marseille", {"weight": 4.11}),
    ("Lyon", "Paris", {"weight": 5.94}),
    ("Lyon", "Zurich", {"weight": 5.07}),
    ("Marseille", "Rome", {"weight": 9.07}),
    ("Milan", "Munich", {"weight": 5.22}),
    ("Milan", "Rome", {"weight": 7.20}),
    ("Milan", "Zurich", {"weight": 3.27}),
    ("Munich", "Vienna", {"weight": 5.34}),
    ("Palermo", "Rome", {"weight": 6.38}),
    ("Paris", "Strasbourg", {"weight": 6.00}),
    ("Prague", "Vienna", {"weight": 3.76}),
    ("Rome", "Zagreb", {"weight": 7.83}),
    ("Strasbourg", "Zurich", {"weight": 2.18}),
    ("Vienna", "Zagreb", {"weight": 4.00})
])

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