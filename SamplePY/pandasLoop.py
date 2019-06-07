# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 10:33:28 2018

@author: jd2383
"""

import pandas
for filename in ['data/gapminder_gdp_africa.csv', 'data/gapminder_gdp_asia.csv']:
    data = pandas.read_csv(filename, index_col='country')
    print(filename, data.min())