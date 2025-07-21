import numpy as np
import pandas as pd
import os
import requests
import matplotlib.pyplot as plt
import statsmodels.api as sm


from tensorflow.keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV, TimeSeriesSplit
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, mean_squared_error


MainDirectory = os.path.abspath(os.path.dirname(__file__))
os.chdir(MainDirectory)

#%% Function to extract code from GitHub

def GetGitHubCode(GitUrl):

    response = requests.get(GitUrl) #get data from json file located at specified URL 

    if response.status_code == requests.codes.ok:
        contentOfUrl = response.content
        exec(contentOfUrl, globals() )
    else:
        print('Content was not found.')

#%% Download functions from GitHub:

GitUrl__Prepare_Data_For_Regression = 'https://raw.githubusercontent.com/kamilbanas85/Phyton_usefull_functions/main/Prepare_Data_For_Regression.py'
GetGitHubCode(GitUrl__Prepare_Data_For_Regression)

GitUrl__Make_TS_Regression = 'https://raw.githubusercontent.com/kamilbanas85/Phyton_usefull_functions/main/Make_TS_Regression.py'
GetGitHubCode(GitUrl__Make_TS_Regression)

GitUrl__Goodness_Of_Fit = 'https://raw.githubusercontent.com/kamilbanas85/Phyton_usefull_functions/main/Goodness_Of_Fit.py'
GetGitHubCode(GitUrl__Goodness_Of_Fit)

GitUrl__Multicollinearity_Check_Functions = 'https://raw.githubusercontent.com/kamilbanas85/Phyton_usefull_functions/main/Multicollinearity_Check_Functions.py'
GetGitHubCode(GitUrl__Multicollinearity_Check_Functions)

GitUrl__Feature_Selection = 'https://raw.githubusercontent.com/kamilbanas85/Phyton_usefull_functions/main/Feature_Selection.py'
GetGitHubCode(GitUrl__Feature_Selection)

GitUrl__ANN_Keras_functions = 'https://raw.githubusercontent.com/kamilbanas85/Phyton_usefull_functions/main/ANN_Keras_functions.py'
GetGitHubCode(GitUrl__ANN_Keras_functions)


#################################################################
#################################################################
#################################################################
#%% Downolad AnalysisData:

AnalysisData = pd.read_csv('AnalysisDF.csv',
                           parse_dates =['Date'],
                           index_col = 'Date')



#%% Cut data to pre-Covid time


AnalysisData = AnalysisData.loc[:'2020-02']
#AnalysisData = AnalysisData.loc[:'2019-09']


#################################################################
#################################################################
#################################################################
#%% Select Main Data
Dependent_Var = 'Demand'

Independent_Vars = ['HDD',
                    'CDD',
                    'wind_speed',
                    'humidity',
                    'sky_cover',
#                   'Population',
                    'RealGDP',
                    'DallasFedManufIndex',
                    'WorkDay',
                    'hour',
#                   'day',
                    'week'
#                   'month'
                   ]

DummyForColumn = ['hour','week']
LagList = None


### Cut data to pre-Covid time and crate 2 datasets to show diffrence between a summer and winter predictions
###################

###################
#%% '01' model on summer time
###################
            
AnalysisData_01 = AnalysisData.loc[:'2019-07']   

TestSetDate_01 = '2019-02'


X_01, y_01 =  DevideOnXandY_CreateDummies(AnalysisData_01, 
                                          DependentVar = Dependent_Var,
						                  IndependentVar = Independent_Vars,
						                  DummyForCol = DummyForColumn,
                                          drop_first = False)

X_Train_sld_01, y_Train_sld_01,\
X_Test_sld_01, y_Test_sld_01,\
scaler_X_01, scaler_y_01 = \
            PrepareDataForRegression(X_01, y_01, 
							         TestSplitInd = TestSetDate_01,
							         ValSplitInd = None,     
							         ScalerType = 'MinMax',
							         ScalerRange = (0,1),                             
                                     BatchSize = None,
                                     WindowLength = 1)
            
            
y_Test_01 = AnalysisData.loc[y_Test_sld_01.index][['Demand']]


#%% '02' model on winter time
###################

AnalysisData_02 = AnalysisData.loc[:'2020-02']

TestSetDate_02 = '2019-09'


X_02, y_02 =  DevideOnXandY_CreateDummies(AnalysisData_02, 
                                          DependentVar = Dependent_Var,
						                  IndependentVar = Independent_Vars,
						                  DummyForCol = DummyForColumn,
                                          drop_first = False)

