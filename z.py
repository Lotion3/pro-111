import plotly_express as py
import pandas as pd
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go

df=pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()
sample=[]

for i in range(0,30):
    random_index=random.randint(0,len(data)-1)
    value=data[random_index]
    sample.append(value)
print(sample)
samMean=statistics.mean(sample)
mean=statistics.mean(data)
stDev=statistics.stdev(data)
zScore=(mean-samMean)/stDev
print(zScore)
fig=ff.create_distplot([data],["Reading Time of articles"], show_hist=False)
fig.show()