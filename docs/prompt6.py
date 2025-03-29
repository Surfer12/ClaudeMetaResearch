import yaml

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

data = yaml.safe_load(yaml_code)
print_tree(data)
