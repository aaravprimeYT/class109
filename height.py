import plotly.figure_factory as ff
import csv
import pandas as pd
import statistics
import random
import plotly.graph_objects as go

df = pd.read_csv("class108.csv")

heightList = df["Height(Inches)"].tolist()

mean = statistics.mean(heightList)
median = statistics.median(heightList)
mode = statistics.mode(heightList)
deviation = statistics.stdev(heightList)

#fsds = first Standard start, fsde = first standard deviation end
fsds,fsde = mean-deviation,mean+deviation
ssds,ssde = mean-(2*deviation),mean+(2*deviation)
tsds,tsde = mean-(3*deviation),mean+(3*deviation)

fig = ff.create_distplot([heightList],["Height"],show_hist=False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.17],mode = "lines", name = "mean"))
fig.add_trace(go.Scatter(x = [fsds,fsds], y = [0,0.17],mode = "lines", name = "Standard Deviation 1"))
fig.add_trace(go.Scatter(x = [fsde,fsde], y = [0,0.17],mode = "lines", name = "Standard Deviation 1"))
fig.add_trace(go.Scatter(x = [ssds,ssds], y = [0,0.17],mode = "lines", name = "Standard Deviation 2"))
fig.add_trace(go.Scatter(x = [ssde,ssde], y = [0,0.17],mode = "lines", name = "Standard Deviation 2"))
fig.add_trace(go.Scatter(x = [tsds,tsds], y = [0,0.17],mode = "lines", name = "Standard Deviation 3"))
fig.add_trace(go.Scatter(x = [tsde,tsde], y = [0,0.17],mode = "lines", name = "Standard Deviation 3"))
fig.show()

listOfDataWithinStdev1 = [result for result in heightList if result > fsds and result < fsde]
listOfDataWithinStdev2 = [result for result in heightList if result > ssds and result < ssde]
listOfDataWithinStdev3 = [result for result in heightList if result > tsds and result < tsde]

print("{}% of data lies within standard deviation 1".format(len(listOfDataWithinStdev1)*100/len(heightList)))
print("{}% of data lies within standard deviation 2".format(len(listOfDataWithinStdev2)*100/len(heightList)))
print("{}% of data lies within standard deviation 3".format(len(listOfDataWithinStdev3)*100/len(heightList)))

print(mean,median,mode,deviation)