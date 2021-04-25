import pandas as pd


file = "data.csv"
data = pd.read_csv(file)

list = data.values.tolist()
print(list)