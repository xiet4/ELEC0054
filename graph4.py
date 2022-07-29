import networkx as nx
from matplotlib import pyplot as plt
from networkx.algorithms.approximation import steiner_tree

import main
# Graph 4  USA 30
terminals = 15
color_map = []
G4 = nx.Graph()

G4.add_nodes_from(["Atlanta", "Baltimore", "Boston", "Chicago", "Charlotte", "Cleveland", "Dallas", "Denver", "ElPaso",
                   "Houston", "Indianapolis", "KansasCity", "LosAngeles", "LasVegas", "Miami", "Parkersburg",
                   "NewOrleans",
                   "NewYork", "Philadelphia", "Phoenix", "Sacramento", "SaltLakeCity", "SanAntonio", "SanFrancisco",
                   "SanJose", "StLouis", "Seattle", "Tampa", "Tallahassee", "Washington,DC"])

pos_G4 = {'Atlanta': (84.42, 33.76),
          'Baltimore': (76.61, 39.3),
          'Boston': (71.2, 42.43),
          'Chicago': (87.68, 41.84),
          'Charlotte': (80.83, 35.2),
          'Cleveland': (81.68, 41.48),
          'Dallas': (96.77, 32.79),
          'Denver': (104.87, 38.77),
          'ElPaso': (106.44, 31.85),
          'Houston': (95.39, 29.77),
          'Indianapolis': (86.15, 39.78),
          'KansasCity': (94.55, 39.12),
          'LosAngeles': (118.41, 34.11),
          'LasVegas': (115.17, 36.8),
          'Miami': (80.21, 25.78),
          'Parkersburg': (80.65, 38.48),
          'NewOrleans': (89.93, 30.7),
          'NewYork': (73.94, 40.67),
          'Philadelphia': (75.13, 40.1),
          'Phoenix': (112.7, 33.54),
          'Sacramento': (121.47, 38.57),
          'SaltLakeCity': (111.93, 40.78),
          'SanAntonio': (98.51, 29.46),
          'SanFrancisco': (122.38, 37.62),
          'SanJose': (121.92, 37.37),
          'StLouis': (90.24, 38.64),
          'Seattle': (122.35, 47.62),
          'Tampa': (82.48, 27.96),
          'Tallahassee': (84.28, 30.46),
          'Washington,DC': (77.2, 38.91)}

G4.add_edges_from([("Charlotte", "Miami", {"weight": 1}),
                   ("Atlanta", "Houston", {"weight": 1}),
                   ("Atlanta", "Charlotte", {"weight": 1}),
                   ("StLouis", "Indianapolis", {"weight": 1}),
                   ("Seattle", "Sacramento", {"weight": 1}),
                   ("Washington,DC", "Charlotte", {"weight": 1}),
                   ("Baltimore", "Philadelphia", {"weight": 1}),
                   ("Baltimore", "Washington,DC", {"weight": 1}),
                   ("Denver", "SaltLakeCity", {"weight": 1}),
                   ("Sacramento", "SanFrancisco", {"weight": 1}),
                   ("Cleveland", "Boston", {"weight": 1}),
                   ("SanJose", "LosAngeles", {"weight": 1}),
                   ("Chicago", "Cleveland", {"weight": 1}),
                   ("Chicago", "Indianapolis", {"weight": 1}),
                   ("Denver", "ElPaso", {"weight": 1}),
                   ("Boston", "NewYork", {"weight": 1}),
                   ("NewOrleans", "Houston", {"weight": 1}),
                   ("Parkersburg", "Washington,DC", {"weight": 1}),
                   ("KansasCity", "Dallas", {"weight": 1}),
                   ("Dallas", "Houston", {"weight": 1}),
                   ("Indianapolis", "Parkersburg", {"weight": 1}),
                   ("SaltLakeCity", "LasVegas", {"weight": 1}),
                   ("SaltLakeCity", "Sacramento", {"weight": 1}),
                   ("KansasCity", "Denver", {"weight": 1}),
                   ("ElPaso", "Phoenix", {"weight": 1}),
                   ("ElPaso", "SanAntonio", {"weight": 1}),
                   ("Seattle", "SaltLakeCity", {"weight": 1}),
                   ("Houston", "SanAntonio", {"weight": 1}),
                   ("LosAngeles", "Phoenix", {"weight": 1}),
                   ("KansasCity", "StLouis", {"weight": 1}),
                   ("LasVegas", "Phoenix", {"weight": 1}),
                   ("Miami", "Tampa", {"weight": 1}),
                   ("NewOrleans", "Tallahassee", {"weight": 1}),
                   ("NewYork", "Philadelphia", {"weight": 1}),
                   ("SanFrancisco", "SanJose", {"weight": 1}),
                   ("Tampa", "Tallahassee", {"weight": 1})])

for i in range(0, len(G4)):
    if i < terminals:
        color_map.append('red')
    else:
        color_map.append('blue')

nx.draw(G4, node_color=color_map, node_size=200, pos=pos_G4, with_labels=True)
plt.show()
G = nx.convert_node_labels_to_integers(G4, first_label=0, ordering='default', label_attribute=None)
print(nx.dijkstra_path(G,0,25,weight='weight'))

terminal_nodes = list(G)[0:terminals]
print(steiner_tree(G,terminal_nodes))
main.sph(G, pos_G4, terminals)
main.algorithm(G, pos_G4, terminals)
main.algorithm2(G, pos_G4, terminals)
main.algorithm3(G, pos_G4, terminals)
print("-------------------------")