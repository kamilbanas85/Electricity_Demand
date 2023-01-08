import numpy as np
import pandas as pd
import requests
import json
import time

import datetime

#%% Biud URL

latitude = 30.1900
longitude=-97.6687

endDate = (datetime.datetime.now().date() - pd.Timedelta(days=2)) .strftime('%Y-%m-%d')

TimeZone = 'auto'

open_meteo_History_API_url = \
f'https://archive-api.open-meteo.com/v1/era5?latitude={latitude}&longitude={longitude}&start_date=2010-01-01&end_date={endDate}&hourly=temperature_2m,relativehumidity_2m,apparent_temperature,cloudcover,shortwave_radiation,windspeed_10m,winddirection_10m&timezone={TimeZone}'


#%% Call API

# Get data
resp = requests.get(url=open_meteo_History_API_url)

# Show main data structure
# resp.json().keys()

Data_Raw = pd.read_json( json.dumps( resp.json()['hourly'] ) )


#%% Basic Process Data

# Data_Raw.columns
# Data_Raw.info()

OpenMeteo = Data_Raw.rename(columns = {'time':'dateTime',
                                       'temperature_2m':'air_temperature',
                                       'relativehumidity_2m':'humidity',
                                       'cloudcover':'sky_cover',
                                       'windspeed_10m':'wind_speed',
                                       'winddirection_10m':'wind_direction'})\
               .assign(dateTime = lambda x: pd.to_datetime(x['dateTime']) )\
               .sort_values('dateTime')\
               .set_index('dateTime')

OpenMeteo = OpenMeteo.dropna(how='all')



def checkIfMissingDateTime(DF, freq = 'H'):
    
    return pd.date_range(DF.index.min(), DF.index.max(), freq=freq).difference(DF.index)


checkIfMissingDateTime(OpenMeteo, 'H')



#%% Write to csv

OpenMeteo.to_csv('Austin_wheather_data_OpenMeteo.csv')



