import itertools
import time

import networkx as nx
from matplotlib import pyplot as plt

import main

# graph 1  world 100 nodes

terminals = 30
color_map = []

G1 = nx.Graph()

G1.add_nodes_from(
    ["Abilene", "Albany", "Albuquerque", "Atlanta", "Austin", "Baltimore", "Baton_Rouge", "Billings", "Birmingham",
     "Bismarck", "Boston", "Buffalo", "Charleston", "Charlotte", "Chicago", "Cincinnati", "Cleveland", "Columbus",
     "Dallas", "Denver", "Detroit", "El_Paso", "Fresno", "Greensboro", "Hartford", "Houston", "Jacksonville",
     "Kansas_City", "Las_Vegas", "Little_Rock", "Long_Island", "Los_Angeles", "Louisville", "Memphis", "Miami",
     "Milwaukee", "Minneapolis", "Nashville", "New_Orleans", "New_York", "Newark", "Norfolk", "Oakland",
     "Oklahoma_City", "Omaha", "Orlando", "Philadelphia", "Phoenix", "Pittsburgh", "Portland", "Providence",
     "Raleigh", "Richmond", "Rochester", "Sacramento", "Salt_Lake_City", "San_Antonio", "San_Diego",
     "San_Francisco", "San_Jose", "Santa_Barbara", "Scranton", "Seattle", "Spokane", "Springfield", "St_Louis",
     "Syracuse", "Tallahassee", "Tampa", "Toledo", "Tucson", "Tulsa", "Washington_DC", "West_Palm_Beach",
     "Wilmington", "Amsterdam", "Berlin", "Brussels", "Bucharest", "Frankfurt", "Istanbul", "London", "Madrid",
     "Paris", "Rome", "Vienna", "Warsaw", "Zurich", "Bangkok", "Beijing", "Delhi", "Hong_Kong", "Honolulu", "Mumbai",
     "Seoul", "Shanghai", "Singapore", "Sydney", "Taipei", "Tokyo"])

