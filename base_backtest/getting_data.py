# getting_data.py
"""
This code simply gets data from Google or Yahoo Finance
Input: symbols (list), start and end time
Output: CSV files that contain the time series of a stock for each symbol in the list
"""

# For compatibility with Py2 and Py3
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

# Import necessary functions
import datetime
import pandas as pd
import pandas_datareader.data as web
import sys

# Check Python and Pandas version
print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)

# Inputs
today = datetime.date.today()
symbols = ['SPY', 'MAR', 'AMZN']
site = 'google'  # Options: google, yahoo, etc.
start = datetime.datetime(2017, 1, 1)
end = today  # Or we use "end = datetime.datetime(2017, 8, 17)" for example

if __name__ == "__main__":
    for s in symbols:
        # Getting the data
        data = web.DataReader(s, site, start, end)
        # Set the file name
        filename = s + ".csv"
        # Write to CSV file
        pd.DataFrame.to_csv(data, filename)
    print('Done.')