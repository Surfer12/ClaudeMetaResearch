import yaml
import pygraphviz as pgv

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

# Render the graph
graph.layout(prog='dot')
graph.draw('yaml_structure.png')