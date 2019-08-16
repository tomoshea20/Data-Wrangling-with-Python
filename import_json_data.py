# -*- coding: utf-8 -*-
"""
Data Wrangling with Python
Ch 3
Import JSON data
"""

import os
os.chdir('F:\\Dev\\data_wrangling\\data')

import json

json_data = open('data-text.json').read()
data = json.loads(json_data)

for item in data:
    print(item)
    
    
