import networkx as nx
from matplotlib import pyplot as plt
from networkx.algorithms.approximation import steiner_tree

import main

# graph 1  world 100 nodes

terminals = 60
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

G1.add_edges_from([
    ("Abilene", "Dallas", {"weight": 336.9509334}),
    ("Abilene", "El_Paso", {"weight": 761.2090776}),
    ("Albany", "Boston", {"weight": 277.0649613}),
    ("Albany", "Syracuse", {"weight": 234.2212201}),
    ("Albuquerque", "Dallas", {"weight": 1133.443119}),
    ("Albuquerque", "Denver", {"weight": 647.7371779}),
    ("Albuquerque", "El_Paso", {"weight": 436.9494668}),
    ("Albuquerque", "Las_Vegas", {"weight": 943.5364333}),
    ("Amsterdam", "Berlin", {"weight": 690.6082921}),
    ("Amsterdam", "Brussels", {"weight": 210.7287967}),
    ("Amsterdam", "Frankfurt", {"weight": 436.3242408}),
    ("Amsterdam", "New_York", {"weight": 7035.611036}),
    ("Atlanta", "Birmingham", {"weight": 266.2280948}),
    ("Atlanta", "Charlotte", {"weight": 439.2379644}),
    ("Atlanta", "Jacksonville", {"weight": 554.1108875}),
    ("Austin", "Houston", {"weight": 282.0488176}),
    ("Austin", "San_Antonio", {"weight": 143.5525064}),
    ("Baltimore", "Philadelphia", {"weight": 179.1949651}),
    ("Baltimore", "Pittsburgh", {"weight": 384.8187539}),
    ("Baltimore", "Washington_DC", {"weight": 67.17947405}),
    ("Bangkok", "Delhi", {"weight": 3505.949664}),
    ("Bangkok", "Hong_Kong", {"weight": 2070.724162}),
    ("Baton_Rouge", "Houston", {"weight": 500.1517957}),
    ("Baton_Rouge", "New_Orleans", {"weight": 147.3504058}),
    ("Beijing", "Seoul", {"weight": 1146.124217}),
    ("Beijing", "Shanghai", {"weight": 1284.465391}),
    ("Berlin", "Warsaw", {"weight": 623.0146936}),
    ("Billings", "Bismarck", {"weight": 729.0170987}),
    ("Billings", "Denver", {"weight": 880.041712}),
    ("Billings", "Spokane", {"weight": 848.8579799}),
    ("Birmingham", "Nashville", {"weight": 352.382908}),
    ("Birmingham", "New_Orleans", {"weight": 582.4644304}),
    ("Bismarck", "Minneapolis", {"weight": 738.9401642}),
    ("Boston", "Providence", {"weight": 79.92293577}),
    ("Brussels", "London", {"weight": 381.9130127}),
    ("Bucharest", "Istanbul", {"weight": 528.5804935}),
    ("Bucharest", "Warsaw", {"weight": 1136.200456}),
    ("Buffalo", "Cleveland", {"weight": 336.4337393}),
    ("Buffalo", "Rochester", {"weight": 126.6263824}),
    ("Charleston", "Jacksonville", {"weight": 379.311106}),
    ("Charleston", "Raleigh", {"weight": 430.1818131}),
    ("Charlotte", "Greensboro", {"weight": 159.8834469}),
    ("Chicago", "Detroit", {"weight": 459.1452686}),
    ("Chicago", "Milwaukee", {"weight": 165.3264805}),
    ("Chicago", "Springfield", {"weight": 357.5730073}),
    ("Cincinnati", "Columbus", {"weight": 193.2153767}),
    ("Cincinnati", "Louisville", {"weight": 177.4925816}),
    ("Cincinnati", "Washington_DC", {"weight": 777.0507392}),
    ("Cleveland", "Columbus", {"weight": 238.9630572}),
    ("Cleveland", "Toledo", {"weight": 191.2436294}),
    ("Columbus", "Pittsburgh", {"weight": 294.7135669}),
    ("Dallas", "Houston", {"weight": 432.7312491}),
    ("Dallas", "Little_Rock", {"weight": 553.9582807}),
    ("Dallas", "Oklahoma_City", {"weight": 366.9361351}),
    ("Delhi", "Istanbul", {"weight": 5457.525355}),
    ("Delhi", "Mumbai", {"weight": 1402.141042}),
    ("Denver", "Omaha", {"weight": 920.3373588}),
    ("Denver", "Salt_Lake_City", {"weight": 731.2717231}),
    ("Detroit", "Toledo", {"weight": 107.2436957}),
    ("El_Paso", "San_Antonio", {"weight": 964.4531908}),
    ("El_Paso", "Tucson", {"weight": 505.7485307}),
    ("Frankfurt", "Vienna", {"weight": 717.0013849}),
    ("Fresno", "Las_Vegas", {"weight": 496.1990407}),
    ("Fresno", "Los_Angeles", {"weight": 386.6707817}),
    ("Fresno", "Oakland", {"weight": 289.9410618}),
    ("Greensboro", "Louisville", {"weight": 690.4091794}),
    ("Greensboro", "Raleigh", {"weight": 131.0972102}),
    ("Greensboro", "Richmond", {"weight": 317.8965469}),
    ("Hartford", "Long_Island", {"weight": 186.2707622}),
    ("Hartford", "Providence", {"weight": 125.5599482}),
    ("Hong_Kong", "Shanghai", {"weight": 1480.405515}),
    ("Hong_Kong", "Sydney", {"weight": 8856.6}),
    ("Hong_Kong", "Taipei", {"weight": 966.1766739}),
    ("Honolulu", "Los_Angeles", {"weight": 4921.458828}),
    ("Honolulu", "Sydney", {"weight": 9808.615854}),
    ("Honolulu", "Taipei", {"weight": 9767.012902}),
    ("Istanbul", "Rome", {"weight": 1650.405834}),
    ("Jacksonville", "Orlando", {"weight": 246.5770348}),
    ("Kansas_City", "Omaha", {"weight": 314.0322058}),
    ("Kansas_City", "St_Louis", {"weight": 470.8657976}),
    ("Kansas_City", "Tulsa", {"weight": 418.4383844}),
    ("Las_Vegas", "Phoenix", {"weight": 495.9003239}),
    ("Las_Vegas", "Salt_Lake_City", {"weight": 700.0051286}),
    ("Little_Rock", "Memphis", {"weight": 261.3433471}),
    ("London", "Paris", {"weight": 411.6923734}),
    ("London", "Washington_DC", {"weight": 7079.44686}),
    ("Long_Island", "New_York", {"weight": 29.36152283}),
    ("Los_Angeles", "San_Diego", {"weight": 223.8445086}),
    ("Los_Angeles", "Santa_Barbara", {"weight": 150.6766134}),
    ("Louisville", "Nashville", {"weight": 295.1182142}),
    ("Louisville", "St_Louis", {"weight": 473.8016755}),
    ("Madrid", "Paris", {"weight": 1263.619232}),
    ("Madrid", "Zurich", {"weight": 1497.358313}),
    ("Memphis", "Nashville", {"weight": 377.8363294}),
    ("Miami", "Paris", {"weight": 8829.357704}),
    ("Miami", "Tampa", {"weight": 397.1149107}),
    ("Miami", "West_Palm_Beach", {"weight": 129.8250315}),
    ("Milwaukee", "Minneapolis", {"weight": 568.3338475}),
    ("Minneapolis", "Omaha", {"weight": 561.3270039}),
    ("Mumbai", "Rome", {"weight": 7415.84084}),
    ("Mumbai", "Singapore", {"weight": 4692.708049}),
    ("New_Orleans", "Tallahassee", {"weight": 653.3593336}),
    ("New_York", "Newark", {"weight": 24.21353477}),
    ("New_York", "Scranton", {"weight": 199.5750874}),
    ("New_York", "Wilmington", {"weight": 204.1516726}),
    ("Newark", "Philadelphia", {"weight": 136.0604521}),
    ("Norfolk", "Raleigh", {"weight": 298.6558234}),
    ("Norfolk", "Wilmington", {"weight": 383.6690534}),
    ("Oakland", "Sacramento", {"weight": 132.6490217}),
    ("Oakland", "Salt_Lake_City", {"weight": 1135.717402}),
    ("Oakland", "San_Francisco", {"weight": 25.71991716}),
    ("Oakland", "Taipei", {"weight": 12461.707}),
    ("Oklahoma_City", "Tulsa", {"weight": 193.3587768}),
    ("Orlando", "West_Palm_Beach", {"weight": 275.7928548}),
    ("Philadelphia", "Scranton", {"weight": 193.4089904}),
    ("Phoenix", "San_Diego", {"weight": 574.6750816}),
    ("Phoenix", "Tucson", {"weight": 222.4582756}),
    ("Pittsburgh", "Scranton", {"weight": 473.5653806}),
    ("Portland", "Sacramento", {"weight": 937.7404056}),
    ("Portland", "Salt_Lake_City", {"weight": 1221.189289}),
    ("Portland", "Seattle", {"weight": 279.0817311}),
    ("Portland", "Tokyo", {"weight": 9349.706225}),
    ("Richmond", "Washington_DC", {"weight": 190.1446685}),
    ("Rochester", "Syracuse", {"weight": 145.265921}),
    ("Rome", "Vienna", {"weight": 920.0256056}),
    ("Rome", "Zurich", {"weight": 823.3996782}),
    ("San_Francisco", "San_Jose", {"weight": 77.16267231}),
    ("San_Jose", "Santa_Barbara", {"weight": 446.9898708}),
    ("Scranton", "Syracuse", {"weight": 223.7750822}),
    ("Seattle", "Spokane", {"weight": 444.2069519}),
    ("Seoul", "Tokyo", {"weight": 1391.084532}),
    ("Singapore", "Sydney", {"weight": 7562.330522}),
    ("Springfield", "St_Louis", {"weight": 144.0599684}),
    ("Taipei", "Tokyo", {"weight": 2537.344602}),
    ("Tallahassee", "Tampa", {"weight": 394.0942686}),
    ("Vienna", "Warsaw", {"weight": 669.2971801})
])

