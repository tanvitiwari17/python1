# -*- coding: utf-8 -*-
"""
Created on Sat May  9 13:27:56 2020

@author: tanvi
"""

import numpy as np
import pandas as pd
import matplotlib as plt
from matplotlib import pyplot
from matplotlib import pyplot as plt
import statsmodels.api as sm
data = pd.read_csv('E:\data\SimpleLinearRegression.csv')
data
help(matplotlib)
data.describe()
plt.scatter(x=data.SAT, y=data.GPA)
plt.show()
