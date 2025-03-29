import yaml
# import pygraphviz as pgv
# import networkx as nx
import pygraphviz as pgv
import networkx as nx
import matplotlib.pyplot as plt
import asciitree

# YAML code to parse
yaml_code = """
understanding: &understanding
  overview: "Initial thoughts"

analysis: &analysis
  breakdown:
    - "Insight into current focus"
  challenges:
    - "Current challenge"

exploration: &exploration
  concepts:
    - "Related concept"
  perspectives:
    - "Different angle"

reflection: &reflection
  insights:
    - "Insight from analysis"
  communication:
    - "Need for clearer concepts"

meta_observation: &meta_observation
  process: "Reflection on cognitive flow"
  recursion: "How recursion aids in understanding"
  meta_reflection: "Thoughts on iterative learning"

# Now use the anchors in the recursive structure
recursive_structure:
  - *understanding
  - *analysis
  - *exploration
  - *reflection
  - *meta_observation
"""

data = yaml.safe_load(yaml_code)

# Create a graph
graph = pgv.AGraph(directed=True)

# Recursive function to add nodes and edges to the graph
def add_to_graph(parent, data):
    if isinstance(data, dict):
        for key, value in data.items():
            node_label = f"{key}: {value}"
            graph.add_node(node_label)
            graph.add_edge(parent, node_label)
            add_to_graph(node_label, value)
    elif isinstance(data, list):
        for item in data:
            node_label = str(item)
            graph.add_node(node_label)
            graph.add_edge(parent, node_label)
            add_to_graph(node_label, item)

# Add the root node to the graph
root_label = "recursive_structure"
graph.add_node(root_label)
add_to_graph(root_label, data[root_label])

class TreeNode:
    def __init__(self, text, children=None):
        self.text = text
        self.children = children if children is not None else []

    def __str__(self):
        return self.text

def convert_to_tree(key, data):
    if isinstance(data, dict):
        node = TreeNode(key, children=[convert_to_tree(k, v) for k, v in data.items()])
        return node
    elif isinstance(data, list):
        node = TreeNode(key, children=[TreeNode(str(item)) for item in data]) # Treat list items as leaf nodes
        return node
    else:
        return TreeNode(f"{key}: {data}" if key else str(data))

def convert_yaml_to_tree(data):
    root_children = []
    for key, value in data.items():
        root_children.append(convert_to_tree(key, value))
    if len(root_children) == 1:
        return root_children[0]
    else:
        return TreeNode("root", children=root_children)


# Convert the YAML data to a tree-like structure
tree_structure_root = convert_yaml_to_tree(data)


print(asciitree.draw_tree(tree_structure_root))

# Render the graph
graph.layout(prog='dot')
graph.draw('yaml_structure.svg')
plt.show()
