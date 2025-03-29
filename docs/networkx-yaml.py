import yaml
import networkx as nx
import matplotlib.pyplot as plt

yaml_code = """ ... (your YAML data) ... """
data = yaml.safe_load(yaml_code)

def create_graph_from_yaml(data, graph=None, parent_node=None, path=None):
    if graph is None:
        graph = nx.DiGraph()
    if path is None:
        path = []

    for key, value in data.items():
        current_path = path + [key]
        node_name = '.'.join(current_path) # More descriptive node name
        label = f"{key}: {str(value)[:20]}..." if isinstance(value, str) and len(str(value)) > 20 else f"{key}: {value}" if not isinstance(value, (dict, list)) else key # Label for display

        graph.add_node(node_name, label=label) # Store label as node attribute
        if parent_node:
            graph.add_edge(parent_node, node_name)

        if isinstance(value, dict):
            create_graph_from_yaml(value, graph, node_name, current_path)
        elif isinstance(value, list):
            for i, item in enumerate(value):
                list_item_path = current_path + [str(i)] #index in path
                list_item_node = '.'.join(list_item_path)
                item_label = str(item)[:20] + "..." if isinstance(item, str) and len(str(item)) > 20 else str(item)
                graph.add_node(list_item_node, label=item_label)
                graph.add_edge(node_name, list_item_node)
                if isinstance(item, dict):
                    create_graph_from_yaml(item, graph, list_item_node, list_item_path)

    return graph

graph = create_graph_from_yaml(data)

# Refined visualization with better layout, labels, and styling
pos = nx.spring_layout(graph, k=0.3, iterations=50) # Spring layout for better spacing
plt.figure(figsize=(12, 12)) # Adjust figure size for better visualization
node_options = {
    'node_color': 'lightblue',
    'node_size': 2000,
    'alpha': 0.7
}
nx.draw(graph, pos, labels=nx.get_node_attributes(graph, 'label'), with_labels=True, **node_options,
        font_size=8, font_weight='bold', font_color=' DimGray',
        edge_color='gray', width=0.8, style='dashed') # Styling adjustments

plt.title("YAML Data Structure Visualization", fontsize=14) # Title for context
plt.axis('off') # Turn off axis for cleaner look
plt.show() # Or plt.savefig("yaml_graph_refined.png")
