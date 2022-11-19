#%%
import plotly.graph_objects as go
import numpy as np

z = np.loadtxt("surface_data.csv", delimiter=",")

num_y, num_x = np.shape(z)
x = np.linspace(start=0, stop=10, num=num_x)
y = np.linspace(start=0, stop=6000, num=num_y)

layout = dict(title="my title",
              autosize=False,
              width=600,
              height=600,
              margin=dict(l=30, r=30, b=0, t=0))
trace_surface = go.Surface(x=x, y=y, z=z, colorscale="Viridis")
fig = go.Figure(data=trace_surface, layout=layout)

fig.show()
# %%
