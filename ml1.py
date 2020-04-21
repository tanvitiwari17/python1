# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.linear_model

#load the data
oecd_bli=pd.read_csv("oecd_bli_2015.csv",thousands=',')
gdp_per_capita=pd.read_csv("gdp_per_capita.csv",thousands=',',delimiter='\t',encoding="latin1",na_values="n/a")


def prepare_country_stats(oecd_bli, gdp_per_capita) :
    oecd_bli = oecd_bli[oecd_bli["INEQUALITY"]=="TOT"]
    oecd_bli = oecd_bli.pivot(index="Country", columns="Indicator", values="Value")
    gdp_per_capita.rename(columns={"2015": "GDP per capita"}, inplace=True)
    gdp_per_capita.set_index('Country', inplace=True )
    full_country_stats = pd.merge(left=oecd_bli, right=gdp_per_capita,
                                  left_index=True, right_index=True)
    full_country_stats.sort_values(by="GDP per capita", inplace=True)
    remove_indices = [0, 1, 6, 8, 33, 34, 35]
    keep_indices = list(set(range(36)) - set(remove_indices))
    return full_country_stats[["GDP per capita", 'Life satisfaction']].iloc[keep_indices]



%matplotlib inline
import matplotlib as mpl
mpl.rc('axes', labelsize=14)
mpl.rc('xtick', labelsize=12)
mpl.rc('ytick', labelsize=12)


#prepare the data
country_stats =prepare_country_stats(oecd_bli,gdp_per_capita)
X=np.c_[country_stats['GDP per capita']]
Y=np.c_[country_stats["Life Satisfaction"]]

#visualize the data
country_stats.plot(kind='scatter',x="GDP per capita",y='Life Satisfaction')
plt.show()

#select a liner model
lin_reg_model=sklearn.liner_model.LinearRegression()
plt.show()

#select a linear model
lin_reg_model=sklear.linear_model.LinearRegression()

#train the model
lin_reg_model.fit(X,y)

#make a pridection for Cyprus
X_new=[[22587]] #cyprus' GDP per capita
print(lin_reg_model.predict(X_new))
