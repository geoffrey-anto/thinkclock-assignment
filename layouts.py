from dash import dcc
import dash_mantine_components as dmc

options = [
    "battery_impedance",
    "re",
    "rct"
]


MAIN_LAYOUT = lambda df : dmc.Container([
    dmc.Title('Analysis of battery cell aging through charge & discharge cycles', color="blue", size="h3", align="center",mb=20),
    dmc.Group([
        dmc.Text("Select battery type:", color="white"),
        dmc.Select(
            data=[i for i in df["battery_id"].unique()],
            id='battery-type-select',
            value='-1',
            size="sm",
            c="white"
        ),
    ], position="center", spacing="md", style={"marginBottom": "20px"}),
    dmc.Group([
        dmc.Text("Select feature:", color="white"),
        dmc.Select(
            data=[i for i in options],
            id='feature-select',
            value='-1',
            size="sm",
        ),
    ], position="center", spacing="md", style={"marginBottom": "20px"}),
    dmc.Group([
        dmc.Text("Select frequency:", color="white"),
        dmc.Select(
            id='frequency-select',
            value='-1',
            size="sm",
        ),
    ], position="center", spacing="md", style={"marginBottom": "20px"}),
    dmc.Grid(children=[], gutter="xl", h="100vh", id="graph-container"),

], fluid=True, bg="#131212", h="100vh", p=20, m=-10)