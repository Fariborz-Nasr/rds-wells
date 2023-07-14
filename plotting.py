import altair as alt
import pandas as pd
from vega_datasets import data

def plot_wells(coords):
    df = pd.DataFrame(coords)
    
    # Read in points
    airports = data.airports()

    # Read in polygons from topojson
    states = alt.topo_feature(data.us_10m.url, feature='states')

    # US states background
    background = alt.Chart(states).mark_geoshape(
        fill='lightgray',
        stroke='white'
    ).properties(
        width=700,
        height=500
    ).project('albersUsa')

    # airport positions on background
    points = alt.Chart(df).mark_circle(
        # size=10,
    ).encode(
        longitude='longitude:Q',
        latitude='latitude:Q',
        color=alt.Color('gradient:Q', scale=alt.Scale(scheme='inferno')),
        tooltip=[
            alt.Tooltip('depth:Q', title='Depth (m)'),
            alt.Tooltip('gradient:Q', title='Gradient (°C/m)', format='0.3f')
        ]
    )

    return background + points