X_Train_sld_02, y_Train_sld_02,\
X_Test_sld_02, y_Test_sld_02,\
scaler_X_02, scaler_y_02 = \
            PrepareDataForRegression(X_02, y_02, 
							         TestSplitInd = TestSetDate_02,
							         ValSplitInd = None,     
							         ScalerType = 'MinMax',
							         ScalerRange = (0,1),                             
                                     BatchSize = None,
                                     WindowLength = 1)
            
            
y_Test_02 = AnalysisData.loc[y_Test_sld_02.index][['Demand']]

#######
###################################################
##########################################################
#%% FIT MODEL - hyperparameter tuning
##########################################################
##########################################################

ParameterForSearch = dict(HiddenLayersNumber = [1,2,3,4,5],
                          NeuronsNumber = [25, 50, 150, 200, 250],\
                          InputShape = [(X_Train_sld_01.shape[1], )],
                          AddBatchNorm = [False, True],\
                          LossFun = ['mean_squared_error'],\
                          Opt = ['Adam()',
                                 'Nadam()',
                                 'SGD(learning_rate=0.01, decay=0.0, momentum=0.9, nesterov=False)',
                                 'SGD(learning_rate=0.1, decay=0.01, momentum=0.9, nesterov=False)',
                                 'SGD(learning_rate=0.1, decay=0.001, momentum=0.9, nesterov=False)'],\
                          ActivationFun = ['relu', 'LeakyReLU', 'ELU', 'swish'],\
                          ActivationOut = ['linear'],\
                          nb_epoch = [10,20,30,50,70,90,110],\
                          batch_size = [10,20,50,70],
                          DropoutValue = [0.2],\
                          init = ['glorot_uniform', 'uniform','normal'] )


###################
#%% '01' model on summer time
###################
# Final_Model_01.reset_states()   
 
WrapedANNmodel_01 = KerasRegressor(build_fn = CreateFeedForwardModel)
# Annmodel_GridSearch = GridSearchCV(WrapedANNmodel, ParameterForSearch, cv = 6)

ANNmodel_RandomSearch_01 = RandomizedSearchCV(WrapedANNmodel_01,\
                                              ParameterForSearch,\
                                              n_iter = 50,\
                                              cv = TimeSeriesSplit(n_splits=8).split(X_Train_sld_01),\
                                              verbose=1,\
                                              n_jobs=-1)

# Fit
ANNmodel_RandomSearch_01.fit( X_Train_sld_01, y_Train_sld_01 )

# Print the best parameters
print("Best parameters found: ", ANNmodel_RandomSearch_01.best_params_)


# Extract the best model
Final_Model_01 = ANNmodel_RandomSearch_01.best_estimator_

###################
#%% '02' model on winter time
###################

Final_Model_02 = \
    CreateFeedForwardModel(\
            HiddenLayersNumber = ANNmodel_RandomSearch_01.best_params_['HiddenLayersNumber'],\
            NeuronsNumber      = ANNmodel_RandomSearch_01.best_params_['NeuronsNumber'],\
            InputShape         = ANNmodel_RandomSearch_01.best_params_['InputShape'],\
            AddBatchNorm       = ANNmodel_RandomSearch_01.best_params_['AddBatchNorm'],\
            LossFun            = ANNmodel_RandomSearch_01.best_params_['LossFun'],\
            Opt                = ANNmodel_RandomSearch_01.best_params_['Opt'],\
            ActivationFun      = ANNmodel_RandomSearch_01.best_params_['ActivationFun'],\
            DropoutValue       = ANNmodel_RandomSearch_01.best_params_['DropoutValue'],\
            init               = ANNmodel_RandomSearch_01.best_params_['init']
                           )

# Train model on new dataset

Final_Model_02.fit(X_Train_sld_02, y_Train_sld_02,\
                   epochs = ANNmodel_RandomSearch_01.best_params_['nb_epoch'],\
                   batch_size = ANNmodel_RandomSearch_01.best_params_['batch_size'])
      
    
    
#%% or find new hyperparameter set

WrapedANNmodel_02 = KerasRegressor(build_fn = CreateFeedForwardModel)
# Annmodel_GridSearch = GridSearchCV(WrapedANNmodel, ParameterForSearch, cv = 6)

ANNmodel_RandomSearch_02 = RandomizedSearchCV(WrapedANNmodel_02,\
                                              ParameterForSearch,\
                                              n_iter = 50,\
                                              cv = TimeSeriesSplit(n_splits=8).split(X_Train_sld_02),\
                                              verbose=1,\
                                              n_jobs=-1)

# Fit
ANNmodel_RandomSearch_02.fit( X_Train_sld_02, y_Train_sld_02 )

