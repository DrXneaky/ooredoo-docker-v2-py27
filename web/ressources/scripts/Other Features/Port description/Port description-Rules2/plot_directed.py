
# Author: Rodrigo Dorantes-Gilardi (rodgdor@gmail.com)
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import networkx as nx

#G = nx.generators.directed.random_k_out_graph(20, 5, 0.5)
graph = { "aaaaaaaaa" : ["ccccccccc"],
      "bbbbbbbbb" : ["ccccccccc", "eeeeeeeeee"],
      "ccccccccc" : ["aaaaaaaaa", "bbbbbbbbb", "ddddddddddd", "eeeeeeeeee", "ffffffffff"],
      "ddddddddddd" : ["ccccccccc"],
      "eeeeeeeeee" : ["ccccccccc", "bbbbbbbbb"],
    } 

G = nx.MultiDiGraph()

M = G.number_of_edges()
print ("number of edges", M)

for k,v in graph.items():
    for vv in v:
        G.add_edge(k,vv)
print(G)

G = nx.petersen_graph()

pdot = nx.drawing.nx_pydot.to_pydot(G)

for node in enumerate(pdot.get_nodes()):
    node.set_shape('oval')

png_path = "test.png"
pdot.write_png(png_path)

pos = nx.layout.spring_layout(G)
#print(pos)

node_sizes = [3 + 10 * i for i in range(len(G))]
M = G.number_of_edges()
print ("number of edges", M)
edge_colors = range(2, M + 2)
edge_alphas = [(5 + i) / (M + 4) for i in range(M)]

#so^>v<dph8
nodes = nx.draw_networkx_nodes(G, pos, node_size=2000,node_shape="so", node_color='blue')
print("nodes:",nodes)
edges = nx.draw_networkx_edges(G, pos, node_size=800, arrowstyle='->',
                               arrowsize=10, edge_color=edge_colors,
                               edge_cmap=plt.cm.Blues, width=2)
print("edges: ", edges)
# set alpha value for each edge
labels={}
labels[0]=r'$a$'
for i in range (20):
    labels[0]=r'$1$'

nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')

for i in range(M):
    edges[i].set_alpha(edge_alphas[i])


pc = mpl.collections.PatchCollection(edges, cmap=plt.cm.Blues)
pc.set_array(edge_colors)
plt.colorbar(pc)

ax = plt.gca()
ax.set_axis_off()

#nx.draw(G,node_size=4000,node_shape="o", with_labels = True)
plt.show()


"""

import random
import networkx as nx
""" 

G = nx.petersen_graph()
print(type(G))
pdot = nx.drawing.nx_pydot.to_pydot(G)
"""

graph = { "aaaaaaaaa" : ["ccccccccc"],
      "bbbbbbbbb" : ["ccccccccc", "eeeeeeeeee"],
      "ccccccccc" : ["aaaaaaaaa", "bbbbbbbbb", "ddddddddddd", "eeeeeeeeee", "ffffffffff"],
      "ddddddddddd" : ["ccccccccc"],
      "eeeeeeeeee" : ["ccccccccc", "bbbbbbbbb"],
    } 

G = nx.DiGraph()

M = G.number_of_edges()
print ("number of edges", M)

for k,v in graph.items():
    for vv in v:
        G.add_edge(k,vv)

pdot = nx.drawing.nx_pydot.to_pydot(G)

shapes = ['box', 'polygon', 'ellipse', 'oval', 'circle', 'egg', 'triangle', 'exagon', 'star', ]
colors = ['blue', 'black', 'red', '#db8625', 'green', 'gray', 'cyan', '#ed125b']
styles = ['filled', 'rounded', 'rounded, filled', 'dashed', 'dotted, bold']

for i, node in enumerate(pdot.get_nodes()):
    node.set_label("AS365984")
    node.set_shape('ellipse')
    node.set_fontcolor('black')
    node.set_fillcolor('white')
    node.set_style(styles[2])
    node.set_color('black')

for i, edge in enumerate(pdot.get_edges()):
    edge.set_fontcolor(colors[2])
    edge.set_style(styles[2])
    edge.set_color(colors[1])

png_path = 'test.png'
pdot.write_png(png_path) 