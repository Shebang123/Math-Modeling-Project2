import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
 
def Get_Map_Information(file):
    data = pd.read_csv(file)
    df = data['X']
    print(df)
    # data = data.values.tolist()
    # length = len(data)
    # number = [None] * length
    # coordinate = [None] * length
    # food_or_bonfire = [None] * length
    # supply = [None] * length
    
    # for i in range(length):
    #     number[i] = i
    #     coordinate[i] = data[i][1:4]
    #     food_or_bonfire[i] = int(data[i][4])
    #     supply[i] = int(data[i][5])
    
    # return number, coordinate, food_or_bonfire, supply

print(Get_Map_Information("data.csv"))