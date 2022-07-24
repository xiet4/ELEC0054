import networkx as nx
from matplotlib import pyplot as plt
from networkx.algorithms.approximation import steiner_tree

import main
# Graph 3 Germany
terminals = 30
color_map = []
G3 = nx.Graph()

G3.add_nodes_from(["Aachen", "Augsburg", "Bayreuth", "Berlin", "Bielefeld", "Braunschweig", "Bremen", "Bremerhaven",
                   "Chemnitz", "Darmstadt", "Dortmund", "Dresden", "Duesseldorf", "Erfurt", "Essen", "Flensburg",
                   "Frankfurt", "Freiburg", "Fulda", "Giessen", "Greifswald", "Hamburg", "Hannover", "Kaiserslautern",
                   "Karlsruhe", "Kassel", "Kempten", "Kiel", "Koblenz", "Koeln", "Konstanz", "Leipzig", "Magdeburg",
                   "Mannheim", "Muenchen", "Muenster", "Norden", "Nuernberg", "Oldenburg", "Osnabrueck", "Passau",
                   "Regensburg", "Saarbruecken", "Schwerin", "Siegen", "Stuttgart", "Trier", "Ulm", "Wesel",
                   "Wuerzburg"])

pos_G3 = {"Aachen": (6.04, 50.76),
          "Augsburg": (10.90, 48.33),
          "Bayreuth": (11.59, 49.93),
          "Berlin": (13.39, 52.52),
          "Bielefeld": (8.50, 52.04),
          "Braunschweig": (10.55, 52.28),
          "Bremen": (8.85, 53.11),
          "Bremerhaven": (8.58, 53.54),
          "Chemnitz": (12.93, 50.84),
          "Darmstadt": (8.65, 49.89),
          "Dortmund": (7.45, 51.51),
          "Dresden": (13.73, 51.03),
          "Duesseldorf": (6.77, 51.25),
          "Erfurt": (11.04, 50.98),
          "Essen": (7.02, 51.46),
          "Flensburg": (9.45, 54.77),
          "Frankfurt": (8.71, 50.12),
          "Freiburg": (7.80, 47.98),
          "Fulda": (9.69, 50.56),
          "Giessen": (8.67, 50.57),
          "Greifswald": (13.40, 54.09),
          "Hamburg": (9.99, 53.57),
          "Hannover": (9.72, 52.38),
          "Kaiserslautern": (7.75, 49.43),
          "Karlsruhe": (8.41, 49.01),
          "Kassel": (9.51, 51.32),
          "Kempten": (10.32, 47.72),
          "Kiel": (10.12, 54.34),
          "Koblenz": (7.52, 50.40),
          "Koeln": (6.87, 50.94),
          "Konstanz": (9.18, 47.66),
          "Leipzig": (12.38, 51.34),
          "Magdeburg": (11.64, 52.14),
          "Mannheim": (8.49, 49.49),
          "Muenchen": (11.57, 48.15),
          "Muenster": (7.60, 51.97),
          "Norden": (7.21, 53.60),
          "Nuernberg": (11.03, 49.57),
          "Oldenburg": (8.21, 53.11),
          "Osnabrueck": (8.03, 52.28),
          "Passau": (13.46, 48.57),
          "Regensburg": (12.09, 49.00),
          "Saarbruecken": (7.03, 49.23),
          "Schwerin": (11.45, 53.55),
          "Siegen": (8.03, 50.91),
          "Stuttgart": (9.10, 48.74),
          "Trier": (6.68, 49.75),
          "Ulm": (9.99, 48.40),
          "Wesel": (6.37, 51.39),
          "Wuerzburg": (9.97, 49.78)
          }

