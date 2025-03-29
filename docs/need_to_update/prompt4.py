import yaml

yaml_code = """
# Anchors for cognitive processes
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

# Recursive structure using merge key
recursive_structure:
  - <<: *understanding
    - <<: *analysis
      - <<: *exploration
      - <<: *reflection
        - <<: *meta_observation
  - <<: *understanding
    - <<: *analysis
      - <<: *exploration
      - <<: *reflection
        - <<: *meta_observation
  - <<: *understanding
    - <<: *analysis
      - <<: *exploration
      - <<: *reflection
        - <<: *meta_observation
"""
data = yaml.safe_load(yaml_code)

for key, value in data.items():
    print(f"Key: {key}")
    print(value)
    print("\n")
