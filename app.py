from dash import Dash, html, dcc

app = Dash(__name__)

app.layout = html.Div([
    html.H1(
        "Pink Morsel Sales Dashboard",
        id="dashboard-header",
        style={"color": "#2c3e50"}
    ),

    dcc.RadioItems(
        id="region-picker",
        options=[
            {"label": "All", "value": "all"},
            {"label": "North", "value": "north"},
            {"label": "South", "value": "south"},
            {"label": "East", "value": "east"},
            {"label": "West", "value": "west"},
        ],
        value="all",
        labelStyle={"display": "inline-block", "margin": "10px"},
    ),

    dcc.Graph(id="sales-graph")
])

if __name__ == "__main__":
    app.run(debug=True)