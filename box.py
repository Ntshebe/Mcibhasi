import pandas as pd

df = pd.read_csv("C:/Users/Admin/Downloads/dataset - 2020-09-24 (1).csv")

selectedNum = df.iloc[0:67]
#print(selectedNum)

import matplotlib.pyplot as plt
import numpy as py

column_name = 'Appearances'
data_column= df[column_name]

plt.figure(figsize= (6,5))

plt.boxplot(selectedNum.data_column, vert=True, patch_artist=True, meanline=True, showmeans=True)
plt.title('Name and Age for each player')

plt.ylabel('Losses')
plt.grid(True)
plt.show()
