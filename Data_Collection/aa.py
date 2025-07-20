from scikeras.wrappers import KerasRegressor

from sklearn.model_selection import RandomizedSearchCV, GridSearchCV, TimeSeriesSplit


# Define parameters set
ann_param_grid = dict(epochs = [10,20,30,50,70,90,110],
                      batch_size = [10,20,50,70],
                      model__loss = ['mean_squared_error'],
                      model__optimizer = ['adam','nadam'],
                      model__neurons_nr = [25, 50, 150, 200, 250],
                      model__hidden_layers_nr = [1,2,3,4,5],
                      model__input_shape = [(X_train_sld.shape[1], )],
                      model__output_nodes_nr = [1],                      
                      model__add_batch_norm = [False, True],
                      model__activation_fun = ['relu', 'LeakyReLU', 'swish'],
                      model__activation_out = ['linear'],
                      model__dropout = [0.1,  0.2],
                      model__init = ['glorot_uniform','normal'],
                      model__regression_type = [True])



#Final_Model_01.reset_states()

# Define wrapper
wraped_ann_model  = KerasRegressor(model = create_feed_forward_model)

# Search hyperparamers
model_ann_random_search  = RandomizedSearchCV(wraped_ann_model ,\
                                              ann_param_grid,\
                                              n_iter = 25,\
                                              cv = TimeSeriesSplit(n_splits=5).split(X_train_sld),\
                                              verbose=1,\
                                              n_jobs=1)

model_ann_random_search .fit( X_train_sld, y_train_sld )

# Print the best parameters
print("Best parameters found: ", model_ann_random_search .best_params_)



final_model_ann = \
    CreateFeedForwardModel(\
            hidden_layers_nr = model_ann_random_search.best_params_['hidden_layers_nr'],\
            neurons_nr      = model_ann_random_search.best_params_['neurons_nr'],\
            input_shape         = model_ann_random_search.best_params_['input_shape'],\
            AddBatchNorm       = model_ann_random_search.best_params_['AddBatchNorm'],\
            LossFun            = model_ann_random_search.best_params_['LossFun'],\
            Opt                = model_ann_random_search.best_params_['Opt'],\
            ActivationFun      = model_ann_random_search.best_params_['ActivationFun'],\
            DropoutValue       = model_ann_random_search.best_params_['DropoutValue'],\
            init               = model_ann_random_search.best_params_['init']
                           )
