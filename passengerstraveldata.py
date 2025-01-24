# # import pandas as pd
# # import numpy as np
# # from datetime import datetime, timedelta
# # import random

# # # Load the CSV files
# # metro_data_path = 'DELHI_METRO_DATA.csv'
# # travel_times_path = 'dmrc_all_station_travel_times.csv'
# # footfall_data_path = 'dmrc_footfall_data.csv'

# # metro_data = pd.read_csv(metro_data_path)
# # travel_times = pd.read_csv(travel_times_path)
# # footfall_data = pd.read_csv(footfall_data_path)

# # # Define peak and off-peak hours
# # peak_hours_morning = (datetime.strptime("08:00", "%H:%M"), datetime.strptime("10:00", "%H:%M"))
# # peak_hours_evening = (datetime.strptime("17:00", "%H:%M"), datetime.strptime("20:00", "%H:%M"))

# # # Get all days of the week
# # days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# # # Initialize the result list
# # passenger_data = []

# # # Function to check if a given time is within peak hours
# # def is_peak_hour(time):
# #     return peak_hours_morning[0] <= time <= peak_hours_morning[1] or peak_hours_evening[0] <= time <= peak_hours_evening[1]

# # # Function to generate passenger count
# # def generate_passenger_count(start_footfall, end_footfall, time, day):
# #     base_count = (start_footfall + end_footfall) // 2
# #     if day in ["Saturday", "Sunday"]:
# #         base_count = int(base_count * 0.7)  # Reduce footfall by 30% on weekends

# #     if is_peak_hour(time):
# #         passengers = random.randint(int(base_count * 0.8), min(base_count, 200))
# #     else:
# #         passengers = random.randint(13, min(int(base_count * 0.5), 200))
    
# #     return passengers

# # # Iterate through each permutation of stations and each minute
# # for index, row in travel_times.iterrows():
# #     start_station = row['Start Station']
# #     end_station = row['End Station']
# #     line = row['Start Line']
    
# #     for day in days_of_week:
# #         daily_footfall_start = footfall_data[(footfall_data['Station'] == start_station) & (footfall_data['Date'].str.contains(day))]
# #         daily_footfall_end = footfall_data[(footfall_data['Station'] == end_station) & (footfall_data['Date'].str.contains(day))]
        
# #         for _, start_footfall_row in daily_footfall_start.iterrows():
# #             time_str = start_footfall_row['Time']
# #             time = datetime.strptime(time_str, "%H:%M")
# #             start_footfall = start_footfall_row['Footfall']
            
# #             end_footfall_row = daily_footfall_end[daily_footfall_end['Time'] == time_str]
            
# #             if not end_footfall_row.empty:
# #                 end_footfall = end_footfall_row.iloc[0]['Footfall']
# #                 passengers = generate_passenger_count(start_footfall, end_footfall, time, day)
                
# #                 passenger_data.append({
# #                     "Start Station": start_station,
# #                     "End Station": end_station,
# #                     "Line": line,
# #                     "Day": day,
# #                     "Time": time_str,
# #                     "Passengers": passengers
# #                 })

# # # Convert to DataFrame
# # passenger_df = pd.DataFrame(passenger_data)

# # # Save to CSV
# # output_path = 'dmrc_passenger_data.csv'
# # passenger_df.to_csv(output_path, index=False)

# # print(f"Passenger data generated and saved to '{output_path}'")

# import pandas as pd
# import numpy as np
# from datetime import datetime, timedelta
# import random

# # Load the CSV files
# metro_data_path = '/home/shatrughan-shukla/Desktop/CODEEE/DELHI_METRO_DATA.csv'
# travel_times_path = '/home/shatrughan-shukla/Desktop/CODEEE/dmrc_all_station_travel_times.csv'
# footfall_data_path = '/home/shatrughan-shukla/Desktop/CODEEE/dmrc_footfall_data.csv'

# metro_data = pd.read_csv(metro_data_path)
# travel_times = pd.read_csv(travel_times_path)
# footfall_data = pd.read_csv(footfall_data_path)

# # Define peak and off-peak hours
# peak_hours_morning = (datetime.strptime("08:00", "%H:%M"), datetime.strptime("10:00", "%H:%M"))
# peak_hours_evening = (datetime.strptime("17:00", "%H:%M"), datetime.strptime("20:00", "%H:%M"))

# # Get all days of the week
# days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# # Initialize the output file
# output_path = '/home/shatrughan-shukla/Desktop/CODEEE/dmrc_passenger_data.csv'
# with open(output_path, 'w') as f:
#     f.write("Start Station,End Station,Line,Day,Time,Passengers\n")

# # Function to check if a given time is within peak hours
# def is_peak_hour(time):
#     return peak_hours_morning[0] <= time <= peak_hours_morning[1] or peak_hours_evening[0] <= time <= peak_hours_evening[1]

# # Function to generate passenger count
# def generate_passenger_count(start_footfall, end_footfall, time, day):
#     base_count = (start_footfall + end_footfall) // 2
#     if day in ["Saturday", "Sunday"]:
#         base_count = int(base_count * 0.7)  # Reduce footfall by 30% on weekends

#     if is_peak_hour(time):
#         passengers = random.randint(int(base_count * 0.8), min(base_count, 200))
#     else:
#         passengers = random.randint(13, min(int(base_count * 0.5), 200))
    
#     return passengers

# # Process data in chunks
# chunk_size = 100  # Adjust this size based on your memory capacity
# num_chunks = len(travel_times) // chunk_size + 1

