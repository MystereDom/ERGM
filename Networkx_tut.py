import networkx as nx
G = nx.Graph()

# Hashing is the process of transforming any given key or a string of characters into another value

### NODES ###
# add a node
G.add_node(1)

# add nodes from any iterable container, such as a list
G.add_nodes_from([2, 3])

# You can also add nodes along with node attributes if your container yields 2-tuples of the form
# (node, node_attribute_dict):
G.add_nodes_from([(4, {"color": "red"}), (5, {"color": "green"})])


pass