for i in range(0, len(G1)):
    if i < terminals:
        color_map.append('red')
    else:
        color_map.append('blue')
nx.draw(G1, node_color=color_map, node_size=200, pos=pos_G1, with_labels=True)
plt.show()

G = nx.convert_node_labels_to_integers(G1, first_label=0, ordering='default', label_attribute=None)
terminal_nodes = list(G)[0:terminals]
print(steiner_tree(G, terminal_nodes))
main.algorithm(G, pos_G1, terminals)

# graph 2  USA 75 nodes

terminals = 50
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

G2.add_edges_from([
    ("Abilene", "Dallas", {"weight": 336.9509334}),
    ("Abilene", "El_Paso", {"weight": 761.2090776}),
    ("Albany", "Boston", {"weight": 277.649613}),
    ("Albany", "Syracuse", {"weight": 234.2212201}),
    ("Albuquerque", "Dallas", {"weight": 1133.443119}),
    ("Albuquerque", "Denver", {"weight": 647.7371779}),
    ("Albuquerque", "El_Paso", {"weight": 436.9494668}),
    ("Albuquerque", "Las_Vegas", {"weight": 943.5364333}),
    ("Atlanta", "Birmingham", {"weight": 266.2280948}),
    ("Atlanta", "Charlotte", {"weight": 439.279644}),
    ("Atlanta", "Jacksonville", {"weight": 554.1108875}),
    ("Austin", "Houston", {"weight": 282.0488176}),
    ("Austin", "San_Antonio", {"weight": 143.5525064}),
    ("Baltimore", "Philadelphia", {"weight": 179.1949651}),
    ("Baltimore", "Pittsburgh", {"weight": 384.8187539}),
    ("Baltimore", "Washington_DC", {"weight": 67.17947405}),
    ("Baton_Rouge", "Houston", {"weight": 500.1517957}),
    ("Baton_Rouge", "New_Orleans", {"weight": 147.3504058}),
    ("Billings", "Bismarck", {"weight": 729.0170987}),
    ("Billings", "Denver", {"weight": 880.041712}),
    ("Billings", "Spokane", {"weight": 848.8579799}),
    ("Birmingham", "Nashville", {"weight": 352.382908}),
    ("Birmingham", "New_Orleans", {"weight": 582.4644304}),
    ("Bismarck", "Minneapolis", {"weight": 738.9401642}),
    ("Boston", "Providence", {"weight": 79.92293577}),
    ("Buffalo", "Cleveland", {"weight": 336.4337393}),
    ("Buffalo", "Rochester", {"weight": 126.6263824}),
    ("Charleston", "Jacksonville", {"weight": 379.311106}),
    ("Charleston", "Raleigh", {"weight": 430.1818131}),
    ("Charlotte", "Greensboro", {"weight": 159.8834469}),
    ("Chicago", "Detroit", {"weight": 459.1452686}),
    ("Chicago", "Milwaukee", {"weight": 165.3264805}),
    ("Chicago", "Springfield", {"weight": 357.5730073}),
    ("Cincinnati", "Columbus", {"weight": 193.2153767}),
    ("Cincinnati", "Louisville", {"weight": 177.4925816}),
    ("Cincinnati", "Washington_DC", {"weight": 777.0507392}),
    ("Cleveland", "Columbus", {"weight": 238.9630572}),
    ("Cleveland", "Toledo", {"weight": 191.2436294}),
    ("Columbus", "Pittsburgh", {"weight": 294.7135669}),
    ("Dallas", "Houston", {"weight": 432.7312491}),
    ("Dallas", "Little_Rock", {"weight": 553.9582807}),
    ("Dallas", "Oklahoma_City", {"weight": 366.9361351}),
    ("Denver", "Omaha", {"weight": 920.3373588}),
    ("Denver", "Salt_Lake_City", {"weight": 731.2717231}),
    ("Detroit", "Toledo", {"weight": 107.2436957}),
    ("El_Paso", "San_Antonio", {"weight": 964.4531908}),
    ("El_Paso", "Tucson", {"weight": 505.7485307}),
    ("Fresno", "Las_Vegas", {"weight": 96.1990407}),
    ("Fresno", "Los_Angeles", {"weight": 386.6707817}),
    ("Fresno", "Oakland", {"weight": 289.9410618}),
    ("Greensboro", "Louisville", {"weight": 690.4091794}),
    ("Greensboro", "Raleigh", {"weight": 131.0972102}),
    ("Greensboro", "Richmond", {"weight": 317.8965469}),
    ("Hartford", "Long_Island", {"weight": 186.2707622}),
    ("Hartford", "Providence", {"weight": 125.5599482}),
    ("Jacksonville", "Orlando", {"weight": 246.5770348}),
    ("Kansas_City", "Omaha", {"weight": 314.0322058}),
    ("Kansas_City", "St_Louis", {"weight": 470.8657976}),
    ("Kansas_City", "Tulsa", {"weight": 418.4383844}),
    ("Las_Vegas", "Phoenix", {"weight": 495.9003239}),
    ("Las_Vegas", "Salt_Lake_City", {"weight": 700.0051286}),
    ("Little_Rock", "Memphis", {"weight": 261.3433471}),
    ("Long_Island", "New_York", {"weight": 29.36152283}),
    ("Los_Angeles", "San_Diego", {"weight": 223.8445086}),
    ("Los_Angeles", "Santa_Barbara", {"weight": 150.6766134}),
    ("Louisville", "Nashville", {"weight": 295.1182142}),
    ("Louisville", "St_Louis", {"weight": 473.8016755}),
    ("Memphis", "Nashville", {"weight": 377.8363294}),
    ("Miami", "Tampa", {"weight": 397.1149107}),
    ("Miami", "West_Palm_Beach", {"weight": 129.8250315}),
    ("Milwaukee", "Minneapolis", {"weight": 568.3338475}),
    ("Minneapolis", "Omaha", {"weight": 561.3270039}),
    ("New_Orleans", "Tallahassee", {"weight": 653.3593336}),
    ("New_York", "Newark", {"weight": 24.21353477}),
    ("New_York", "Scranton", {"weight": 199.5750874}),
    ("New_York", "Wilmington", {"weight": 204.1516726}),
    ("Newark", "Philadelphia", {"weight": 136.0604521}),
    ("Norfolk", "Raleigh", {"weight": 298.6558234}),
    ("Norfolk", "Wilmington", {"weight": 383.6690534}),
    ("Oakland", "Sacramento", {"weight": 132.6490217}),
    ("Oakland", "Salt_Lake_City", {"weight": 1135.717402}),
    ("Oakland", "San_Francisco", {"weight": 25.71991716}),
    ("Oklahoma_City", "Tulsa", {"weight": 193.3587768}),
    ("Orlando", "West_Palm_Beach", {"weight": 275.7928548}),
    ("Philadelphia", "Scranton", {"weight": 193.4089904}),
    ("Phoenix", "San_Diego", {"weight": 574.6750816}),
    ("Phoenix", "Tucson", {"weight": 222.4582756}),
    ("Pittsburgh", "Scranton", {"weight": 473.5653806}),
    ("Portland", "Sacramento", {"weight": 937.7404056}),
    ("Portland", "Salt_Lake_City", {"weight": 1221.189289}),
    ("Portland", "Seattle", {"weight": 279.0817311}),
    ("Richmond", "Washington_DC", {"weight": 190.1446685}),
    ("Rochester", "Syracuse", {"weight": 145.265921}),
    ("San_Francisco", "San_Jose", {"weight": 77.16267231}),
    ("San_Jose", "Santa_Barbara", {"weight": 446.9898708}),
    ("Scranton", "Syracuse", {"weight": 223.7750822}),
    ("Seattle", "Spokane", {"weight": 444.2069519}),
    ("Springfield", "St_Louis", {"weight": 144.0599684}),
    ("Tallahassee", "Tampa", {"weight": 394.0942686})
])

nx.draw(G2, pos=pos_G2, with_labels=True)

for i in range(0, len(G2)):
    if i < terminals:
        color_map.append('red')
    else:
        color_map.append('blue')
nx.draw(G2, node_color=color_map, node_size=200, pos=pos_G2, with_labels=True)
plt.show()

G = nx.convert_node_labels_to_integers(G2, first_label=0, ordering='default', label_attribute=None)
terminal_nodes = list(G)[0:terminals]
print(steiner_tree(G, terminal_nodes))
main.algorithm(G, pos_G2, terminals)