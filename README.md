# Electricity Demand Forecasting for Texas

## About
A project presents forecasting an electricity demand in Texas. A focuse was made on a XshortXlongX-term horizont. A muliple regresion models approach were used with few independent variables.

## Predcitors

A electricity is used in all area of our life. In residential is used to air-conditioning, heating, and to power house equipment, such as: TV, washing machine, kitchen devices, etc. In industry during production processes and also to air-conditioning. In serveices to power a devices, etc.  

<p align="center">
    <img src="https://user-images.githubusercontent.com/53495965/211201091-a3de9f5e-6fcb-40c1-8d63-d0b8c12dbe33.png" width=80% height=80%>
    
Fig. Electricity demand daily profile according with season (Source: https://learn.pjm.com/three-priorities/keeping-the-lights-on/how-energy-use-varies).

<p align="center">
    <img src="https://user-images.githubusercontent.com/53495965/211203111-c5ac464b-cd38-4c80-9430-5dcb941981c9.png" width=50% height=50%>
    
Fig. Comparison of daily load profiles for year seasons.

A electricity usage in residential starts increasing in the morning around 5 a.m. People begin getting ready for work and school and, on a cold morning, turn the heat up, turn on the hot water or turn on the coffee maker. In the winter, usage typically declines between 8 a.m. and 5 p.m. once buildings have warmed up and outside temperatures begin to rise. During a summer peple turn on air-condition. At 5 p.m., when people are getting home, there is another spike in energy use as lights and appliances are turned on at multiple homes and outside temperatures decrease as the sun sets. Load starts dropping off again when people power down to go to bed for the night.

In a industry sector loead peak is during a working hours through working day. The value of load depends on season, bacouse air-condiction usege in offcie.

For the Texas region, summer and winter workig day load profiles are presented below:

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
- weather data: air_temperature 	humidity 	sky_cover 	wind_speed
- Population
- Real GDP
- Dallas Fed Manufacturing Index
- Datetime inidcatores: hour, day, week, month, working day


## Data Sources
- ### Electricity Demand in Texas:

    The Demand data for Texas were fetched from EIA using API (https://www.eia.gov/opendata/v1/qb.php?category=3389948&sdid=EBA.TEX-ALL.D.H). The script:  

- ### Wether:

    The Wether data were fetched from Open Meteo web using API (https://open-meteo.com/).

- ### Real GPD:

    The Real Gross Domestic Product (All Industry Total in Texas) data were fetched from Federal Reserve Economic Data (FRED) using API (https://fred.stlouisfed.org/series/TXRQGSP).


- ### Population:

    The Population in Texas data were fetched from Federal Reserve Economic Data (FRED) using API (https://fred.stlouisfed.org/series/TXPOP).

- ### Dallas Fed Manufacturing Index:

    The Dallas Fed Manufacturing Index data were fetched from Investing.com using 'investpy' python library.
    
## Forecast were divided for 2 period:
- pred Covid time
- post Covid (indlucid Covid time in training)

## Few models were conidered:
- Linear Regression
- ADL
- ANN
- SVM
- drzewa
