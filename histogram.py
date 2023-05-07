"""
1. The code imports two libraries, pandas and matplotlib.pyplot.
2. The code defines a function named "adjust_time" that takes a time string in the format
"HH:MM" and converts it to the corresponding 24-hour time.
3. The code defines a function named "histogram" that reads a CSV file named "trips_data.csv"
into a pandas dataframe, filters it for successful trips, and creates a histogram of the arrival times by hour of the day.
4. The "adjust_time" function is used to adjust the time format of the "APtime1" column in the pandas dataframe.
5. Finally, the "histogram" function is called to create a histogram using matplotlib.pyplot.
"""

import pandas as pd
import matplotlib.pyplot as plt


# This function converts any time greater than or equal to 24 hrs format to corresponding 24 hr time.
# eg: 31 HRS was re-calculated to 7:00 HRS
# eg: 46 HRS was re-calculated to 22:00 HRS
def adjust_time(time_str):
    hour, minute = map(int, time_str.split(':'))
    hour = hour % 24
    return f'{hour:02d}:{minute:02d}'

def histogram():
    # read the CSV file into a pandas dataframe
    df = pd.read_csv('trips_data.csv')

    # filter for successful trips
    success_df = df[df['Status'] == 'S']

    success_df['APtime1'] = success_df['APtime1'].apply(adjust_time)
    success_df['ArrivalHour'] = pd.to_datetime(success_df['APtime1']).dt.hour

    # create histogram
    plt.hist(success_df['ArrivalHour'], bins=50)
    plt.xlabel('Hour of the day')
    plt.ylabel('Number of successful trips')
    plt.title('Arrival times by hour of the day')
    plt.show()