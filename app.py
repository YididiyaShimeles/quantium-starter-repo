import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("formatted_sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])

app = Dash(__name__)

# Layout
app.layout = html.Div(
    style={"textAlign": "center", "fontFamily": "Arial"},
    children=[
        html.H1("Pink Morsel Sales Dashboard", style={"color": "#2c3e50"}),

        html.Div([
            html.Label("Select Region:", style={"fontWeight": "bold"}),

            dcc.RadioItems(
                id="region-filter",
                options=[
                    {"label": "All", "value": "all"},
                    {"label": "North", "value": "north"},
                    {"label": "South", "value": "south"},
                    {"label": "East", "value": "east"},
                    {"label": "West", "value": "west"},
                ],
                value="all",
                labelStyle={"display": "inline-block", "margin": "10px"}
            )
        ]),

        dcc.Graph(id="sales-graph")
    ]
)

# Callback (this makes it interactive)
@app.callback(
    Output("sales-graph", "figure"),
    Input("region-filter", "value")
)
def update_graph(selected_region):

    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["Region"] == selected_region]

    # Group by date
    df_daily = filtered_df.groupby("Date", as_index=False)["Sales"].sum()

    # Create graph
    fig = px.line(
        df_daily,
        x="Date",
        y="Sales",
        title=f"Sales Over Time ({selected_region.capitalize()})",
        labels={"Sales": "Total Sales", "Date": "Date"}
    )

    return fig


# Run app
if __name__ == "__main__":
    app.run(debug=True)