from plotly.graph_objs import *
import plotly as py
import plotly.graph_objs as go


pyplt = py.offline.plot

import pandas as pd

# read in volcano database data
df = pd.read_excel(r'dat/volcano_db.xlsx')



# frequency of Country
freq = df
freq = freq.Country.value_counts().reset_index().rename(columns={'index': 'x'})

# plot(1) top 10 countries by total volcanoes
locations = go.Bar(x=freq['x'][0:10],y=freq['Country'][0:10], marker=dict(color='#CF1020'))

# read in 3d volcano surface data
df_v = pd.read_excel(r'dat/volcano.xlsx')

# plot(2) 3d surface of volcano
threed = Surface(z=df_v.values.tolist(), colorscale='Reds', showscale=False)

# plot(3)  scattergeo map of volcano locations
trace3 = {
  "geo": "geo3",
  "lon": df['Longitude'],
  "lat": df['Latitude'],
  "hoverinfo": 'text',
  "marker": {
    "size": 4,
    "opacity": 0.8,
    "color": '#CF1020',
    "colorscale": 'Viridis'
  },
  "mode": "markers",
  "type": "scattergeo"
}

data = go.Data([locations, threed, trace3])

# control the subplot below using domain in 'geo', 'scene', and 'axis'
layout = {
  "plot_bgcolor": 'black',
  "paper_bgcolor": 'black',
  "titlefont": {
      "size": 20,
      "family": "Raleway"
  },
  "font": {
      "color": 'white'
  },
  "dragmode": "zoom",
  "geo3": {
    "domain": {
      "x": [0, 0.55],
      "y": [0, 0.9]
    },
    "lakecolor": "rgba(127,205,255,1)",
    "oceancolor": "rgb(6,66,115)",
    "landcolor": 'white',
    "projection": {"type": "orthographic"},
    "scope": "world",
    "showlakes": True,
    "showocean": True,
    "showland": True,
    "bgcolor": 'black'
  },
  "margin": {
    "r": 10,
    "t": 25,
    "b": 40,
    "l": 60
  },
  "scene": {"domain": {
      "x": [0.5, 1],
      "y": [0, 0.55]
    },
           "xaxis": {"gridcolor": 'white'},
           "yaxis": {"gridcolor": 'white'},
           "zaxis": {"gridcolor": 'white'}
           },
  "showlegend": False,
  "title": "<br>Volcano Database",
  "xaxis": {
    "anchor": "y",
    "domain": [0.6, 0.95]
  },
  "yaxis": {
    "anchor": "x",
    "domain": [0.65, 0.95],
    "showgrid": False
  }
}

annotations = { "text": "Source: NOAA",
               "showarrow": False,
               "xref": "paper",
               "yref": "paper",
               "x": 0,
               "y": 0}

layout['annotations'] = [annotations]

fig = go.Figure(data=data, layout=layout)
pyplt(fig, filename = "tmp/Mixed Subplots Volcano.html")