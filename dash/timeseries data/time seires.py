#%%
from datetime import datetime, timedelta

current_time = datetime.strftime(datetime.now(), "%Y %B %w %H:%M:%S")
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

df = pd.read_csv(
    "C:/Users/ImRadish/OneDrive - 逢甲大學/Programming/python/dashboard/example_data.csv"
)
data_headers = df.columns

app = Dash(__name__)
#%%

app.layout = html.Div(
    [
        dcc.Interval(id="interval_1", interval=1000, n_intervals=0),
        html.Div(id="current-time", children=current_time),
        dcc.Dropdown(
            id="col",
            options=df.columns,
            value=df.columns[0],
        ),
        dcc.Graph(id="time-series"),
    ],
    # style={"display": "inline-block", "width": "49%"},
)


#%%
@app.callback(Output("time-series", "figure"), Input("col", "value"))
def update_timeseries(header):
    timeseries_data = df[header]
    timeseries_data = [[0.1, 0.2, 0.3], timeseries_data]
    return create_time_series(timeseries_data, header)


def create_time_series(timeseries_data, title):

    fig = px.scatter(timeseries_data, x=timeseries_data[0], y=timeseries_data[1])
    fig.update_traces(mode="lines+markers")
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(type="linear")

    fig.add_annotation(
        x=0,
        y=0.85,
        xanchor="left",
        yanchor="bottom",
        xref="paper",
        yref="paper",
        showarrow=False,
        align="left",
        text=title,
    )

    fig.update_layout(height=225, margin={"l": 20, "b": 30, "r": 10, "t": 10})

    return fig


@app.callback(Output("current-time", "children"), Input("interval_1", "n_intervals"))
def update_current_time(n):
    current_time = datetime.strftime(datetime.now(), "%Y %B %w %H:%M:%S")
    return current_time


#%%
app.run_server(debug=True)
