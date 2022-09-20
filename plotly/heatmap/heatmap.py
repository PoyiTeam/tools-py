#%%
import plotly.graph_objects as go
import numpy as np

z = np.loadtxt("heatmap_data.csv", delimiter=",")

num_y, num_x = np.shape(z)
x = np.linspace(start=0, stop=10, num=num_x)
y = np.linspace(start=0, stop=6000, num=num_y)

trace_heatmap = go.Heatmap(z=z,
                           x=x,
                           y=y,
                           colorscale='Viridis',
                           showscale=False)

layout = dict(xaxis_showgrid=False,
              xaxis_zeroline=False,
              xaxis_showticklabels=False,
              yaxis_showgrid=False,
              yaxis_zeroline=False,
              yaxis_showticklabels=False,
              margin=dict(l=0, r=0, b=0, t=0),
              autosize=False,
              width=299,
              height=299)

fig = go.Figure(data=trace_heatmap, layout=layout)

fig.show()
# %%
