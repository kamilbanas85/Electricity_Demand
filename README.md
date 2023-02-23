# Electricity Demand Forecasting for Texas

## About
The project presents forecasting an electricity demand in Texas with 1h frequency data. A focuse was made on a medium-term horizont (6 months). A muliple regresion models approach were used with few explanatory variables.

## Predcitors

A electricity is used in all area of our life. In residential is used to air-conditioning, heating, and to power house equipment, such as: TV, washing machine, kitchen devices, etc. In industry during production processes and also to air-conditioning. In serveices to power a devices, etc.  

<p align="center">
    <img src="https://user-images.githubusercontent.com/53495965/211201091-a3de9f5e-6fcb-40c1-8d63-d0b8c12dbe33.png" width=80% height=80%>
    
Fig. Electricity demand daily profile according with season (Source: https://learn.pjm.com/three-priorities/keeping-the-lights-on/how-energy-use-varies).

<p align="center">
    <img src="https://user-images.githubusercontent.com/53495965/211203111-c5ac464b-cd38-4c80-9430-5dcb941981c9.png" width=50% height=50%>
    
Fig. Comparison of daily load profiles for a year seasons.

A electricity usage in residential starts increasing in the morning around 5 a.m. People begin getting ready for work and school and, on a cold morning, turn the heat up, turn on the hot water or turn on the coffee maker. In the winter, usage typically declines between 8 a.m. and 5 p.m. once buildings have warmed up and outside temperatures begin to rise. During a summer peple turn on air-condition. At 5 p.m., when people are getting home, there is another spike in energy use as lights and appliances are turned on at multiple homes and outside temperatures decrease as the sun sets. Load starts dropping off again when people power down to go to bed for the night.

In a industry sector loead peak is during a working hours through working day. The value of load depends on season, bacouse air-condiction usege in offcie.

For the Texas region, summer and winter a working day load profiles are presented below:
    
<p align="center">
    <img src="https://user-images.githubusercontent.com/53495965/211215364-f5798cb3-3d4a-4ddf-be13-c2016ad99cdd.png" width=70% height=70%>

Fig. Summer and winter load profile for Texas.

Therefore, the atmospheric factor is one of the main influencing factors.

An electicity demand is influnced by;
- weather data (air-conditioning, electicity heating)
- population number
- economic activity - economy growth, etc...
- period of day - during during day peple and inductry use more electricity
- working day - industry use more
- period of year - during hlodiay industry use less, etc...

So, based of above as predictors are used fllowed variables:
- Weather data: air temperature, humidity, sky cover, wind speed
- Population
- Real GDP
- Dallas Fed Manufacturing Index
- Datetime indicatores: hour, day, week, month, working day


### Data Sources:
- #### Electricity Demand in Texas:

    The Demand data for Texas were fetched from EIA using API (https://www.eia.gov/opendata/v1/qb.php?category=3389948&sdid=EBA.TEX-ALL.D.H).  
    The script: https://github.com/kamilbanas85/Electricity_Demand/blob/main/Data_Collection/A2_Read_Data_Electricty_Demand.py 

- #### Wether:

    The Wether data were fetched from Open Meteo web using API (https://open-meteo.com/).  
    The script: https://github.com/kamilbanas85/Electricity_Demand/blob/main/Data_Collection/A3_Read_API_Weather_OpenMeteo.py

- #### Real GPD:

    The Real Gross Domestic Product (All Industry Total in Texas) data were fetched from Federal Reserve Economic Data (FRED) using API (https://fred.stlouisfed.org/series/TXRQGSP).  
    The script: https://github.com/kamilbanas85/Electricity_Demand/blob/main/Data_Collection/A4_Read_API_Teaxas_GDP_and_Population.py


- #### Population:

    The Population in Texas data were fetched from Federal Reserve Economic Data (FRED) using API (https://fred.stlouisfed.org/series/TXPOP).  
    The script: https://github.com/kamilbanas85/Electricity_Demand/blob/main/Data_Collection/A4_Read_API_Teaxas_GDP_and_Population.py


- #### Dallas Fed Manufacturing Index:

    The Dallas Fed Manufacturing Index data were fetched from Investing.com using 'investpy' python library.  
    The script: https://github.com/kamilbanas85/Electricity_Demand/blob/main/Data_Collection/A5_Read_Dallas_Fed_Manufacturing_Index.py

## Time period:

Models were fitted on data set beginning from 2015-07. A time period before Covid-19 was investigated, because lockdowns influence load profile (https://www.eia.gov/todayinenergy/detail.php?id=43295#tab1), so it requires additional consideration.

A summer and winter load profiles differs and models predicted those two region with diffrent accuracy, so a two test set were used to evaluate moldes. First, a model was trained to data till '2019-09' and tested on six month period to '2020-03' to cover a winter load profile. A second train set contains data to '2019-02' and a test set till '2019-08', what covers a summer time.    

### Data Preparation:

The data preparation: filling NAs, adjustment frequency to 'H', and merging different data sets are presented in:    https://github.com/kamilbanas85/Electricity_Demand/blob/main/Prepare_Predictors.ipynb
    
    
    
## Few models were conidered:
- Linear Regression
- ARDL
- ANN
- SVM
- drzewa
    
## Results:
  
  ### The Linear Regression model:
    I test set ( summer time):
      R2_adj: 0.81
      MAE:  2670.2
      MAPE: 6.49
    
    II test set ( winter time):
      R2_adj: 0.8858
      MAE:  2497.61
      MAPE: 5.9
    
  ### The ARDL model:
    I test set ( summer time):
      R2_adj: 0.8795
      MAE:  1934.6
      MAPE: 4.72
    
    II test set ( winter time):
      R2_adj: 0.9316
      MAE:  1780.18
      MAPE: 4.1
  
   ### The ANN model:
    I test set ( summer time):
      R2_adj: 0.8685
      MAE:  2000.5
      MAPE: 4.89
    
    II test set ( winter time):
      R2_adj: 0.923
      MAE:  1894.15
      MAPE: 4.47  

    