pos_G1 = {"Abilene": (32.45, -99.739998),
          "Albany": (42.6699982, -73.8000029),
          "Albuquerque": (35.119977, -106.61997),
          "Atlanta": (33.7599982, -84.4199987),
          "Austin": (30.3099988, -97.7500018),
          "Baltimore": (39.2999992, -76.6100008),
          "Baton_Rouge": (30.4499996, -91.1299968),
          "Billings": (45.79000104, -108.5400006),
          "Birmingham": (33.5299985, -86.8000029),
          "Bismarck": (46.81000154, -100.7699965),
          "Boston": (42.3400005, -71.0199959),
          "Buffalo": (42.8899993, -78.860001),
          "Charleston": (32.7900008, -79.9899982),
          "Charlotte": (35.2, -80.83),
          "Chicago": (41.839997, -87.680001),
          "Cincinnati": (39.1399991, -84.5100027),
          "Cleveland": (41.4799992, -81.6800014),
          "Columbus": (39.990002, -82.989997),
          "Dallas": (32.79, -96.77),
          "Denver": (39.77000271, -104.8700036),
          "Detroit": (42.3800019, -83.0999998),
          "El_Paso": (31.84981, -106.4396),
          "Fresno": (36.7800007, -119.790002),
          "Greensboro": (36.0800024, -79.8300018),
          "Hartford": (41.7700004, -72.6800003),
          "Houston": (29.77, -95.39),
          "Jacksonville": (30.330003, -81.660002),
          "Kansas_City": (39.1199992, -94.7300038),
          "Las_Vegas": (36.20999, -115.2199),
          "Little_Rock": (34.72, -92.35),
          "Long_Island": (40.5899999, -73.6699993),
          "Los_Angeles": (34.110001, -118.410002),
          "Louisville": (38.2200009, -85.7399979),
          "Memphis": (35.110001, -90.010004),
          "Miami": (25.7800006, -80.2099997),
          "Milwaukee": (43.0600013, -87.9700005),
          "Minneapolis": (44.9599988, -93.2699973),
          "Nashville": (36.1699984, -86.7799989),
          "New_Orleans": (30.07, -89.93),
          "New_York": (40.6699983, -73.9400035),
          "Newark": (40.7200012, -74.1699986),
          "Norfolk": (36.9199982, -76.2399978),
          "Oakland": (37.77000071, -122.2200016),
          "Oklahoma_City": (35.4700015, -97.5100028),
          "Omaha": (41.2599984, -96.0100022),
          "Orlando": (28.4999994, -81.370003),
          "Philadelphia": (40.0099985, -75.1299964),
          "Phoenix": (33.54000058, -112.0699996),
          "Pittsburgh": (40.3, -80.13),
          "Portland": (45.54000072, -122.6600035),
          "Providence": (41.82, -71.42),
          "Raleigh": (35.8199995, -78.6600034),
          "Richmond": (37.5299986, -77.4700015),
          "Rochester": (43.1699985, -77.620003),
          "Sacramento": (38.56999946, -121.4700016),
          "Salt_Lake_City": (40.77999863, -111.9300007),
          "San_Antonio": (29.459997, -98.510002),
          "San_Diego": (32.8100017, -117.139999),
          "San_Francisco": (37.65999942, -122.4199987),
          "San_Jose": (37.29999947, -121.8499985),
          "Santa_Barbara": (34.43000021, -119.7200014),
          "Scranton": (41.4, -75.67),
          "Seattle": (47.61999916, -122.3499985),
          "Spokane": (47.66999805, -117.4100038),
          "Springfield": (39.5, -89.4),
          "St_Louis": (38.64, -90.24),
          "Syracuse": (43.040001, -76.1399993),
          "Tallahassee": (30.46, -84.28),
          "Tampa": (27.9599988, -82.4800035),
          "Toledo": (41.659997, -83.58),
          "Tucson": (32.2, -110.89),
          "Tulsa": (36.13, -95.92),
          "Washington_DC": (38.9100003, -77.0199965),
          "West_Palm_Beach": (26.7499997, -80.1299975),
          "Wilmington": (39.7400018, -75.5299989),
          "Amsterdam": (52.3699996, 4.88999915),
          "Berlin": (52.520002, 13.379995),
          "Brussels": (50.830002, 4.330002),
          "Bucharest": (44.44, 26.1),
          "Frankfurt": (50.1199992, 8.68000104),
          "Istanbul": (41.1, 29),
          "London": (51.5200005, -0.100000296),
          "Madrid": (40.419998, -3.7100002),
          "Paris": (48.86, 2.3399995),
          "Rome": (41.8899996, 12.5000004),
          "Vienna": (48.2200024, 16.3700005),
          "Warsaw": (52.2599987, 21.0200005),
          "Zurich": (47.3800015, 8.5399996),
          "Bangkok": (13.73, 100.5),
          "Beijing": (39.92999979, 116.4000013),
          "Delhi": (28.6700003, 77.2099989),
          "Hong_Kong": (22.267, 114.14),
          "Honolulu": (21.3199996, -157.800003),
          "Mumbai": (18.9599987, 72.8199999),
          "Seoul": (37.56000108, 126.9899988),
          "Shanghai": (31.23, 121.47),
          "Singapore": (1.299999907, 103.8499992),
          "Sydney": (-33.86999896, 151.2100066),
          "Taipei": (25.0200005, 121.449997),
          "Tokyo": (35.6699986, 139.770004)}

