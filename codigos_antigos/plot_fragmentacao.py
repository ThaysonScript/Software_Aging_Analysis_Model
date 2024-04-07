import pandas as pd

base_folder = './data_logs/logs/fragmentation.csv'
minimum = 4

# Read the CSV file into a DataFrame
df = pd.read_csv(base_folder, delimiter=';')

# Convert the datetime column to a datetime object
df['datetime'] = pd.to_datetime(df['datetime'])

# Set the index to the datetime column
df = df.set_index('datetime')

df['time_passed'] = (df.index - df.index[0]).total_seconds() / 3600

# Resetting the index to use 'time_passed' as index
df = df.set_index('time_passed')

df_filtered = df[df['process_occurrences'] >= minimum]

df_pivot = df_filtered.pivot(columns='process', values='process_occurrences')
ax = df_pivot.plot(ylabel='Process occurrences', xlabel='Time(H)')

# Save the figure
fig = ax.get_figure()
fig.savefig(f'./plot_images/fragmentation.png')
