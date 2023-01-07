# Electricity Demand Forecasting for Austin, TX

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
**- Demand data:***

Demand Data were downloaded from ...

***- Wether data:***

Wether Data

***- Real GPD data:***

Real GPD vvv

## Forecast were divided for 2 period:
- pred Covid time
- post Covid (indlucid Covid time in training)

## Few models were conidered:
- Linear Regression
- ADL
- ANN
- SVM
- drzewa
