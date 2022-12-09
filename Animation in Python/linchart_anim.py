import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import bar_chart_race as bcr
from matplotlib.animation import FuncAnimation, writers

df = pd.read_csv("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
df = df.set_index('country').stack().reset_index(name="GDP").rename(columns={'level_1': 'year'})

print(df.head())

# print(df['country'])
countries = ["China", "United States", "Japan", "India", "Ethiopia", "United Kingdom"]
line_chart_plot = df.loc[df['country'].isin(countries), :]
# print(line_chart_plot)

# define colors
colors = ['red', 'green', 'yellow', 'blue', 'orange', 'black']
fig, ax = plt.subplots()


def plot_linechart(i):
    for j in range(len(colors)):
        country = countries[j]
        color = colors[j]

        data = line_chart_plot.loc[line_chart_plot['country'] == country, :]
        ax.plot(data.year[:i], data.GDP[:i], color)


plt.title("Line chart animation")
num_frames = len(line_chart_plot['year'].unique())
anim = FuncAnimation(fig, plot_linechart, frames=num_frames, interval=50)
# anim.save("linechart.gif")
plt.show()