G1.add_edges_from(
    [('Abilene', 'Dallas', {'weight': 1}), ('Abilene', 'El_Paso', {'weight': 1}), ('Albany', 'Boston', {'weight': 1}),
     ('Albany', 'Syracuse', {'weight': 1}), ('Albuquerque', 'Dallas', {'weight': 1}),
     ('Albuquerque', 'Denver', {'weight': 1}), ('Albuquerque', 'El_Paso', {'weight': 1}),
     ('Albuquerque', 'Las_Vegas', {'weight': 1}), ('Amsterdam', 'Berlin', {'weight': 1}),
     ('Amsterdam', 'Brussels', {'weight': 1}), ('Amsterdam', 'Frankfurt', {'weight': 1}),
     ('Amsterdam', 'New_York', {'weight': 1}), ('Atlanta', 'Birmingham', {'weight': 1}),
     ('Atlanta', 'Charlotte', {'weight': 1}), ('Atlanta', 'Jacksonville', {'weight': 1}),
     ('Austin', 'Houston', {'weight': 1}), ('Austin', 'San_Antonio', {'weight': 1}),
     ('Baltimore', 'Philadelphia', {'weight': 1}), ('Baltimore', 'Pittsburgh', {'weight': 1}),
     ('Baltimore', 'Washington_DC', {'weight': 1}), ('Bangkok', 'Delhi', {'weight': 1}),
     ('Bangkok', 'Hong_Kong', {'weight': 1}), ('Baton_Rouge', 'Houston', {'weight': 1}),
     ('Baton_Rouge', 'New_Orleans', {'weight': 1}), ('Beijing', 'Seoul', {'weight': 1}),
     ('Beijing', 'Shanghai', {'weight': 1}), ('Berlin', 'Warsaw', {'weight': 1}),
     ('Billings', 'Bismarck', {'weight': 1}), ('Billings', 'Denver', {'weight': 1}),
     ('Billings', 'Spokane', {'weight': 1}), ('Birmingham', 'Nashville', {'weight': 1}),
     ('Birmingham', 'New_Orleans', {'weight': 1}), ('Bismarck', 'Minneapolis', {'weight': 1}),
     ('Boston', 'Providence', {'weight': 1}), ('Brussels', 'London', {'weight': 1}),
     ('Bucharest', 'Istanbul', {'weight': 1}), ('Bucharest', 'Warsaw', {'weight': 1}),
     ('Buffalo', 'Cleveland', {'weight': 1}), ('Buffalo', 'Rochester', {'weight': 1}),
     ('Charleston', 'Jacksonville', {'weight': 1}), ('Charleston', 'Raleigh', {'weight': 1}),
     ('Charlotte', 'Greensboro', {'weight': 1}), ('Chicago', 'Detroit', {'weight': 1}),
     ('Chicago', 'Milwaukee', {'weight': 1}), ('Chicago', 'Springfield', {'weight': 1}),
     ('Cincinnati', 'Columbus', {'weight': 1}), ('Cincinnati', 'Louisville', {'weight': 1}),
     ('Cincinnati', 'Washington_DC', {'weight': 1}), ('Cleveland', 'Columbus', {'weight': 1}),
     ('Cleveland', 'Toledo', {'weight': 1}), ('Columbus', 'Pittsburgh', {'weight': 1}),
     ('Dallas', 'Houston', {'weight': 1}), ('Dallas', 'Little_Rock', {'weight': 1}),
     ('Dallas', 'Oklahoma_City', {'weight': 1}), ('Delhi', 'Istanbul', {'weight': 1}),
     ('Delhi', 'Mumbai', {'weight': 1}), ('Denver', 'Omaha', {'weight': 1}),
     ('Denver', 'Salt_Lake_City', {'weight': 1}), ('Detroit', 'Toledo', {'weight': 1}),
     ('El_Paso', 'San_Antonio', {'weight': 1}), ('El_Paso', 'Tucson', {'weight': 1}),
     ('Frankfurt', 'Vienna', {'weight': 1}), ('Fresno', 'Las_Vegas', {'weight': 1}),
     ('Fresno', 'Los_Angeles', {'weight': 1}), ('Fresno', 'Oakland', {'weight': 1}),
     ('Greensboro', 'Louisville', {'weight': 1}), ('Greensboro', 'Raleigh', {'weight': 1}),
     ('Greensboro', 'Richmond', {'weight': 1}), ('Hartford', 'Long_Island', {'weight': 1}),
     ('Hartford', 'Providence', {'weight': 1}), ('Hong_Kong', 'Shanghai', {'weight': 1}),
     ('Hong_Kong', 'Sydney', {'weight': 1}), ('Hong_Kong', 'Taipei', {'weight': 1}),
     ('Honolulu', 'Los_Angeles', {'weight': 1}), ('Honolulu', 'Sydney', {'weight': 1}),
     ('Honolulu', 'Taipei', {'weight': 1}), ('Istanbul', 'Rome', {'weight': 1}),
     ('Jacksonville', 'Orlando', {'weight': 1}), ('Kansas_City', 'Omaha', {'weight': 1}),
     ('Kansas_City', 'St_Louis', {'weight': 1}), ('Kansas_City', 'Tulsa', {'weight': 1}),
     ('Las_Vegas', 'Phoenix', {'weight': 1}), ('Las_Vegas', 'Salt_Lake_City', {'weight': 1}),
     ('Little_Rock', 'Memphis', {'weight': 1}), ('London', 'Paris', {'weight': 1}),
     ('London', 'Washington_DC', {'weight': 1}), ('Long_Island', 'New_York', {'weight': 1}),
     ('Los_Angeles', 'San_Diego', {'weight': 1}), ('Los_Angeles', 'Santa_Barbara', {'weight': 1}),
     ('Louisville', 'Nashville', {'weight': 1}), ('Louisville', 'St_Louis', {'weight': 1}),
     ('Madrid', 'Paris', {'weight': 1}), ('Madrid', 'Zurich', {'weight': 1}), ('Memphis', 'Nashville', {'weight': 1}),
     ('Miami', 'Paris', {'weight': 1}), ('Miami', 'Tampa', {'weight': 1}),
     ('Miami', 'West_Palm_Beach', {'weight': 1}), ('Milwaukee', 'Minneapolis', {'weight': 1}),
     ('Minneapolis', 'Omaha', {'weight': 1}), ('Mumbai', 'Rome', {'weight': 1}),
     ('Mumbai', 'Singapore', {'weight': 1}), ('New_Orleans', 'Tallahassee', {'weight': 1}),
     ('New_York', 'Newark', {'weight': 1}), ('New_York', 'Scranton', {'weight': 1}),
     ('New_York', 'Wilmington', {'weight': 1}), ('Newark', 'Philadelphia', {'weight': 1}),
     ('Norfolk', 'Raleigh', {'weight': 1}), ('Norfolk', 'Wilmington', {'weight': 1}),
     ('Oakland', 'Sacramento', {'weight': 1}), ('Oakland', 'Salt_Lake_City', {'weight': 1}),
     ('Oakland', 'San_Francisco', {'weight': 1}), ('Oakland', 'Taipei', {'weight': 1}),
     ('Oklahoma_City', 'Tulsa', {'weight': 1}), ('Orlando', 'West_Palm_Beach', {'weight': 1}),
     ('Philadelphia', 'Scranton', {'weight': 1}), ('Phoenix', 'San_Diego', {'weight': 1}),
     ('Phoenix', 'Tucson', {'weight': 1}), ('Pittsburgh', 'Scranton', {'weight': 1}),
     ('Portland', 'Sacramento', {'weight': 1}), ('Portland', 'Salt_Lake_City', {'weight': 1}),
     ('Portland', 'Seattle', {'weight': 1}), ('Portland', 'Tokyo', {'weight': 1}),
     ('Richmond', 'Washington_DC', {'weight': 1}), ('Rochester', 'Syracuse', {'weight': 1}),
     ('Rome', 'Vienna', {'weight': 1}), ('Rome', 'Zurich', {'weight': 1}),
     ('San_Francisco', 'San_Jose', {'weight': 1}), ('San_Jose', 'Santa_Barbara', {'weight': 1}),
     ('Scranton', 'Syracuse', {'weight': 1}), ('Seattle', 'Spokane', {'weight': 1}),
     ('Seoul', 'Tokyo', {'weight': 1}), ('Singapore', 'Sydney', {'weight': 1}),
     ('Springfield', 'St_Louis', {'weight': 1}), ('Taipei', 'Tokyo', {'weight': 1}),
     ('Tallahassee', 'Tampa', {'weight': 1}), ('Vienna', 'Warsaw', {'weight': 1})])

for i in range(0, len(G1)):
    if i < terminals:
        color_map.append('red')
    else:
        color_map.append('blue')
nx.draw(G1, node_color=color_map, node_size=200, pos=pos_G1, with_labels=True)
plt.show()

G = nx.convert_node_labels_to_integers(G1, first_label=0, ordering='default', label_attribute=None)
terminal_nodes = list(G)[0:terminals]

i = 0
for key in pos_G1.copy():
    pos_G1[i] = pos_G1.pop(key)
    i = i + 1
nx.draw(G, node_color=color_map, node_size=200, pos=pos_G1, with_labels=True)
plt.show()

main.sph(G, pos_G1, terminals)
main.algorithm(G, pos_G1, terminals)
main.algorithm2(G, pos_G1, terminals)
main.algorithm3(G, pos_G1, terminals)
print("-------------------------")
