import networkx as nx
# docum networkx : https://networkx.org/

import pandas as pd
import matplotlib as plt

df = pd.read_csv("C:/Projets_Python/ergm/inputs/test_adj_matrix.csv", sep=";", header=None)
G = nx.from_pandas_adjacency(df)
G.name = "Graph from pandas adjacency matrix"
nx.draw_networkx(G)
plt.pyplot.show()


pass