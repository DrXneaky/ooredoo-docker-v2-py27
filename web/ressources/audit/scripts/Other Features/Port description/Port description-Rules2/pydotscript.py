import pydot
g = { "aaaaaaaaa" : ["ccccccccc"],
      "bbbbbbbbb" : ["ccccccccc", "eeeeeeeee"],
      "ccccccccc" : ["aaaaaaaaa", "bbbbbbbbb", "ddddddddd", "eeeeeeeee", "ffffffffff", "ooooooooooo", "zzzzzzzzzz","ppppppppppppp", "nnnnnnnnnnn", "wwwwwwwwwwwww", "lllllllllll"],
      "ddddddddd" : ["ccccccccc", "iiiiiiiii"],
      "eeeeeeeee" : ["ccccccccc", "bbbbbbbbb", "iiiiiiiii", "ffffffffff", "ooooooooooo", "zzzzzzzzzz","ppppppppppppp", "nnnnnnnnnnn", "wwwwwwwwwwwww", "lllllllllll"],
      "ggggggggg" : ["ccccccccc", "aaaaaaaaa", "ddddddddd"],
      "kkkkkkkkk" : ["fffffffff", "ggggggggg", "ppppppppppppp"],
      "fffffffff" : ["iiiiiiiii", "fffffffff"]
    } 
graph = pydot.Dot(graph_type='digraph', rankdir="LR")
print(type(graph))
for k,v in g.items():
  graph.add_node(pydot.Node(k, label = k))
  for vv in v:
    graph.add_edge(pydot.Edge(k,vv,label="back", labelfontcolor="#009933", fontsize="10.0", arrowsize="0.7"))
graph.write_svg("mygraph.svg")

