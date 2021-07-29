# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 20:21:17 2021

@author: Andrew
"""

from data_generator import generator_regression
from data_loader_sorter import data_loader
from data_loader_sorter import remove_missing
from trainers import sk_regression_trainer
from trainers import sk_classification_trainer

generator_regression()
raw = data_loader('DATA.csv',3)
X,y = remove_missing(raw,10)
#X, y = standardize(data)
sk_regression_trainer(X,y)

from sklearn import datasets

iris = datasets.load_iris()

X = iris.data
y = iris.target
sk_classification_trainer(X, y)
