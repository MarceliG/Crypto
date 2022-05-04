import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash
import yfinance as yf
import pandas as pd

data = yf.download(tickers="BTC-EUR", period="22h", interval="15m")
app = DjangoDash("data_price")
app.layout = html.Div(
    [
        dcc.Checklist(
            id="toggle-rangeslider",
            options=[{"label": "Include Rangeslider", "value": "slider"}],
            value=["slider"],
        ),
        html.H1("Bitcoin price"),
        dcc.Graph(
            id="btc_graph",
            animate=True,
        ),
    ]
)


@app.callback(
    Output(component_id="btc_graph", component_property="figure"),
    [Input(component_id="toggle-rangeslider", component_property="value")],
)
def display_value(value):
    # declare figure
    figure = go.Figure()
    # Candlestick
    figure = go.Candlestick(
        x=data.index,
        open=data["Open"],
        high=data["High"],
        low=data["Low"],
        close=data["Close"],
        name="market data",
    )

    layout = go.Layout(
        title="Crypto price",
        xaxis_rangeslider_visible="slider" in value,
        yaxis_title="Price (EUR)",
    )
    return {"data": [figure], "layout": layout}
