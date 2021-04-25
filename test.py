import pandas as pd

file = "data.csv"
data = pd.read_csv(file)
list = data.values.tolist()
length = len(list)
coordinate = [None] * length
food_or_bonfire = [None] * length
supply = [None] * length
for i in range(length):
    coordinate[i] = list[i][1:4]
    food_or_bonfire[i] = int(list[i][4])
    supply[i] = int(list[i][5])