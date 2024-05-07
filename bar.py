import pandas as pd

df = pd.read_csv("C:/Users/Admin/Downloads/dataset - 2020-09-24 (1).csv")

selectedNum = df.iloc[5:15]
#print(selectedNum)

import matplotlib.pyplot as plt

plt.figure(figsize= (15,5))

plt.bar(selectedNum.Name, selectedNum.Age, color= 'blue' ,alpha= 0.7)
plt.title('Name and Age for each player')
plt.xlabel('Name')
plt.ylabel('Losses')
plt.grid(True)
plt.show()