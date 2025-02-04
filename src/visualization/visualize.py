# -*- coding: utf-8 -*-
"""Visualization Plots.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GKxgVvU6Ar94Qnt6qnQoiysjwDDCmA1g
"""

import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import numpy as np

"""## Count plots"""

places = ['Bangalore']*5 + ['Delhi']*5 + ['Indore']*5 + ['Kochi']*5 + ['Coimbatore (test)']*5
scene_classes = ['commercial', 'residential', 'industrial', 'others', 'mixed']
scenes = scene_classes*5
numbers = [108, 122, 31, 19, 13] + [106, 145, 9, 51, 23] + [89, 102, 32 ,43, 8] + [43, 20, 10, 8, 8] + [42, 27, 25, 20, 20]

my_df = pd.DataFrame([places, scenes, numbers]).T.rename(columns = {0: 'city', 1: 'class', 2:'counts'})

fig = go.Figure()

for city in my_df.city.value_counts().index.tolist():

  temp_df = my_df[my_df['city'] == city]

  fig.add_trace(go.Bar(x=temp_df['class'],
                  y=temp_df['counts'],
                  text=temp_df['counts'].astype(np.int16),
                  name=city,
                  ))

fig.update_traces(textposition='outside')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', bargap=0.15,
                  bargroupgap=0.1, barmode='group',
                  yaxis = dict(title = 'Count'), xaxis = dict(title = 'Scene Class'))
fig.show()

fig = go.Figure()

for city in my_df.iloc[20:].city.value_counts().index.tolist():

  temp_df = my_df[my_df['city'] == city]

  fig.add_trace(go.Bar(x=temp_df['class'],
                  y=temp_df['counts'],
                  text=temp_df['counts'].astype(np.int16),
                  name=city,
                  ))

fig.update_traces(textposition='outside')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', bargap=0.15,
                  bargroupgap=0.1, barmode='group',
                  yaxis = dict(title = 'Count'), xaxis = dict(title = 'Scene Class'))
fig.show()

"""## Feature Importance Plot"""

objects = ['tree', 'car', 'wheel', 'person', 'land vehicle', 'palm tree', 'clothing', 
           'man', 'billboard', 'bus', 'motorcycle', 'truck', 'bicycle', 'footwear', 'street light',
           'van', 'table', 'jeans', 'flowerpot'] # ignored human face
           
counts = [4577, 3506, 2701, 2204, 1878, 1350, 1349, 1234, 844,804,518,344,325,301,227,178,
          164,132,126]

my_df = pd.DataFrame([objects, counts]).T.rename(columns = {0: 'object', 1:'counts'})

fig = go.Figure(go.Bar(
            x=my_df['counts'],
            y=my_df['object'],
            text = my_df['counts'],
            orientation='h', 
            marker_color='rgb(55, 83, 109)'))

fig.update_traces(textposition='outside')
fig.update_layout(barmode='stack', yaxis={'categoryorder':'total ascending'})
fig.show()



labels = ["US", "China", "European Union", "Russian Federation", "Brazil", "India",
          "Rest of World"]

# Create subplots: use 'domain' type for Pie subplot
fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
fig.add_trace(go.Pie(labels=labels, values=[16, 15, 12, 6, 5, 4, 42], name="GHG Emissions"),
              1, 1)
fig.add_trace(go.Pie(labels=labels, values=[27, 11, 25, 8, 1, 3, 25], name="CO2 Emissions"),
              1, 2)

# Use `hole` to create a donut-like pie chart
fig.update_traces(hole=.4, hoverinfo="label+percent+name")

fig.update_layout(
    title_text="Global Emissions 1990-2011",
    # Add annotations in the center of the donut pies.
    annotations=[dict(text='GHG', x=0.18, y=0.5, font_size=20, showarrow=False),
                 dict(text='CO2', x=0.82, y=0.5, font_size=20, showarrow=False)])
fig.show()

labels = ["Asia", "Europe", "Africa", "Americas", "Oceania"]

fig = make_subplots(1, 2, specs=[[{'type':'domain'}, {'type':'domain'}]],
                    subplot_titles=['1980', '2007'])
fig.add_trace(go.Pie(labels=labels, values=[4, 7, 1, 7, 0.5], scalegroup='one',
                     name="World GDP 1980"), 1, 1)
fig.add_trace(go.Pie(labels=labels, values=[21, 15, 3, 19, 1], scalegroup='one',
                     name="World GDP 2007"), 1, 2)

fig.update_layout(title_text='World GDP')
fig.show()


# neighborhood objects detected by this
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("/content/drive/MyDrive/frequency_df.csv")
df.drop(['building', 'house', 'skyscraper', 'tower', 'window', 'Unnamed: 0'], axis = 1, inplace = True)

num = 20
others = df[df.sum()[df.sum() <= num].index.tolist()].sum().values.sum()
final_df = df[df.sum()[df.sum() > num].index.tolist()].sum().append(pd.Series({'others': others}))

import plotly.graph_objects as go

labels = final_df.index.tolist()
values = final_df.values.tolist()

fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig.show()


# neighborhood objects detected by this

df = pd.read_csv("/content/drive/MyDrive/frequency_test_df.csv")
df.drop(['building', 'house', 'window', 'Unnamed: 0'], axis = 1, inplace = True)

num = 2
others = df[df.sum()[df.sum() <= num].index.tolist()].sum().values.sum()
final_df = df[df.sum()[df.sum() > num].index.tolist()].sum().append(pd.Series({'others': others}))

import plotly.graph_objects as go

labels = final_df.index.tolist()
values = final_df.values.tolist()

fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig.show()