import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Load data
df = pd.read_csv("formatted_sales_data.csv")

# Convert date
df["Date"] = pd.to_datetime(df["Date"])

# Sort by date
df = df.sort_values("Date")

# Group by date
df_daily = df.groupby("Date", as_index=False)["Sales"].sum()

# Create line chart
fig = px.line(
    df_daily,
    x="Date",
    y="Sales",
    title="Pink Morsel Sales Over Time",
    labels={"Sales": "Total Sales", "Date": "Date"}
)

# Create Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Dashboard"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)