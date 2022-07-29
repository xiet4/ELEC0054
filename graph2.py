import networkx as nx
from matplotlib import pyplot as plt
from networkx.algorithms.approximation import steiner_tree

import main

# graph 2  USA 75 nodes

terminals = 30
color_map = []

G2 = nx.Graph()

G2.add_nodes_from(
    ["Abilene", "Albany", "Albuquerque", "Atlanta", "Austin", "Baltimore", "Baton_Rouge", "Billings", "Birmingham",
     "Bismarck", "Boston", "Buffalo", "Charleston", "Charlotte", "Chicago", "Cincinnati", "Cleveland", "Columbus",
     "Dallas", "Denver", "Detroit", "El_Paso", "Fresno", "Greensboro", "Hartford", "Houston", "Jacksonville",
     "Kansas_City", "Las_Vegas", "Little_Rock", "Long_Island", "Los_Angeles", "Louisville", "Memphis",
     "Miami", "Milwaukee", "Minneapolis", "Nashville", "New_Orleans", "New_York", "Newark", "Norfolk", "Oakland",
     "Oklahoma_City", "Omaha", "Orlando", "Philadelphia", "Phoenix", "Pittsburgh", "Portland", "Providence",
     "Raleigh", "Richmond", "Rochester", "Sacramento", "Salt_Lake_City", "San_Antonio", "San_Diego", "San_Francisco",
     "San_Jose", "Santa_Barbara", "Scranton", "Seattle", "Spokane", "Springfield", "St_Louis", "Syracuse",
     "Tallahassee", "Tampa", "Toledo", "Tucson", "Tulsa", "Washington_DC", "West_Palm_Beach", "Wilmington"])

pos_G2 = {"Abilene": (-99.7, 32.5),
          "Albany": (-73.8, 42.6),
          "Albuquerque": (-106.6, 35.1),
          "Atlanta": (-84.4, 33.8),
          "Austin": (-97.8, 30.3),
          "Baltimore": (-76.6, 39.3),
          "Baton_Rouge": (-91.1, 30.4),
          "Billings": (-108.5, 45.8),
          "Birmingham": (-86.8, 33.5),
          "Bismarck": (-100.8, 46.8),
          "Boston": (-71.1, 46.8),
          "Buffalo": (-78.9, 42.9),
          "Charleston": (-80.0, 32.8),
          "Charlotte": (-80.8, 35.2),
          "Chicago": (-87.7, 41.8),
          "Cincinnati": (-84.5, 39.1),
          "Cleveland": (-81.7, 41.5),
          "Columbus": (-83.0, 40.0),
          "Dallas": (-96.8, 32.8),
          "Denver": (-104.9, 39.8),
          "Detroit": (-83.1, 42.4),
          "El_Paso": (-106.4, 31.4),
          "Fresno": (-119.8, 36.8),
          "Greensboro": (-79.8, 36.1),
          "Hartford": (-72.7, 41.8),
          "Houston": (-95.4, 29.8),
          "Jacksonville": (-81.7, 30.3),
          "Kansas_City": (-94.7, 39.1),
          "Las_Vegas": (-115.2, 36.2),
          "Little_Rock": (-92.4, 34.7),
          "Long_Island": (-73.7, 40.6),
          "Los_Angeles": (-118.4, 34.1),
          "Louisville": (-85.7, 38.3),
          "Memphis": (-90.0, 35.1),
          "Miami": (-80.2, 25.8),
          "Milwaukee": (-88.0, 43.1),
          "Minneapolis": (-93.3, 45.0),
          "Nashville": (-86.8, 36.2),
          "New_Orleans": (-90.0, 30.0),
          "New_York": (-74.0, 40.7),
          "Newark": (-74.2, 40.7),
          "Norfolk": (-76.2, 37.0),
          "Oakland": (-122.2, 37.8),
          "Oklahoma_City": (-97.5, 35.4),
          "Omaha": (-96.0, 41.3),
          "Orlando": (-81.4, 28.5),
          "Philadelphia": (-75.1, 40.0),
          "Phoenix": (-112.1, 33.5),
          "Pittsburgh": (-80.1, 40.3),
          "Portland": (-122.7, 45.5),
          "Providence": (-71.4, 41.8),
          "Raleigh": (-78.7, 35.8),
          "Richmond": (-77.4, 37.5),
          "Rochester": (-77.6, 43.1),
          "Sacramento": (-121.5, 38.7),
          "Salt_Lake_City": (-111.9, 40.8),
          "San_Antonio": (-98.5, 29.5),
          "San_Diego": (-117.1, 32.8),
          "San_Francisco": (-122.4, 37.7),
          "San_Jose": (-121.8, 37.3),
          "Santa_Barbara": (-119.7, 34.4),
          "Scranton": (-75.7, 41.4),
          "Seattle": (-122.3, 47.6),
          "Spokane": (-117.4, 47.7),
          "Springfield": (-89.4, 39.5),
          "St_Louis": (-90.2, 38.6),
          "Syracuse": (-76.1, 43.0),
          "Tallahassee": (-84.3, 30.5),
          "Tampa": (-82.5, 28.0),
          "Toledo": (-83.6, 41.7),
          "Tucson": (-110.9, 32.2),
          "Tulsa": (-95.9, 36.1),
          "Washington_DC": (-77.0, 38.9),
          "West_Palm_Beach": (-80.1, 26.7),
          "Wilmington": (-75.5, 39.7)}

