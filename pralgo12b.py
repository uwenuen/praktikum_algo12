# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 10:10:05 2023

@author: Gwen
"""

import pandas as pd

df = pd.read_csv('Negara.csv')

print(df.head(10))

mean = df.groupby(['Benua']).mean(numeric_only=True)
std = df.groupby(['Benua']).std(numeric_only=True)

print("\nRata-rata: ")
print(mean)
print("\nStandar Deviasi")
print(std)

mean.to_csv('outputpralgo12b/NegaraMean.csv', index = False)
std.to_csv('outputpralgo12b/NegaraStandarDevisiasi.csv', index = False)

print("\nFile Anda Berhasil Dibuat!")