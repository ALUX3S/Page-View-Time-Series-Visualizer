import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

# Clean data
df = df[(df['value']>=df['value'].quantile(0.025))&(df['value']<=df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(17, 5))
    plt.plot(df.index, df['value'], color='brown')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel("Date")
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df['Years'] = df.index.year
    df['Months'] = df.index.month
    df_bar = pd.pivot_table(df, values="value", index=["Years"], columns=["Months"], aggfunc=np.average)
    df_bar.columns = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # Draw bar plot
    fig = df_bar.plot.bar(ylabel="Average Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box = df_box.sort_values(by='Months')
    # Draw box plots (using Seaborn)

    fig, axes = plt.subplots(1,2, figsize=(17, 5))
    sns.boxplot(data=df_box, x='year', y='value', ax=axes[0], palette = "deep").set(title='Year-wise Box Plot (Trend)', ylabel='Page Views')
    sns.boxplot(data=df_box, x='month', y='value', ax=axes[1], palette = "pastel").set(title='Month-wise Box Plot (Seasonality)', ylabel='Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
