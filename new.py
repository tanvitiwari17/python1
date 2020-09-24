# -*- coding: utf-8 -*-
"""
Created on Sat May  9 22:35:49 2020

@author: tanvi
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels as sm

data=pd.read_csv("E:\\data\real_estate_price_size.csv")
data
data.describe()