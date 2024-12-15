from dash import Dash, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import layouts
import utils
import plotly.graph_objects as go
import dash_mantine_components as dmc


dataset = "./dataset/metadata-norm.csv"

df = pd.read_csv(dataset)

app = Dash()


app.layout = layouts.MAIN_LAYOUT(df)

@callback(
    Output(component_id="frequency-select", component_property="data"),
    Input(component_id="feature-select", component_property="value")
)
def update_feature_option(value):
    if value == "battery_impedance":
        return [f"{i*0.1:.1f}" for i in range(1, 49)]
    return []

@callback(
    Output(component_id="graph-container", component_property="children"),
    Input(component_id="battery-type-select", component_property="value"),
    Input(component_id="feature-select", component_property="value"),
    Input(component_id="frequency-select", component_property="value")
)
def update_graph(battery_type, feature, frequency):
    if battery_type == "-1" and feature == "-1" and frequency == "-1":
        return {}
    
    if battery_type == "-1":
        return {}
    
    if feature == "-1":
        return {}
    
    if frequency == "-1" and feature == "battery_impedance":
        return {}
    
    data = utils.get_rows_by_battery_id(df, battery_type, feature, frequency)
    
    if feature == "battery_impedance":
        return [
            dmc.Col([
                dcc.Graph(figure=go.Figure(go.Scattersmith(imag=data[0], real=data[1])), id='graph')
            ], style={"padding": "10px"}),
        ]
    
    if feature == "re":
        return [
        dmc.Col([
            dcc.Graph(figure=px.line(data, x="start_time", y="Re", title="Re vs Time", labels={"Re": "Re", "start_time": "Time"}), id='graph')
        ], style={"padding": "10px"}),
    ]
    
    if feature == "rct":
        return [
        dmc.Col([
            dcc.Graph(figure=px.line(data, x="start_time", y="Rct", title="Rct vs Time", labels={"Rct": "Rct", "start_time": "Time"}), id='graph')
        ], style={"padding": "10px"}),
    ]
    
    return {}
if __name__ == '__main__':
    app.run(debug=True)