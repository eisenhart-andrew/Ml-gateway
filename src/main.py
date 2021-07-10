# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 20:21:17 2021

@author: Andrew
"""

from data_generator import generator
from data_loader_sorter import data_loader
from data_loader_sorter import remove_missing
from data_loader_sorter import standardize_split

generator()
raw = data_loader('DATA.csv',3)
data = remove_missing(raw,10)
X, y = standardize_split(data)

print(X)