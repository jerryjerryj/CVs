import pandas as pd
import pickle
import matplotlib.pyplot as plt
import numpy



data = pd.read_csv("RetrainingCspability.csv", dtype={"retraining_capability": object},sep=";", header=0)

counts = pd.DataFrame(data['retraining_capability'].value_counts())
print(counts)
print('Неизвестно\t\t\t\t\t\t\t\t'+ str(data['retraining_capability'].isnull().sum()))
print('\t\t\t\t\t\t\t\t\t\t------')
print('Всего\t\t\t\t\t\t\t\t\t'+ str(data.__len__()))