import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the dataset we generated

csv_path = os.path.join("data" , "accidents.csv")
df=pd.read_csv(csv_path)
print("First 10 rows of the dataset:")
print(df.head(10))

# Convert date/time
df['date'] = pd.to_datetime(df['date'])
df['time'] = pd.to_datetime(df['time'], format='%H:%M:%S')
df['hour'] = df['time'].dt.hour
df['day'] = df['date'].dt.day_name()

# Plot: Accidents by Hour
hourly = df['hour'].value_counts().sort_index()
plt.figure(figsize=(10,5))
plt.plot(hourly.index, hourly.values, marker='o')
plt.title("Accidents by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Number of Accidents")
plt.grid()
plt.show()

# Plot: Accidents by Day of Week
order = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
day_counts = df['day'].value_counts().reindex(order)

plt.figure(figsize=(8,5))
day_counts.plot(kind='bar', color='orange')
plt.title("Accidents by Day of Week")
plt.xlabel("Day")
plt.ylabel("Number of Accidents")
plt.show()

# High Risk Areas
area_counts = df['area'].value_counts().head(10)
plt.figure(figsize=(8,6))
area_counts.plot(kind='barh', color='red')
plt.title("Top 10 High Risk Areas")
plt.xlabel("Count")
plt.ylabel("Area")
plt.show()

# Heatmap: Day vs Hour
heatmap_data = df.pivot_table(
    index='day', columns='hour', values='id', aggfunc='count'
).reindex(order)

plt.figure(figsize=(14,6))
sns.heatmap(heatmap_data, cmap="Reds", linewidths=0.4)
plt.title("Accident Heatmap (Day vs Hour)")
plt.show()

# Trend Over Time
daily_trend = df.groupby('date').size()
plt.figure(figsize=(12,5))
plt.plot(daily_trend.index, daily_trend.values, marker='o', color='green')
plt.title("Accident Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Total Accidents")
plt.grid()
plt.show()