G3.add_edges_from([
    ("Duesseldorf", "Essen", {"weight": 30.74}),
    ("Dortmund", "Essen", {"weight": 31.69}),
    ("Wesel", "Essen", {"weight": 35.53}),
    ("Koeln", "Duesseldorf", {"weight": 34.15}),
    ("Aachen", "Koeln", {"weight": 64.33}),
    ("Koblenz", "Koeln", {"weight": 79.05}),
    ("Muenster", "Dortmund", {"weight": 51.71}),
    ("Siegen", "Dortmund", {"weight": 80.89}),
    ("Kassel", "Dortmund", {"weight": 142.47}),
    ("Wesel", "Aachen", {"weight": 104.69}),
    ("Trier", "Aachen", {"weight": 120.53}),
    ("Bielefeld", "Muenster", {"weight": 62.28}),
    ("Osnabrueck", "Muenster", {"weight": 44.42}),
    ("Siegen", "Koblenz", {"weight": 64.83}),
    ("Frankfurt", "Koblenz", {"weight": 81.53}),
    ("Kaiserslautern", "Koblenz", {"weight": 102.12}),
    ("Trier", "Koblenz", {"weight": 95.49}),
    ("Bielefeld", "Siegen", {"weight": 132.59}),
    ("Giessen", "Siegen", {"weight": 56.23}),
    ("Oldenburg", "Wesel", {"weight": 197.36}),
    ("Norden", "Wesel", {"weight": 219.22}),
    ("Leipzig", "Berlin", {"weight": 149.7}),
    ("Dresden", "Berlin", {"weight": 165.22}),
    ("Schwerin", "Berlin", {"weight": 181.03}),
    ("Magdeburg", "Berlin", {"weight": 128.00}),
    ("Greifswald", "Berlin", {"weight": 175.00}),
    ("Dresden", "Leipzig", {"weight": 100.21}),
    ("Erfurt", "Leipzig", {"weight": 102.50}),
    ("Magdeburg", "Leipzig", {"weight": 101.44}),
    ("Bayreuth", "Leipzig", {"weight": 165.39}),
    ("Erfurt", "Dresden", {"weight": 189.86}),
    ("Chemnitz", "Dresden", {"weight": 61.69}),
    ("Chemnitz", "Erfurt", {"weight": 134.27}),
    ("Kassel", "Erfurt", {"weight": 113.27}),
    ("Wuerzburg", "Erfurt", {"weight": 152.40}),
    ("Bayreuth", "Chemnitz", {"weight": 137.92}),
    ("Magdeburg", "Schwerin", {"weight": 166.81}),
    ("Greifswald", "Schwerin", {"weight": 139.47}),
    ("Hamburg", "Schwerin", {"weight": 94.40}),
    ("Kiel", "Schwerin", {"weight": 114.12}),
    ("Braunschweig", "Magdeburg", {"weight": 77.33}),
    ("Kiel", "Hamburg", {"weight": 86.01}),
    ("Hannover", "Hamburg", {"weight": 132.52}),
    ("Braunschweig", "Hamburg", {"weight": 147.82}),
    ("Oldenburg", "Bremen", {"weight": 40.01}),
    ("Bremerhaven", "Bremen", {"weight": 53.67}),
    ("Hannover", "Bremen", {"weight": 100.10}),
    ("Flensburg", "Kiel", {"weight": 68.15}),
    ("Norden", "Oldenburg", {"weight": 84.38}),
    ("Osnabrueck", "Oldenburg", {"weight": 97.30}),
    ("Bremerhaven", "Flensburg", {"weight": 148.71}),
    ("Bielefeld", "Hannover", {"weight": 90.68}),
    ("Braunschweig", "Hannover", {"weight": 55.07}),
    ("Osnabrueck", "Hannover", {"weight": 114.95}),
    ("Braunschweig", "Bielefeld", {"weight": 138.63}),
    ("Kassel", "Braunschweig", {"weight": 126.83}),
    ("Giessen", "Kassel", {"weight": 99.75}),
    ("Fulda", "Kassel", {"weight": 85.97}),
    ("Darmstadt", "Frankfurt", {"weight": 26.26}),
    ("Giessen", "Frankfurt", {"weight": 52.59}),
    ("Fulda", "Frankfurt", {"weight": 86.10}),
    ("Mannheim", "Darmstadt", {"weight": 44.89}),
    ("Kaiserslautern", "Darmstadt", {"weight": 79.32}),
    ("Karlsruhe", "Mannheim", {"weight": 53.26}),
    ("Saarbruecken", "Kaiserslautern", {"weight": 60.78}),
    ("Karlsruhe", "Kaiserslautern", {"weight": 66.95}),
    ("Fulda", "Giessen", {"weight": 70.45}),
    ("Saarbruecken", "Trier", {"weight": 62.90}),
    ("Wuerzburg", "Fulda", {"weight": 86.37}),
    ("Karlsruhe", "Saarbruecken", {"weight": 105.61}),
    ("Karlsruhe", "Stuttgart", {"weight": 62.34}),
    ("Ulm", "Stuttgart", {"weight": 73.23}),
    ("Konstanz", "Stuttgart", {"weight": 124.00}),
    ("Wuerzburg", "Stuttgart", {"weight": 125.40}),
    ("Freiburg", "Karlsruhe", {"weight": 119.49}),
    ("Augsburg", "Ulm", {"weight": 66.31}),
    ("Freiburg", "Konstanz", {"weight": 105.26}),
    ("Kempten", "Konstanz", {"weight": 85.50}),
    ("Augsburg", "Muenchen", {"weight": 56.79}),
    ("Kempten", "Muenchen", {"weight": 105.22}),
    ("Passau", "Muenchen", {"weight": 147.33}),
    ("Nuernberg", "Muenchen", {"weight": 150.34}),
    ("Regensburg", "Muenchen", {"weight": 104.82}),
    ("Wuerzburg", "Augsburg", {"weight": 173.69}),
    ("Regensburg", "Passau", {"weight": 111.27}),
    ("Bayreuth", "Nuernberg", {"weight": 65.01}),
    ("Wuerzburg", "Nuernberg", {"weight": 91.43}),
    ("Regensburg", "Nuernberg", {"weight": 88.48})
])

for i in range(0, len(G3)):
    if i < terminals:
        color_map.append('red')
    else:
        color_map.append('blue')

nx.draw(G3, node_color=color_map, node_size=200, pos=pos_G3, with_labels=True)
plt.show()

G = nx.convert_node_labels_to_integers(G3, first_label=0, ordering='default', label_attribute=None)
terminal_nodes = list(G)[0:terminals]
print(steiner_tree(G,terminal_nodes))
main.sph(G, pos_G3, terminals)
main.algorithm(G, pos_G3, terminals)
main.algorithm2(G, pos_G3, terminals)
print("-------------------------")
