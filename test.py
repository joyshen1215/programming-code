# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os, sys
import csv
import pandas as pd

file_path = './csv/'

csv =  os.listdir(file_path)

temp = []
for i in csv:
    if i[0] != '.': 
        temp.append(i)

print(temp[1]) 
 
for i in range(121):    
    with open(file_path + (temp[i]), newline='') as csvfile:
        a = csvfile.readlines()
        b = csvfile.read()
        print(a[1])
      
    

