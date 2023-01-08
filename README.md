# Electricity Demand Forecasting for Texas

## About
A project presents forecasting an electricity demand in Texas. A focuse was made on a XshortXlongX-term horizont. A muliple regresion models approach were used with few independent variables.

## Predcitors

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


## Data Source
- ### Demand data:

    The Demand data for Texas were fetched from EIA using API (https://www.eia.gov/opendata/v1/qb.php?category=3389948&sdid=EBA.TEX-ALL.D.H).

- ### Wether data:

    The Wether data were fetched from Open Meteo web using API (https://open-meteo.com/).

- ### Real GPD data:

    The Real Gross Domestic Product (All Industry Total in Texas) data were fetched from Federal Reserve Economic Data (FRED) using API (https://fred.stlouisfed.org/series/TXRQGSP).


- ### Population data:

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
