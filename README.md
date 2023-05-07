How to run this project:
	1. First run the requirements.txt file which has the necessary python modules to run the CODE.py file
	$ pip3 install -r requirements.txt
	
	2. Run the CODE.py file
	$ python3 CODE.py
	* A histogram will be displayed on the screen, press any keyboard key to exit the histogram window
	* A .xlsx file namely SUMMARY_OUTPUTS.xlsx file will be created with specific sheet of the questions.

1. Some fields in the trip.csv file need some modifications like the 'ProviderType' should be one of 'E-Hail', 'Primary', 'Broker' but I encountered 'Test Record', 'Deleted', 'Driver break record' which I suppose was necessary as per the condition of that particular trip. I have handled such cases in the 'total_successful_trip.py' file.


2. The 'Outcome' cell is handled as well (for Outcome == 'Fixed Route-Exclude')

3. To plot a histogram, I was calculating the time difference between arrival time, which I was comming out to be negative (-22). I have taken care of that part by copying the data from 'trips.csv' to a new file called 'trips_data.csv'

4. The 2nd question do not require a sheet in the SUMMARY_OUTPUTS.xlsx file. That question is coded in 'histogram.py' file which plots a histogram (run the files in VS code)
