import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Import the data
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# 2. Clean the data
df = df[
    (df['value'] <= df['value'].quantile(0.975)) &
    (df['value'] >= df['value'].quantile(0.025))
]

# 3. Draw line plot
def draw_line_plot():
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['value'], color='blue', linewidth=1)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('line_plot.png')
    return plt

# 4. Draw bar plot
def draw_bar_plot():
    # Create a copy of the data
    df_bar = df.copy()
    
    # Extract year and month
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()
    
    # Group by year and month
    df_bar_grouped = df_bar.groupby(['year', 'month'])['value'].mean().unstack()
    
    # Sort the columns (months)
    df_bar_grouped = df_bar_grouped.reindex(columns=[
        'January', 'February', 'March', 'April', 'May', 'June', 
        'July', 'August', 'September', 'October', 'November', 'December'
    ])
    
    # Plotting
    plt.figure(figsize=(12, 6))
    df_bar_grouped.plot(kind='bar', legend=True)
    plt.title('Average Page Views per Month by Year')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months')
    plt.tight_layout()
    plt.savefig('bar_plot.png')
    return plt

# 5. Draw box plot
def draw_box_plot():
    # Create a copy of the data
    df_box = df.copy()
    
    # Extract year and month
    df_box['year'] = df_box.index.year
    df_box['month'] = df_box.index.month
    
    # Convert month to a categorical type with proper ordering
    df_box['month'] = pd.Categorical(df_box['month'], categories=[
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
    ], ordered=True)
    
    # Set up the matplotlib figure
    plt.figure(figsize=(14, 6))
    
    # Year-wise box plot
    plt.subplot(1, 2, 1)
    sns.boxplot(x='year', y='value', data=df_box)
    plt.title('Year-wise Box Plot (Trend)')
    plt.xlabel('Year')
    plt.ylabel('Page Views')
    
    # Month-wise box plot
    plt.subplot(1, 2, 2)
    sns.boxplot(x='month', y='value', data=df_box)
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.xlabel('Month')
    plt.ylabel('Page Views')
    plt.xticks(ticks=range(12), labels=[
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    ])
    
    plt.tight_layout()
    plt.savefig('box_plot.png')
    return plt

# Do not modify the next two lines
if __name__ == "__main__":
    draw_line_plot()
    draw_bar_plot()
    draw_box_plot()
    plt.show()
