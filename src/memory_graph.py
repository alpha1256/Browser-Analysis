import plotly.graph_objs as go
import pandas as pd
import plotly.offline as ply

filename = input("Enter name of the file you want to open")
inPutfile = open(filename)
memoryPercent =[]
timeUp =[]
for i in inPutfile:
	memoryPercent.append(float(i[0:4]))
	timeUp.append(int(i[4:7]))

mem_trace = go.Scatter(x = timeUp,y = memoryPercent )
name = input("Enter name of the graph")
layout = dict(title = name
	xaxis = dict(title = ""Up Time in secs')
	yaxis = dict(title = 'Memory usuage in percent'))

data = [mem_trace]
figure = dict(data = data, layout = layout)
ply.plot(figure, filename='MemoryGraph.html')