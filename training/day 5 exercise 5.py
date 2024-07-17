import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('timeseries.csv', parse_dates=['Date'])

# Display the first few rows of the dataset
print(df.head())

# Create a line plot
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Value'], marker='o', linestyle='-')

# Add title and labels
plt.title('Time Series Trend')
plt.xlabel('Date')
plt.ylabel('Value')

# Display grid
plt.grid(True)

# Display the plot
plt.show()