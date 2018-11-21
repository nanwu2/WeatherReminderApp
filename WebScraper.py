import datetime
import pandas as pd
import numpy as np
from datetime import datetime as dt
import re

start_time = input('What time do you start your day? ')
end_time = input('What time do you end your day? ')

start_time = dt.strptime(start_time, '%H:%M').time()
end_time = dt.strptime(end_time, '%H:%M').time()

today = datetime.datetime.today().strftime('%d %B %Y')
tomorrow = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d %B %Y')

url = "https://weather.gc.ca/forecast/hourly/bc-74_metric_e.html"
pd_table = pd.read_html(url, header=0)[0]
pd_table.columns = ['Time', 'Temp', 'Weather Conditions', 'Likelihood of Precip', 'Wind (km/h)']

cutoff = pd_table.index[pd_table['Time'] == tomorrow].tolist()[0]

curr_table = pd_table.iloc[1:cutoff,:]

curr_table.loc[:,'Time'] = pd.to_datetime(curr_table['Time'], format='%H:%M').dt.time

user_times = curr_table[(curr_table['Time'] >= start_time) & (curr_table['Time'] <= end_time)]

if ('High' in str(user_times['Likelihood of Precip'])) & (('Showers' in str(user_times['Weather Conditions'])) | ('showers' in str(user_times['Weather Conditions']))):
    print('Bring your umbrella and wear rain boots')
elif ('Medium' in str(user_times['Likelihood of Precip'])) & (('Showers' in str(user_times['Weather Conditions'])) | ('showers' in str(user_times['Weather Conditions']))):
    print('Bring your umbrella')
else:
    print("Don't need your umbrella today")
