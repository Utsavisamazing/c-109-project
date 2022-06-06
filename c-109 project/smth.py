import random
from unicodedata import name
from unittest import result
import pandas as pd
import statistics as st
import plotly.figure_factory as ff
import plotly.graph_objects as go

df=pd.read_csv("StudentsPerformance.csv")
fig=ff.create_distplot([df["math score"].tolist()],["writing score"],show_hist=False)
fig.show()

mean = st.mean(df)
standard_deviation=st.stdev(df)
print(mean)
print(standard_deviation)
sd1start,sd1end=mean-standard_deviation,mean+standard_deviation
sd2start,sd2end=mean-(2*standard_deviation),mean+(2*standard_deviation)
sd3start,sd3end=mean-(3*standard_deviation),mean+(3*standard_deviation)

fig = ff.create_distplot([df],  ["Result"], show_hist=False)
fig.add_trace(go.Scatter(x=[sd1start,sd1start],y=[0,0.17],mode="lines",name="sd1"))
fig.add_trace(go.Scatter(x=[sd1end,sd1end],y=[0,0.17],mode="lines",name="sd1"))
fig.add_trace(go.Scatter(x=[sd2start,sd2start],y=[0,0.17],mode="lines",name="sd2"))
fig.add_trace(go.Scatter(x=[sd2end,sd2end],y=[0,0.17],mode="lines",name="sd2"))
fig.show()

listsd1 = [result for result in df if result > sd1start and result < sd1end ]
listsd2 = [result for result in df if result > sd2start and result < sd2end ]
listsd3 = [result for result in df if result > sd3start and result < sd3end ]
print("{}% of data lies within standard deviation 1" .format(len(listsd1)*100.0/len(df)))
print("{}% of data lies within standard deviation 2" .format(len(listsd2)*100.0/len(df)))
print("{}% of data lies within standard deviation 3" .format(len(listsd3)*100.0/len(df)))