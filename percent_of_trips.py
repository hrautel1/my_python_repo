"""
This code is used to analyze data from a CSV file containing trip records, and
calculate the percentage of trips by mode and weekday/weekend. The resulting data is written to an Excel file.
1. The code reads data from a CSV file named "trips.csv" using the pandas library.
2. It processes the data by converting the "Tripdate" column to a datetime format, and creating a new column to
indicate whether the date falls on a weekday or weekend.
3. It calculates the number and percentage of trips by mode (Primary, Broker, and E-Hail) and weekday/weekend.
4. It creates a table containing the calculated data and writes it to a new sheet named "question_1_part_3"
in an Excel file named "SUMMARY_OUTPUTS.xlsx" using the openpyxl library.
5. The table is formatted to include column widths, text alignment, and merged cells for the row and column headers.
"""

import pandas as pd
from openpyxl.styles import Alignment

def percentage_by_mode():
    # Load the CSV file into a pandas dataframe
    df = pd.read_csv('trips.csv')

    # Convert the "Tripdate" column to datetime format
    df['Tripdate'] = pd.to_datetime(df['Tripdate'])

    # Create a new column to indicate whether the date falls on a weekday or weekend
    df['Weekday/Weekend'] = df['Tripdate'].dt.weekday.apply(lambda x: 'Weekday (M to F)' if x < 5 else 'Weekend (Sa & Su)')

    # Calculate the total number of trips
    total_trips = len(df)

    # Calculate the number of trips by mode and weekday/weekend
    primary_weekday_trips = len(df[(df['ProviderType'] == 'Primary') & (df['Weekday/Weekend'] == 'Weekday (M to F)')])
    primary_weekend_trips = len(df[(df['ProviderType'] == 'Primary') & (df['Weekday/Weekend'] == 'Weekend (Sa & Su)')])
    broker_weekday_trips = len(df[(df['ProviderType'] == 'Broker') & (df['Weekday/Weekend'] == 'Weekday (M to F)')])
    broker_weekend_trips = len(df[(df['ProviderType'] == 'Broker') & (df['Weekday/Weekend'] == 'Weekend (Sa & Su)')])
    ehail_weekday_trips = len(df[(df['ProviderType'] == 'E-Hail') & (df['Weekday/Weekend'] == 'Weekday (M to F)')])
    ehail_weekend_trips = len(df[(df['ProviderType'] == 'E-Hail') & (df['Weekday/Weekend'] == 'Weekend (Sa & Su)')])

    # Calculate the percentage of trips by mode and weekday/weekend
    primary_weekday_pct = round((primary_weekday_trips / total_trips) * 100, 2)
    primary_weekend_pct = round((primary_weekend_trips / total_trips) * 100, 2)
    broker_weekday_pct = round((broker_weekday_trips / total_trips) * 100, 2)
    broker_weekend_pct = round((broker_weekend_trips / total_trips) * 100, 2)
    ehail_weekday_pct = round((ehail_weekday_trips / total_trips) * 100, 2)
    ehail_weekend_pct = round((ehail_weekend_trips / total_trips) * 100, 2)

    # Create and fill the data
    data = {'': ['Weekday (M to F)', 'Weekend (Sa & Su)', 'Total'],
            'Primary': [f'{primary_weekday_pct}', f'{primary_weekend_pct}', float(f'{primary_weekend_pct}') + float(f'{primary_weekend_pct}')],
            'Broker': [f'{broker_weekday_pct}', f'{broker_weekend_pct}', float(f'{broker_weekday_pct}') + float(f'{broker_weekend_pct}')],
            'E-Hail': [f'{ehail_weekday_pct}', f'{ehail_weekend_pct}', float(f'{ehail_weekday_pct}') + float(f'{ehail_weekend_pct}')],
            'Total': [float(f'{primary_weekday_pct}') + float(f'{broker_weekday_pct}') + float(f'{ehail_weekday_pct}'), float(f'{primary_weekend_pct}') + float(f'{broker_weekend_pct}') + float(f'{ehail_weekend_pct}'),
                    float(f'{primary_weekday_pct}') + float(f'{broker_weekday_pct}') + float(f'{ehail_weekday_pct}') + float(f'{primary_weekend_pct}') + float(f'{broker_weekend_pct}') + float(f'{ehail_weekend_pct}')]}
    
    with pd.ExcelWriter('SUMMARY_OUTPUTS.xlsx', engine='openpyxl', mode='a') as writer:
        if 'question_1_part_3' in writer.book.sheetnames:
            # If the sheet already exists, remove it
            writer.book.remove(writer.book['question_1_part_3'])
        table_df = pd.DataFrame(data)
        table_df.to_excel(writer, sheet_name='question_1_part_3', index=True, header=True)
        worksheet = writer.sheets['question_1_part_3']
        for col in worksheet.columns:
            column = col[0].column_letter
            col_width = worksheet.column_dimensions[column].width
            worksheet.column_dimensions[column].width = 4 + col_width
        for cell in worksheet['A1:E4']:
            for c in cell:
                c.alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)