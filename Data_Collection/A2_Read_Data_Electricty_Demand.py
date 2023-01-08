import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import os

MainDirectory = os.path.abspath(os.path.dirname(__file__))
os.chdir(MainDirectory)

from A1_TakeEIAdataBySeriesID import *


#%% Read EIA data

##   Electricity DEMAND for USA general:
##   https://www.eia.gov/opendata/qb.php?category=2122628


## Demand for United States Lower 48 (region), hourly - UTC time:
##   series_id=EBA.US48-ALL.D.H
##
## https://www.eia.gov/opendata/qb.php?category=3389935&sdid=EBA.US48-ALL.D.H


## Demand for Texas (region), hourly - UTC time:
##   series_id=EBA.TEX-ALL.D.H
## 
## https://www.eia.gov/opendata/qb.php?category=3389948&sdid=EBA.TEX-ALL.D.H


## Demand for California (region), hourly - UTC time:
##   series_id=EBA.CAL-ALL.D.H
## 
## https://www.eia.gov/opendata/qb.php?category=3389936&sdid=EBA.CAL-ALL.D.H


### Take data based on series id:
    
api_key = "XXX"
series_ID='EBA.US48-ALL.D.H'

ElectricityDemandUSA_Main = EIAtakeDataBySeriesID(api_key, series_ID)

ElectricityDemandUSA = ElectricityDemandUSA_Main.TakeTimeSeries()


#ElectricityDemandUSA.plot()

#%% Take data for Texas

series_ID='EBA.TEX-ALL.D.H'

ElectricityDemandTexas_Main = EIAtakeDataBySeriesID(api_key, series_ID)

ElectricityDemandTexas = ElectricityDemandTexas_Main.TakeTimeSeries()

#ElectricityDemandTexas.plot()


#%% Write to csv

ElectricityDemandTexas.reset_index().to_csv('Electricity_Demand_Texas_data.csv', index=False)
