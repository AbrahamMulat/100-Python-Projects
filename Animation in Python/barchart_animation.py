import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, writers

df = pd.read_csv("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
df = df.set_index('country').stack().reset_index(name="GDP").rename(columns={'level_1': 'year'})

print(df.head())

# Create a barchart
countries_plot = ["China", "United States", "Japan", "India", "Ethiopia", "United Kingdom"]
barchart_data = df.loc[df['country'].isin(countries_plot), :]
print(barchart_data.head())
font = {'weight': 'normal', 'size': 40, 'color': 'lightgray'}

years = barchart_data['year'].unique()
colors = ['#FF0000', '#03d3fc', '#098c45', '#aa151b', '#002868', '#b1fc03']

fig, ax = plt.subplots(figsize=(10, 5))
label = ax.text(0.95, 0.2, years[0],
                horizontalalignment='right',
                verticalalignment='top',
                transform=ax.transAxes,
                fontdict=font)


def plot_barchart(i):
    year = years[i]

    data_temp = barchart_data.loc[barchart_data['year'] == year, :]
    ax.clear()
    # ax.barh(data_temp.country, data_temp.GDP, color=colors)
    # label.set_text(year)


# anim = FuncAnimation(fig, plot_barchart, frames=len(years))
# anim.save('barchart.gif')
# plt.show()


# Create a barchart animation
barchart_race_data = df.copy()
n_observations = 10

fig, ax = plt.subplots(figsize=(10, 5))

font = {
    'weight': 'normal',
    'size': 40,
    'color': 'lightgray'
}

years = barchart_race_data['year'].unique()

label = ax.text(0.95, 0.20, years[0],
                horizontalalignment='right',
                verticalalignment='top',
                transform=ax.transAxes,
                fontdict=font)


def plot_barchart_race(i):
    year = years[i]

    data_temp = barchart_race_data.loc[barchart_race_data['year'] == year, :]

    # Create rank and get first 10 countries
    data_temp['gdp2'] = data_temp['GDP'].rank(ascending=False)
    data_temp = data_temp.loc[data_temp['gdp2'] <= n_observations]

    colors = plt.cm.Dark2(range(6))

    ax.clear()
    ax.barh(y=data_temp['gdp2'],
            width=data_temp.GDP,
            tick_label=data_temp['country'],
            color=colors)

    label = ax.text(0.95, 0.20, year,
                    horizontalalignment='right',
                    verticalalignment='top',
                    transform=ax.transAxes,
                    fontdict=font)

    ax.set_ylim(ax.get_ylim()[::-1])  # Revert axis


plt.title("Countries GDP barchart race")
anim = FuncAnimation(fig, plot_barchart_race, frames=len(years))
anim.save('barchart_race.gif')
plt.show()