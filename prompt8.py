
import yaml
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

def convert_dict_to_tree(d):
    tree = {}
    for key, value in d.items():
        if isinstance(value, dict):
            tree[key] = convert_dict_to_tree(value)
        else:
            tree[key] = value
    return tree

# Convert the YAML data to a tree-like structure
tree_structure = convert_dict_to_tree(data)

def print_tree(data, indent=0):
    for key, value in data.items():
        print("\t" * indent + str(key))
        if isinstance(value, dict):
            print_tree(value, indent + 1)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    print_tree(item, indent + 1)
                else:
                    print("\t" * (indent + 1) + str(item))
        else:
            print("\t" * (indent + 1) + str(value))

# Print the YAML structure as an ASCII tree
print(asciitree.draw_tree(tree_structure))

# Render the graph
graph.layout(prog='dot')
graph.draw('yaml_structure.svg')
