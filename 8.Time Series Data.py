import pandas as pd
import matplotlib.pyplot as plt

# Create a sample time series data
data = {
    'Date': pd.date_range(start='2023-01-01', periods=10, freq='D'),
    'Value': [10, 12, 15, 14, 13, 16, 18, 17, 19, 20]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Set the 'Date' column as the index
df.set_index('Date', inplace=True)

# Plot the time series
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Value'], marker='o', linestyle='-', color='b')
plt.title('Time Series Plot')
plt.xlabel('Date')
plt.ylabel('Value')
plt.grid()
plt.show()