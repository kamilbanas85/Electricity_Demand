import numpy as np
import pandas as pd


import datetime
import investpy

#%% Biud URL
## Comparision diffrent index:
# https://seekingalpha.com/article/4561025-dallas-fed-manufacturing-growth-declines-in-november

#  Dallas Fed Manufacturing Index
# https://tradingeconomics.com/united-states/dallas-fed-manufacturing-index

# Texas Manufacturing Business Activity Index 
# https://ycharts.com/indicators/texas_manufacturing_business_activity_index

# Houston PMI
# https://www.ism-houston.org/ism-houston-business-report-february-2022/
# https://www.houston.org/houston-data/monthly-update-purchasing-managers-index

# US ISM Manufacturing PMI 
# https://ycharts.com/indicators/us_pmi

#  Industrial Production: Total Index
# https://fred.stlouisfed.org/series/INDPRO



Dallas_Fed_Manufacturing_Index_Raw = []

year = 2015
while year <= datetime.datetime.now().year:
    
    # fatch data form investopedia
    dataCarrentYear = investpy.economic_calendar(from_date=f'01/01/{year}', to_date=f'31/12/{year}', countries = ['united states'] )
    
    # extract data containg sentence 'Dallas Fed Mfg Business Index' in event column:
    ExtractedData = dataCarrentYear[dataCarrentYear['event'].str.contains('Dallas Fed Mfg Business Index')]
    
    # append to results
    Dallas_Fed_Manufacturing_Index_Raw.append(ExtractedData)

    year+=1


# Build finall data
Dallas_Fed_Manufacturing_Index_Raw = pd.concat(Dallas_Fed_Manufacturing_Index_Raw, axis =0)

#%%  Process data

Dallas_Fed_Manufacturing_Index = Dallas_Fed_Manufacturing_Index_Raw[['date','event','actual', 'previous']]\
                                    .rename(columns = {'actual':'value'})

# Convert to datetime 'date' column and 'value' and 'previous' to numeric
Dallas_Fed_Manufacturing_Index = Dallas_Fed_Manufacturing_Index\
                                    .assign(date = lambda x: pd.to_datetime(x['date'], format = '%d/%m/%Y'),
                                            value = lambda x: pd.to_numeric(x['value']),
                                            previous = lambda x: pd.to_numeric(x['previous'])  
                                            )


# Offset date to proper month and than to start of the month
Dallas_Fed_Manufacturing_Index['date'] = Dallas_Fed_Manufacturing_Index['date'] - pd.Timedelta("5D")
Dallas_Fed_Manufacturing_Index['date'] = Dallas_Fed_Manufacturing_Index['date'] - pd.offsets.MonthBegin(1)

Dallas_Fed_Manufacturing_Index = Dallas_Fed_Manufacturing_Index.set_index('date')


#%% Write to csv


Dallas_Fed_Manufacturing_Index[['value']].to_csv('Dallas_Fed_Manufacturing_Index.csv')

