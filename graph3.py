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

G3.add_edges_from([('Duesseldorf', 'Essen', {'weight': 1}), ('Dortmund', 'Essen', {'weight': 1}), ('Wesel', 'Essen', {'weight': 1}),
       ('Koeln', 'Duesseldorf', {'weight': 1}), ('Aachen', 'Koeln', {'weight': 1}), ('Koblenz', 'Koeln', {'weight': 1}),
       ('Muenster', 'Dortmund', {'weight': 1}), ('Siegen', 'Dortmund', {'weight': 1}),
       ('Kassel', 'Dortmund', {'weight': 1}), ('Wesel', 'Aachen', {'weight': 1}), ('Trier', 'Aachen', {'weight': 1}),
       ('Bielefeld', 'Muenster', {'weight': 1}), ('Osnabrueck', 'Muenster', {'weight': 1}),
       ('Siegen', 'Koblenz', {'weight': 1}), ('Frankfurt', 'Koblenz', {'weight': 1}),
       ('Kaiserslautern', 'Koblenz', {'weight': 1}), ('Trier', 'Koblenz', {'weight': 1}),
       ('Bielefeld', 'Siegen', {'weight': 1}), ('Giessen', 'Siegen', {'weight': 1}),
       ('Oldenburg', 'Wesel', {'weight': 1}), ('Norden', 'Wesel', {'weight': 1}), ('Leipzig', 'Berlin', {'weight': 1}),
       ('Dresden', 'Berlin', {'weight': 1}), ('Schwerin', 'Berlin', {'weight': 1}),
       ('Magdeburg', 'Berlin', {'weight': 1}), ('Greifswald', 'Berlin', {'weight': 1}),
       ('Dresden', 'Leipzig', {'weight': 1}), ('Erfurt', 'Leipzig', {'weight': 1}),
       ('Magdeburg', 'Leipzig', {'weight': 1}), ('Bayreuth', 'Leipzig', {'weight': 1}),
       ('Erfurt', 'Dresden', {'weight': 1}), ('Chemnitz', 'Dresden', {'weight': 1}),
       ('Chemnitz', 'Erfurt', {'weight': 1}), ('Kassel', 'Erfurt', {'weight': 1}),
       ('Wuerzburg', 'Erfurt', {'weight': 1}), ('Bayreuth', 'Chemnitz', {'weight': 1}),
       ('Magdeburg', 'Schwerin', {'weight': 1}), ('Greifswald', 'Schwerin', {'weight': 1}),
       ('Hamburg', 'Schwerin', {'weight': 1}), ('Kiel', 'Schwerin', {'weight': 1}),
       ('Braunschweig', 'Magdeburg', {'weight': 1}), ('Kiel', 'Hamburg', {'weight': 1}),
       ('Hannover', 'Hamburg', {'weight': 1}), ('Braunschweig', 'Hamburg', {'weight': 1}),
       ('Oldenburg', 'Bremen', {'weight': 1}), ('Bremerhaven', 'Bremen', {'weight': 1}),
       ('Hannover', 'Bremen', {'weight': 1}), ('Flensburg', 'Kiel', {'weight': 1}),
       ('Norden', 'Oldenburg', {'weight': 1}), ('Osnabrueck', 'Oldenburg', {'weight': 1}),
       ('Bremerhaven', 'Flensburg', {'weight': 1}), ('Bielefeld', 'Hannover', {'weight': 1}),
       ('Braunschweig', 'Hannover', {'weight': 1}), ('Osnabrueck', 'Hannover', {'weight': 1}),
       ('Braunschweig', 'Bielefeld', {'weight': 1}), ('Kassel', 'Braunschweig', {'weight': 1}),
       ('Giessen', 'Kassel', {'weight': 1}), ('Fulda', 'Kassel', {'weight': 1}),
       ('Darmstadt', 'Frankfurt', {'weight': 1}), ('Giessen', 'Frankfurt', {'weight': 1}),
       ('Fulda', 'Frankfurt', {'weight': 1}), ('Mannheim', 'Darmstadt', {'weight': 1}),
       ('Kaiserslautern', 'Darmstadt', {'weight': 1}), ('Karlsruhe', 'Mannheim', {'weight': 1}),
       ('Saarbruecken', 'Kaiserslautern', {'weight': 1}), ('Karlsruhe', 'Kaiserslautern', {'weight': 1}),
       ('Fulda', 'Giessen', {'weight': 1}), ('Saarbruecken', 'Trier', {'weight': 1}),
       ('Wuerzburg', 'Fulda', {'weight': 1}), ('Karlsruhe', 'Saarbruecken', {'weight': 1}),
       ('Karlsruhe', 'Stuttgart', {'weight': 1}), ('Ulm', 'Stuttgart', {'weight': 1}),
       ('Konstanz', 'Stuttgart', {'weight': 1}), ('Wuerzburg', 'Stuttgart', {'weight': 1}),
       ('Freiburg', 'Karlsruhe', {'weight': 1}), ('Augsburg', 'Ulm', {'weight': 1}),
       ('Freiburg', 'Konstanz', {'weight': 1}), ('Kempten', 'Konstanz', {'weight': 1}),
       ('Augsburg', 'Muenchen', {'weight': 1}), ('Kempten', 'Muenchen', {'weight': 1}),
       ('Passau', 'Muenchen', {'weight': 1}), ('Nuernberg', 'Muenchen', {'weight': 1}),
       ('Regensburg', 'Muenchen', {'weight': 1}), ('Wuerzburg', 'Augsburg', {'weight': 1}),
       ('Regensburg', 'Passau', {'weight': 1}), ('Bayreuth', 'Nuernberg', {'weight': 1}),
       ('Wuerzburg', 'Nuernberg', {'weight': 1}), ('Regensburg', 'Nuernberg', {'weight': 1})])



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
