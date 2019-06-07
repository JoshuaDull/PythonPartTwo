# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 10:33:28 2018

@author: jd2383
"""

import pandas

for filename in ['data/gapminder_gdp_africa.csv']:
    data = pandas.read_csv(filename, index_col='country')
    dataMin = pandas.DataFrame(data=data.min(), columns=['MinGDP'])
    dataIndex = pandas.DataFrame(data=data.idxmin(), columns=['country'])
    results = dataIndex.join(dataMin)
    results.to_csv('africaMin.csv')
    print(results)