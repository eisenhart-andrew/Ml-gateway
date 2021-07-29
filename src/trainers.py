# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 16:15:33 2021

@author: Andrew
"""
import numpy as np
import operator
from sklearn.neural_network import MLPRegressor
from sklearn.kernel_ridge import KernelRidge
from sklearn.svm import SVR
from sklearn.linear_model import SGDRegressor
from sklearn.gaussian_process import GaussianProcessRegressor

from sklearn.linear_model import RidgeClassifier
from sklearn.svm import SVC
from sklearn.linear_model import SGDClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.neural_network import MLPClassifier

regression_models = [KernelRidge, SVR, SGDRegressor, GaussianProcessRegressor, MLPRegressor]
classification_models = [RidgeClassifier, SVC, SGDClassifier, GaussianProcessClassifier, MLPClassifier]
results = {}

def sk_regression_trainer(X,y):
    y = np.squeeze(y)
    
    for model in regression_models:
        m = model()
        m.fit(X,y)
        result = m.score(X,y)
        results[model] = result
        print(f'Model: {model} -- Result: {result}')
    return max(results.items(), key=operator.itemgetter(1))[0]    
        
    
def sk_classification_trainer(X,y):
    y = np.squeeze(y)
    
    for model in classification_models:
        m = model()
        m.fit(X,y)
        result = m.score(X,y)
        results[model] = result
        print(f'Model: {model} -- Result: {result}')
    return max(results.items(), key=operator.itemgetter(1))[0]