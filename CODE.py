"""
    The code below is a Python script that imports five separate modules to perform various calculations and generate tables and visualizations related to Paratransit service.
    The first line of the code imports the "total_successful_trip" module, which is responsible for calculating and displaying the total number of successful trips.
    The second line imports the "avg_trips_per_day" module, which calculates and displays the average number of trips per day.
    The third line imports the "percent_of_trips" module, which calculates and displays the percentage of trips by mode (i.e., provider type) for both weekdays and weekends.
    The fourth line imports the "histogram" module, which generates a histogram to profile arrival times by hour of the day for all successful trips.
    The fifth line imports the "top_geographic_score" module, which generates a table of the top 10 ZIP codes by the count of successful "Primary" trip pickups occurring in the AM rush hour.
"""

import total_successful_trip
import avg_trips_per_day
import percent_of_trips
import histogram
import top_geographic_score

if __name__ == '__main__':
    total_successful_trip.total_trips()
    avg_trips_per_day.average_trips()
    percent_of_trips.percentage_by_mode()
    top_geographic_score.top_geographic_score()
    histogram.histogram()