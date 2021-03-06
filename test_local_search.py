
from shapely.geometry import *
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from intersections_and_roads import *
from search import *
import geopandas as gpd
import ast

# # Read in the geolocation data for cambridge
intersections = gpd.read_file('./cambridgegis_data_trans/Intersections/TRANS_Intersections.topojson')
street_centerline = gpd.read_file('./cambridgegis_data_trans/Street_Centerlines/TRANS_Centerlines.topojson')
intersection_graph, connection_dict = build_intersection_graph(intersections=intersections, street_centerline=street_centerline)

# select a set of random starting points
p1 = intersection_graph[np.random.choice(intersection_graph.keys())]
p2 = intersection_graph[np.random.choice(intersection_graph.keys())]
p3 = intersection_graph[np.random.choice(intersection_graph.keys())]
p4 = intersection_graph[np.random.choice(intersection_graph.keys())]
p5 = intersection_graph[np.random.choice(intersection_graph.keys())]

starting_points = [p1,p2,p3, p4,p5]

best_centroid, best_cost, k_points = k_beam_search(5, intersection_graph, connection_dict, get_road_cost, euclidean_heuristic, starting_points=starting_points)

fig, ax = plt.subplots(1,1, figsize=(10, 10))
routes, connections = get_routes_to_centroid(best_centroid, starting_points, intersection_graph, connection_dict)
plot_local_search_graph(best_centroid, starting_points, [], intersection_graph, connection_dict, routes, ax=ax)
