# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 11:28:26 2018

@author: jd2383
"""

import glob, pandas

for filename in glob.glob('data/gapminder_gdp*.csv'):
    data = pandas.read_csv(filename)
    print(filename, data['gdpPercap_1952'].min())
