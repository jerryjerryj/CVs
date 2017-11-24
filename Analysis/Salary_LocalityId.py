import pandas as pd
import pickle
import matplotlib.pyplot as plt
import numpy



data = pd.read_csv("Salary_LocalityId.csv", dtype={"locality_id": object},sep=";", header=0)

#labels = list(set(data['locality_id']))
#print(labels)

data = data.drop(data[data.salary>900000].index)
data = data.drop(data[data.salary<1000].index)

#chel = data.loc[data['locality_id'] == '7400000000000' ] # челябинск
#chel = data.loc[data['locality_id'] == '5000000000000'] #мск
#chel['locality_id'] = chel['locality_id'].map({'7400000000000': 1, '6600000000000': 2})

chelSalaries =pd.DataFrame(data['salary'].value_counts())
chelSalaries['counts'] =chelSalaries.index.values
df = chelSalaries.sort_values(['counts'])

'''plt.scatter(chel['locality_id'],chel['salary'])
plt.xticks([1,2])
plt.show()'''
print(df['counts'].tolist())
print(df['salary'].tolist())
plt.scatter(df['counts'].tolist(),df['salary'].tolist())
plt.title("Зарплаты по Всем регионам")
plt.xlabel("З\п, указанная в резюме")
plt.ylabel("Кол-во резюме")
plt.show()