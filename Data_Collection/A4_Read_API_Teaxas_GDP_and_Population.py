import numpy as np
import pandas as pd
import requests
import json
import time

#%% Biud URL
## https://fred.stlouisfed.org/series/TXRQGSP



def GetFREDdata(Series_Id):
    
    # API url
    API_key = 'XXX'
    URL_FREDdata = f'https://api.stlouisfed.org/fred/series/observations?series_id={Series_Id}&api_key={API_key}&file_type=json'

    # Get data
    resp = requests.get(url=URL_FREDdata)

    # Show main data structure
    # resp.json().keys()

    Data_Raw = pd.read_json( json.dumps( resp.json()['observations'] ) )
    Data = Data_Raw[['date', 'value']].set_index('date')
    
    return Data



Series_Id_GDP_Texas = 'TXRQGSP'
Series_Id_Population_Texas = 'TXPOP'

Real_GDP_Texas = GetFREDdata(Series_Id_GDP_Texas)
Population_Texas = GetFREDdata(Series_Id_Population_Texas)

# Population in x 1000, so:
Population_Texas['value'] = Population_Texas['value']\
                                .mul(1000)\
                                .astype('int')
                                

#%% write to csv

Real_GDP_Texas.to_csv('Real_GDP_Texas.csv')
Population_Texas.to_csv('Population_Texas.csv')



