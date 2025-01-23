import pandas as pd
import numpy as np
import random

# Load the station and travel time datasets
stations_df = pd.read_csv('DELHI_METRO_DATA.csv')
travel_times_df = pd.read_csv('dmrc_travel_times.csv')

# Define metro operation timings
start_time = pd.to_datetime("05:30 AM", format="%I:%M %p")
end_time = pd.to_datetime("11:30 PM", format="%I:%M %p")

# Generate all minutes in the metro operation timings
operation_minutes = pd.date_range(start=start_time, end=end_time, freq='1min').time

# Define days of the week and footfall multipliers for weekends vs weekdays
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekday_multiplier = 1.0
weekend_multiplier = 0.6  # Lower footfall on weekends

# Initialize a list to store the footfall data
footfall_data = []

# Total daily footfall range (between 5,00,000 and 35,00,000)
total_daily_footfall_range = (500000, 3500000)

# Assign each station a share of total footfall based on random weights
stations = stations_df['Station'].unique()
station_weights = np.random.dirichlet(np.ones(len(stations)), size=1).flatten()

# Generate footfall data for each station, day, and minute
for day in days_of_week:
    is_weekend = day in ['Saturday', 'Sunday']
    multiplier = weekend_multiplier if is_weekend else weekday_multiplier

    # Randomly determine total daily footfall within the range
    total_daily_footfall = random.randint(*total_daily_footfall_range)

    for station, weight in zip(stations, station_weights):
        station_daily_footfall = int(total_daily_footfall * weight * multiplier)

        # Distribute footfall over all minutes in the day
        minute_footfall = np.random.randint(13, 201, size=len(operation_minutes))
        minute_footfall = (minute_footfall / minute_footfall.sum()) * station_daily_footfall
        minute_footfall = minute_footfall.astype(int)  # Ensure integer values

        for minute, footfall in zip(operation_minutes, minute_footfall):
            footfall_data.append({
                "Day": day,
                "Station": station,
                "Time": minute,
                "Footfall": footfall
            })

# Convert the footfall data into a DataFrame
footfall_df = pd.DataFrame(footfall_data)

# Verify total daily footfall is within range
for day in days_of_week:
    total_footfall = footfall_df[footfall_df['Day'] == day]['Footfall'].sum()
    print(f"{day} - Total Footfall: {total_footfall}")

# Save to a CSV file
output_file = 'metro_footfall_data.csv'
footfall_df.to_csv(output_file, index=False)
print(f"Footfall data created and saved to {output_file}!")
