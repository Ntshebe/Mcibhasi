import pandas as pd

df = pd.read_csv("C:/Users/Admin/Downloads/dataset - 2020-09-24 (1).csv")


#print(selectedNum)

import matplotlib.pyplot as plt
num_raws= 5;
column_name = 'Appearances'
data_column= df[column_name]
data_raws = data_column.head(num_raws)

column= 'Name'
Name_column = df[column]
data = Name_column.head(num_raws)

plt.figure(figsize= (10,5))

plt.pie(data_raws, labels=data,autopct='%1.1f%%',startangle=140)
plt.title('Name and Age for each player')
plt.show()