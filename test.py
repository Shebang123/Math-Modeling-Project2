import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

#获取地图坐标、食物和篝火信息
def Get_Map_Information(file):
    data = pd.read_csv(file)
    data = data.values.tolist()
    length = len(data)
    number = [None] * length
    coordinate = [None] * length
    food_or_bonfire = [None] * length
    supply = [None] * length
    for i in range(length):
        number[i] = i
        coordinate[i] = data[i][1:4]
        food_or_bonfire[i] = int(data[i][4])
        supply[i] = int(data[i][5])
    return number, coordinate, food_or_bonfire, supply

# 求生者属性
class Survivor:
    state = 1 #1表示生，0表示死
    satiety = 10 #饱食度
    comfortability = 10 #舒适度
    torch = 0 #火把数量,只在篝火点可以制作

# 地图属性
class Map:
    # number表示序号，coordinate表示坐标
    # food_or_bonfire表示食物（1）或篝火（0），supply表示可提供的饱食度或舒适度
    number, coordinate, food_or_bonfire, supply = Get_Map_Information("data.csv")
    origin = coordinate[0] # 起点
    destination = coordinate[len(coordinate)-1] #终点

# 描述路线
def Draw_Roadmap():
    print()

if __name__ == "__main__":
    print(Map.destination)