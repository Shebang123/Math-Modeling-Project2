from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

plt.rc("font",family='YouYuan')

# 获取地图坐标、食物和篝火信息
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

# 获取文件中参数值
def Get_XYZ(file):  
    # coordinate = Get_Map_Information(file)[1]
    # cow_X = [X[0] for X in coordinate]
    # cow_Y = [Y[0] for Y in coordinate]
    # cow_Z = [Z[0] for Z in coordinate]
    # print(cow_X)
    cow_X = pd.read_csv(file, usecols=[1])
    cow_Y = pd.read_csv(file, usecols=[2])
    cow_Z = pd.read_csv(file, usecols=[3])
    cow_X = cow_X.values.tolist()
    cow_Y = cow_Y.values.tolist()
    cow_Z = cow_Z.values.tolist()
    return cow_X, cow_Y, cow_Z

# 画出所有资源点分布
def Draw_Resource_Node(file):
    choice = input("平面选0，空间选1:\n")
    file = "data.csv"
    cow_X, cow_Y, cow_Z = Get_XYZ(file)
    food_or_bonfire = Get_Map_Information(file)[2]
    length = len(cow_X)
    food_X = food_Y = food_Z = bonfire_X = bonfire_Y = bonfire_Z = []

    # 区分食物和篝火资源点，并标注起点和终点
    for i in range(length):
        if i == 0:
            origin_X = cow_X[i]
            origin_Y = cow_Y[i]
            origin_Z = cow_Z[i]
        elif i == length-1:
            destination_X = cow_X[i]
            destination_Y = cow_Y[i]
            destination_Z = cow_Z[i]
        elif food_or_bonfire[i] == 1:
            food_X = food_X + cow_X[i]
            food_Y = food_Y + cow_Y[i]
            food_Z = food_Z + cow_Z[i]
        elif food_or_bonfire[i] == 0:
            bonfire_X = bonfire_X + cow_X[i]
            bonfire_Y = bonfire_Y + cow_Y[i]
            bonfire_Z = bonfire_Z + cow_Z[i]

    # 空间
    if choice == '1':
        ax = plt.subplot(projection="3d")
        origin = ax.scatter(origin_X, origin_Y, origin_Z, s = 300, c = 'g', marker = '>')
        destination = ax.scatter(destination_X, destination_Y, destination_Z, s = 300, c = 'g', marker = 'p')
        food = ax.scatter(food_X, food_Y, food_Z, c = 'r')
        bonfire = ax.scatter(bonfire_X, bonfire_Y, bonfire_Z, c = 'b')
        plt.legend((origin, destination, food, bonfire), ('起点', '终点', '食物', '篝火'))
        ax.set_xlabel('X')  # 设置x坐标轴
        ax.set_ylabel('Y')  # 设置y坐标轴
        ax.set_zlabel('Z')  # 设置z坐标轴
        plt.show()
    
    # 平面
    elif choice == '0':
        ax = plt.subplot()
        # fig = plt.figure()
        # ax = fig.add_subplot(1, 1, 1)
        ax.scatter(origin_X, origin_Y, s = 300, c = 'g', marker = '>')
        ax.scatter(destination_X, destination_Y, s = 300, c = 'g', marker = 'p')
        ax.scatter(food_X, food_Y, c = 'r')
        ax.scatter(bonfire_X, bonfire_Y, c = 'b')
        ax.set_xlabel('X')  # 设置x坐标轴
        ax.set_ylabel('Y')  # 设置y坐标轴
        plt.show()

# 画出求生者从起点到终点的路线图
