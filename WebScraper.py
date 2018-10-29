import datetime
import pandas as pd
import numpy as np
from datetime import datetime as dt

start_time = input('What time do you start your day? ')
end_time = input('What time do you end your day? ')

start_time = dt.strptime(start_time, '%H:%M')
end_time = dt.strptime(end_time, '%H:%M')

today = datetime.datetime.today().strftime('%d %B %Y')
tomorrow = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d %B %Y')

url = "https://weather.gc.ca/forecast/hourly/bc-74_metric_e.html"
pd_table = pd.read_html(url, header=0)[0]
pd_table.columns = ['Time', 'Temp', 'Weather Conditions', 'Likelihood of Precip', 'Wind (km/h)']

cutoff = pd_table.index[pd_table['Time'] == tomorrow].tolist()[0]

curr_table = pd_table.iloc[1:cutoff,:]

print(curr_table)
#
# curr_table['Time'] = pd.to_datetime(curr_table['Time'])
#
# user_times = curr_table[(curr_table['Time'] >= start_time) & (curr_table['Time'] <= end_time)]
# print(user_times)

# print(len(rows))
# print(rows[0:8])



# print(len(columns))
# print(columns[0:2])

# print(soup.prettify())