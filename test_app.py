"""
Test script for st-cytoscape component
Run with: streamlit run test_app.py
"""
import streamlit as st
from st_cytoscape import cytoscape

st.set_page_config(page_title="st-cytoscape Test", layout="wide")

st.title("🔗 st-cytoscape Component Test")
st.markdown("Testing the updated dependencies (Dec 2025)")

# Sample graph elements
elements = [
    {"data": {"id": "A", "label": "Node A"}, "selected": True},
    {"data": {"id": "B", "label": "Node B"}},
    {"data": {"id": "C", "label": "Node C"}},
    {"data": {"id": "D", "label": "Node D"}},
    {"data": {"id": "E", "label": "Node E"}},
    {"data": {"source": "A", "target": "B", "id": "A➞B"}},
    {"data": {"source": "A", "target": "C", "id": "A➞C"}},
    {"data": {"source": "B", "target": "D", "id": "B➞D"}},
    {"data": {"source": "C", "target": "D", "id": "C➞D"}},
    {"data": {"source": "D", "target": "E", "id": "D➞E"}},
]

# Stylesheet for the graph
stylesheet = [
    {
        "selector": "node",
        "style": {
            "label": "data(label)",
            "width": 40,
            "height": 40,
            "text-valign": "center",
            "text-halign": "left",
            "font-size": "10px",
            "background-color": "#61bffc",
            "color": "#C22727",
        },
    },
    {
        "selector": "edge",
        "style": {
            "width": 2,
            "curve-style": "bezier",
            "target-arrow-shape": "triangle",
            "target-arrow-color": "#999",
            "line-color": "#999",
        },
    },
]

# Layout selection
col1, col2 = st.columns([1, 3])

with col1:
    layout_name = st.selectbox(
        "Layout Algorithm",
        ["fcose", "klay", "dagre", "circle", "grid", "breadthfirst"],
        index=0,
    )
    
    st.markdown("### Selected Elements")

with col2:
    # Create the graph
    layout = {"name": layout_name, "animate": True}
    
    # Add fcose-specific constraints
    if layout_name == "fcose":
        layout["animationDuration"] = 500
        layout["quality"] = "proof"
    
    selected = cytoscape(
        elements,
        stylesheet,
        layout=layout,
        selection_type="additive",
        key="test_graph",
        height="500px",
    )

with col1:
    if selected:
        st.write("**Nodes:**", ", ".join(selected.get("nodes", [])) or "None")
        st.write("**Edges:**", ", ".join(selected.get("edges", [])) or "None")

st.markdown("---")
st.markdown("""
### ✅ Test Checklist
- [ ] Graph renders correctly
- [ ] Layout algorithms work (try different layouts)
- [ ] Node selection works (click nodes)
- [ ] Edge selection works (click edges)
- [ ] Theme colors apply correctly
""")
