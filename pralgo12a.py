# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 08:20:20 2023

@author: Gwen
"""
import pandas as pd

df = pd.read_csv('Negara.csv')

print(df.head(10))

mean = df.groupby(['Benua']).mean(numeric_only=True)
std = df.groupby(['Benua']).std(numeric_only=True)

print("Rata-rata: ")
print(mean)
print("\nStandar Deviasi")
print(std)