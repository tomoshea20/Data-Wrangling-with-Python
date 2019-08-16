# -*- coding: utf-8 -*-
"""
Data Wrangling Chapter 3 
Data Meant to Be Read by Machines

csv reader
"""
import os
os.chdir('F:\\Dev\\data_wrangling\\data')


import csv

csvfile = open('data-text.csv', 'r')
reader = csv.DictReader(csvfile)

for row in reader:
    print(row)
    
    
