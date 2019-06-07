# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 09:11:24 2018

@author: jd2383
"""
import csv

primes = [2,3,5]

with open('output.csv','w', newline='') as outFile:
    for prime in primes:
        squared = prime ** 2
        cubed = prime ** 3
        row = [prime,squared,cubed]
        csv.writer(outFile).writerow(row)