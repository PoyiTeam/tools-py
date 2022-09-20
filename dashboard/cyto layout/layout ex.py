import dash
import dash_cytoscape as cyto
import dash_html_components as html

app = dash.Dash(__name__)

nodes = [
    {
        "data": {"id": short, "label": label},
        "position": {"x": 20 * lat, "y": -20 * long},
    }
    for short, label, long, lat in (
        ("la", "Los Angeles", 34.03, -118.25),
        ("nyc", "New York", 40.71, -74),
        ("to", "Toronto", 43.65, -79.38),
        ("mtl", "Montreal", 45.50, -73.57),
        ("van", "Vancouver", 49.28, -123.12),
        ("chi", "Chicago", 41.88, -87.63),
        ("bos", "Boston", 42.36, -71.06),
        ("hou", "Houston", 29.76, -95.37),
    )
]

edges = [
    {"data": {"source": source, "target": target}}
    for source, target in (
        ("van", "la"),
        ("la", "chi"),
        ("hou", "chi"),
        ("to", "mtl"),
        ("mtl", "bos"),
        ("nyc", "bos"),
        ("to", "hou"),
        ("to", "nyc"),
        ("la", "nyc"),
        ("nyc", "bos"),
    )
]

elements = nodes + edges

app.layout = html.Div(
    [
        cyto.Cytoscape(
            id="cytoscape-layout-1",
            elements=elements,
            style={"width": "100%", "height": "350px"},
            layout={"name": "preset"},
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