# Print the best parameters
print("Best parameters found: ", ANNmodel_RandomSearch_02.best_params_)


# Extract the best model
Final_Model_02 = ANNmodel_RandomSearch_02.best_estimator_    
    
##########################################################
##########################################################
#%% Check Model - Test Set
##########################################################
##########################################################

###################
#%% test '01' model on summer time
###################

yhat_Test_ANN_01, X_Test_ANN_01 = \
     MakeTSforecast(X_Test_sld_01,\
                    Model = Final_Model_01,\
                    DependentVar = Dependent_Var,\
                    Intecept = False,\
                    LagsList = LagList,\
                    Scaler_y = scaler_y_01,\
                    Scaler_X = scaler_X_01,\
                    Test_or_Forecast = 'Test')

    
DataWithPrediction_01 =\
    MakeANNfinalData(Model = Final_Model_01,\
                     Train_X_Scaled = X_Train_sld_01,\
                     Val_X_Scaled = None,\
                     Scaler_y = scaler_y_01,\
                     MainDF = AnalysisData_01,\
                     yhat_Test_DF = yhat_Test_ANN_01,\
                     yhat_Forecast_DF = None)

# Plot Fitted Data        
DataWithPrediction_01[['Fitted-Train','Predicted-Test',Dependent_Var]]\
                    .loc['2018-08':].plot()
                

plt.ylabel('Demand', fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.title('Summer - test set', fontsize=20)
plt.legend(fontsize=14)
plt.grid()
plt.rcParams['figure.figsize'] = [15, 10]
plt.show()



DataWithPrediction_01[['Fitted-Train','Predicted-Test',Dependent_Var]]\
                    .loc['2019-04':].plot()

plt.ylabel('Demand', fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.title('Summer - test set', fontsize=20)
plt.legend(fontsize=14)
plt.grid()
plt.rcParams['figure.figsize'] = [15, 10]
plt.show()        


print( CalculateR2andR2adj(y_Test_01, yhat_Test_ANN_01, X_Test_sld_01, const = False) )
print('')
print( f'MAE:  {round(mean_absolute_error(y_Test_01, yhat_Test_ANN_01),2)}'  )
print( f'MAPE: {round(mean_absolute_percentage_error(y_Test_01, yhat_Test_ANN_01)*100,2)}' )
print( f'RSME: {round(np.sqrt(mean_squared_error(y_Test_01, yhat_Test_ANN_01)),2)}' )


###################
#%% test '02' model on  winter time
###################


yhat_Test_ANN_02, X_Test_ANN_02 = \
     MakeTSforecast(X_Test_sld_02,\
                    Model = Final_Model_02,\
                    DependentVar = Dependent_Var,\
                    Intecept = False,\
                    LagsList = LagList,\
                    Scaler_y = scaler_y_02,\
                    Scaler_X = scaler_X_02,\
                    Test_or_Forecast = 'Test')

    
DataWithPrediction_02 =\
    MakeANNfinalData(Model = Final_Model_02,\
                     Train_X_Scaled = X_Train_sld_02,\
                     Val_X_Scaled = None,\
                     Scaler_y = scaler_y_02,\
                     MainDF = AnalysisData_02,\
                     yhat_Test_DF = yhat_Test_ANN_02,\
                     yhat_Forecast_DF = None)


# Plot Fitted Data
DataWithPrediction_02[['Fitted-Train','Predicted-Test',Dependent_Var]]\
                                .loc['2019-03':].plot()       
        

plt.ylabel('Demand', fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.title('Winter - test set', fontsize=20)
plt.legend(fontsize=14)
plt.grid()
plt.rcParams['figure.figsize'] = [15, 10]
plt.show()




DataWithPrediction_02[['Fitted-Train','Predicted-Test',Dependent_Var]]\
                    .loc['2019-11':].plot()


plt.ylabel('Demand', fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.title('Winter - test set', fontsize=20)
plt.legend(fontsize=14)
plt.grid()
plt.rcParams['figure.figsize'] = [15, 10]
plt.show()        

print( CalculateR2andR2adj(y_Test_02, yhat_Test_ANN_02, X_Test_sld_02, const = False) )
print('')
print( f'MAE:  {round(mean_absolute_error(y_Test_02, yhat_Test_ANN_02),2)}'  )
print( f'MAPE: {round(mean_absolute_percentage_error(y_Test_02, yhat_Test_ANN_02)*100,2)}' )
print( f'RSME: {round(np.sqrt(mean_squared_error(y_Test_02, yhat_Test_ANN_02)),2)}' )