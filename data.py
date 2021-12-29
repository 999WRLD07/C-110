import plotly.figure_factory as ff
import pandas as pd
import statistics
import random

df = pd.read_csv("medium_data.csv")
listData = df["reading_time"].to_list()
print(listData)

fig = ff.create_distplot([listData], ["time"])
# fig.show()
mean = statistics.mean(listData)
std = statistics.stdev(listData)
print(mean, std)
dataset = []
for i in range(0,100): 
    index = random.randint(0,len(listData))
    value = listData[index]
    dataset.append(value)
mean_sample = statistics.mean(dataset)
std_sample = statistics.stdev(dataset)
print(mean_sample, std_sample)