G2.add_edges_from([('Abilene', 'Dallas', {'weight': 1}), ('Abilene', 'El_Paso', {'weight': 1}), ('Albany', 'Boston', {'weight': 1}),
       ('Albany', 'Syracuse', {'weight': 1}), ('Albuquerque', 'Dallas', {'weight': 1}),
       ('Albuquerque', 'Denver', {'weight': 1}), ('Albuquerque', 'El_Paso', {'weight': 1}),
       ('Albuquerque', 'Las_Vegas', {'weight': 1}), ('Atlanta', 'Birmingham', {'weight': 1}),
       ('Atlanta', 'Charlotte', {'weight': 1}), ('Atlanta', 'Jacksonville', {'weight': 1}),
       ('Austin', 'Houston', {'weight': 1}), ('Austin', 'San_Antonio', {'weight': 1}),
       ('Baltimore', 'Philadelphia', {'weight': 1}), ('Baltimore', 'Pittsburgh', {'weight': 1}),
       ('Baltimore', 'Washington_DC', {'weight': 1}), ('Baton_Rouge', 'Houston', {'weight': 1}),
       ('Baton_Rouge', 'New_Orleans', {'weight': 1}), ('Billings', 'Bismarck', {'weight': 1}),
       ('Billings', 'Denver', {'weight': 1}), ('Billings', 'Spokane', {'weight': 1}),
       ('Birmingham', 'Nashville', {'weight': 1}), ('Birmingham', 'New_Orleans', {'weight': 1}),
       ('Bismarck', 'Minneapolis', {'weight': 1}), ('Boston', 'Providence', {'weight': 1}),
       ('Buffalo', 'Cleveland', {'weight': 1}), ('Buffalo', 'Rochester', {'weight': 1}),
       ('Charleston', 'Jacksonville', {'weight': 1}), ('Charleston', 'Raleigh', {'weight': 1}),
       ('Charlotte', 'Greensboro', {'weight': 1}), ('Chicago', 'Detroit', {'weight': 1}),
       ('Chicago', 'Milwaukee', {'weight': 1}), ('Chicago', 'Springfield', {'weight': 1}),
       ('Cincinnati', 'Columbus', {'weight': 1}), ('Cincinnati', 'Louisville', {'weight': 1}),
       ('Cincinnati', 'Washington_DC', {'weight': 1}), ('Cleveland', 'Columbus', {'weight': 1}),
       ('Cleveland', 'Toledo', {'weight': 1}), ('Columbus', 'Pittsburgh', {'weight': 1}),
       ('Dallas', 'Houston', {'weight': 1}), ('Dallas', 'Little_Rock', {'weight': 1}),
       ('Dallas', 'Oklahoma_City', {'weight': 1}), ('Denver', 'Omaha', {'weight': 1}),
       ('Denver', 'Salt_Lake_City', {'weight': 1}), ('Detroit', 'Toledo', {'weight': 1}),
       ('El_Paso', 'San_Antonio', {'weight': 1}), ('El_Paso', 'Tucson', {'weight': 1}),
       ('Fresno', 'Las_Vegas', {'weight': 1}), ('Fresno', 'Los_Angeles', {'weight': 1}),
       ('Fresno', 'Oakland', {'weight': 1}), ('Greensboro', 'Louisville', {'weight': 1}),
       ('Greensboro', 'Raleigh', {'weight': 1}), ('Greensboro', 'Richmond', {'weight': 1}),
       ('Hartford', 'Long_Island', {'weight': 1}), ('Hartford', 'Providence', {'weight': 1}),
       ('Jacksonville', 'Orlando', {'weight': 1}), ('Kansas_City', 'Omaha', {'weight': 1}),
       ('Kansas_City', 'St_Louis', {'weight': 1}), ('Kansas_City', 'Tulsa', {'weight': 1}),
       ('Las_Vegas', 'Phoenix', {'weight': 1}), ('Las_Vegas', 'Salt_Lake_City', {'weight': 1}),
       ('Little_Rock', 'Memphis', {'weight': 1}), ('Long_Island', 'New_York', {'weight': 1}),
       ('Los_Angeles', 'San_Diego', {'weight': 1}), ('Los_Angeles', 'Santa_Barbara', {'weight': 1}),
       ('Louisville', 'Nashville', {'weight': 1}), ('Louisville', 'St_Louis', {'weight': 1}),
       ('Memphis', 'Nashville', {'weight': 1}), ('Miami', 'Tampa', {'weight': 1}),
       ('Miami', 'West_Palm_Beach', {'weight': 1}), ('Milwaukee', 'Minneapolis', {'weight': 1}),
       ('Minneapolis', 'Omaha', {'weight': 1}), ('New_Orleans', 'Tallahassee', {'weight': 1}),
       ('New_York', 'Newark', {'weight': 1}), ('New_York', 'Scranton', {'weight': 1}),
       ('New_York', 'Wilmington', {'weight': 1}), ('Newark', 'Philadelphia', {'weight': 1}),
       ('Norfolk', 'Raleigh', {'weight': 1}), ('Norfolk', 'Wilmington', {'weight': 1}),
       ('Oakland', 'Sacramento', {'weight': 1}), ('Oakland', 'Salt_Lake_City', {'weight': 1}),
       ('Oakland', 'San_Francisco', {'weight': 1}), ('Oklahoma_City', 'Tulsa', {'weight': 1}),
       ('Orlando', 'West_Palm_Beach', {'weight': 1}), ('Philadelphia', 'Scranton', {'weight': 1}),
       ('Phoenix', 'San_Diego', {'weight': 1}), ('Phoenix', 'Tucson', {'weight': 1}),
       ('Pittsburgh', 'Scranton', {'weight': 1}), ('Portland', 'Sacramento', {'weight': 1}),
       ('Portland', 'Salt_Lake_City', {'weight': 1}), ('Portland', 'Seattle', {'weight': 1}),
       ('Richmond', 'Washington_DC', {'weight': 1}), ('Rochester', 'Syracuse', {'weight': 1}),
       ('San_Francisco', 'San_Jose', {'weight': 1}), ('San_Jose', 'Santa_Barbara', {'weight': 1}),
       ('Scranton', 'Syracuse', {'weight': 1}), ('Seattle', 'Spokane', {'weight': 1}),
       ('Springfield', 'St_Louis', {'weight': 1}), ('Tallahassee', 'Tampa', {'weight': 1})])


for i in range(0, len(G2)):
    if i < terminals:
        color_map.append('red')
    else:
        color_map.append('blue')
nx.draw(G2, node_color=color_map, node_size=200, pos=pos_G2, with_labels=True)
plt.show()

G = nx.convert_node_labels_to_integers(G2, first_label=0, ordering='default', label_attribute=None)
terminal_nodes = list(G)[0:terminals]
main.sph(G, pos_G2, terminals)
main.algorithm(G, pos_G2, terminals)
main.algorithm2(G, pos_G2, terminals)
main.algorithm3(G, pos_G2, terminals)
print("-------------------------")