# for chunk in range(num_chunks):
#     start_index = chunk * chunk_size
#     end_index = min((chunk + 1) * chunk_size, len(travel_times))
#     travel_times_chunk = travel_times[start_index:end_index]
    
#     passenger_data_chunk = []

#     for index, row in travel_times_chunk.iterrows():
#         start_station = row['Start Station']
#         end_station = row['End Station']
#         line = row['Start Line']
        
#         for day in days_of_week:
#             daily_footfall_start = footfall_data[(footfall_data['Station'] == start_station) & (footfall_data['Date'].str.contains(day))]
#             daily_footfall_end = footfall_data[(footfall_data['Station'] == end_station) & (footfall_data['Date'].str.contains(day))]
            
#             for _, start_footfall_row in daily_footfall_start.iterrows():
#                 time_str = start_footfall_row['Time']
#                 time = datetime.strptime(time_str, "%H:%M")
#                 start_footfall = start_footfall_row['Footfall']
                
#                 end_footfall_row = daily_footfall_end[daily_footfall_end['Time'] == time_str]
                
#                 if not end_footfall_row.empty:
#                     end_footfall = end_footfall_row.iloc[0]['Footfall']
#                     passengers = generate_passenger_count(start_footfall, end_footfall, time, day)
                    
#                     passenger_data_chunk.append({
#                         "Start Station": start_station,
#                         "End Station": end_station,
#                         "Line": line,
#                         "Day": day,
#                         "Time": time_str,
#                         "Passengers": passengers
#                     })
    
#     # Convert to DataFrame and append to the output CSV file
#     passenger_df_chunk = pd.DataFrame(passenger_data_chunk)
#     passenger_df_chunk.to_csv(output_path, mode='a', header=False, index=False)

# print(f"Passenger data generated and saved to '{output_path}'")

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Load the CSV files
metro_data_path = '/home/shatrughan-shukla/Desktop/CODEEE/DELHI_METRO_DATA.csv'
travel_times_path = '/home/shatrughan-shukla/Desktop/CODEEE/dmrc_all_station_travel_times.csv'
footfall_data_path = '/home/shatrughan-shukla/Desktop/CODEEE/dmrc_footfall_data.csv'

metro_data = pd.read_csv(metro_data_path)
travel_times = pd.read_csv(travel_times_path)
footfall_data = pd.read_csv(footfall_data_path)

# Define peak and off-peak hours
peak_hours_morning = (datetime.strptime("08:00", "%H:%M"), datetime.strptime("10:00", "%H:%M"))
peak_hours_evening = (datetime.strptime("17:00", "%H:%M"), datetime.strptime("20:00", "%H:%M"))

# Get all days of the week
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Initialize the output file
output_path = '/home/shatrughan-shukla/Desktop/CODEEE/dmrc_passenger_data.csv'
with open(output_path, 'w') as f:
    f.write("Start Station,End Station,Line,Day,Time,Passengers\n")

# Function to check if a given time is within peak hours
def is_peak_hour(time):
    return peak_hours_morning[0] <= time <= peak_hours_morning[1] or peak_hours_evening[0] <= time <= peak_hours_evening[1]

# Function to generate passenger count
def generate_passenger_count(start_footfall, end_footfall, time, day):
    base_count = (start_footfall + end_footfall) // 2
    if day in ["Saturday", "Sunday"]:
        base_count = int(base_count * 0.7)  # Reduce footfall by 30% on weekends

    if is_peak_hour(time):
        passengers = random.randint(int(base_count * 0.8), min(base_count, 200))
    else:
        passengers = random.randint(13, min(int(base_count * 0.5), 200))
    
    return passengers

# Process data in chunks
chunk_size = 100  # Adjust this size based on your memory capacity
num_chunks = len(travel_times) // chunk_size + 1

for chunk in range(num_chunks):
    start_index = chunk * chunk_size
    end_index = min((chunk + 1) * chunk_size, len(travel_times))
    travel_times_chunk = travel_times[start_index:end_index]
    
    passenger_data_chunk = []

    for index, row in travel_times_chunk.iterrows():
        start_station = row['Start Station']
        end_station = row['End Station']
        line = row['Start Line']
        
        for day in days_of_week:
            daily_footfall_start = footfall_data[(footfall_data['Station'] == start_station) & (footfall_data['Date'].str.contains(day))]
            daily_footfall_end = footfall_data[(footfall_data['Station'] == end_station) & (footfall_data['Date'].str.contains(day))]
            
            for _, start_footfall_row in daily_footfall_start.iterrows():
                time_str = start_footfall_row['Time']
                time = datetime.strptime(time_str, "%H:%M")
                start_footfall = start_footfall_row['Footfall']
                
                end_footfall_row = daily_footfall_end[daily_footfall_end['Time'] == time_str]
                
                if not end_footfall_row.empty:
                    end_footfall = end_footfall_row.iloc[0]['Footfall']
                    passengers = generate_passenger_count(start_footfall, end_footfall, time, day)
                    
                    passenger_data_chunk.append({
                        "Start Station": start_station,
                        "End Station": end_station,
                        "Line": line,
                        "Day": day,
                        "Time": time_str,
                        "Passengers": passengers
                    })
    
    # Convert to DataFrame and append to the output CSV file
    passenger_df_chunk = pd.DataFrame(passenger_data_chunk)
    passenger_df_chunk.to_csv(output_path, mode='a', header=False, index=False)

print(f"Passenger data generated and saved to '{output_path}'")