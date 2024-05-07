import pandas as pd

df = pd.read_csv("C:/Users/Admin/Downloads/dataset - 2020-09-24 (1).csv")

selectedNum = df.iloc[0:5]
#print(selectedNum)

import matplotlib.pyplot as plt

plt.figure(figsize= (10,5))

plt.scatter(selectedNum.Name, selectedNum.Age)
plt.title('Name and Age for each player')
plt.xlabel('Name')
plt.ylabel('Losses')
plt.grid(True)
plt.show()