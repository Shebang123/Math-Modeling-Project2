from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import linecache

plt.rc("font", family='YouYuan')
plt.rcParams.update({'font.size': 20})
plt.legend(loc='best')

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
def Draw_Resource():
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
        # origin = ax.scatter(origin_X, origin_Y, origin_Z, s = 300, c = 'g', marker = '>')
        # destination = ax.scatter(destination_X, destination_Y, destination_Z, s = 300, c = 'g', marker = 'H')
        # food = ax.scatter(food_X, food_Y, food_Z, c = 'r')
        # bonfire = ax.scatter(bonfire_X, bonfire_Y, bonfire_Z, c = 'b')
        # plt.plot([origin_X, destination_X], [origin_Y, destination_Y], [origin_Z, destination_Z], c = 'r')
        ax.plot_trisurf(food_X, food_Y, food_Z)
        # plt.legend((origin, destination, food, bonfire), ('起点', '终点', '食物', '篝火'))
        ax.set_xlabel('X')  # 设置x坐标轴
        ax.set_ylabel('Y')  # 设置y坐标轴
        ax.set_zlabel('Z')  # 设置z坐标轴
        plt.show()
    
    # 平面
    elif choice == '0':
        ax = plt.subplot()
        origin = ax.scatter(origin_X, origin_Y, s = 200, c = 'g', marker = '>')
        destination = ax.scatter(destination_X, destination_Y, s = 200, c = 'g', marker = 'H')
        food = ax.scatter(food_X, food_Y, c = 'r')
        bonfire = ax.scatter(bonfire_X, bonfire_Y, c = 'b')
        # plt.plot([origin_X, destination_X], [origin_Y, destination_Y], c = 'r')
        plt.legend((origin, destination, food, bonfire), ('起点', '终点', '食物', '篝火'))
        ax.set_xlabel('X')  # 设置x坐标轴
        ax.set_ylabel('Y')  # 设置y坐标轴
        ax.set_aspect(1)
        # plt.show()

# 画出求生者从起点到终点的路线图
def Draw_Route(file):
    Draw_Resource()
    count=0
    f = open(file,"r")
    for line in f.readlines():
        count = count+1

    temp = [""] * int((count - 1) / 5)
    test = [""] * int((count - 1) / 5)
    X = [""] * int((count - 1) / 5)
    Y = [""] * int((count - 1) / 5)
    Z = [""] * int((count - 1) / 5)
    j = 0
    file_utf8 = file[:-4] + "-utf8.txt"
    print(file)
    for i in range(6, count + 1, 5):
        temp[j] = linecache.getline(file_utf8, i)
        for nn in temp[j]:
            if nn == ',':
                break
            else:
                test[j] = test[j] + nn
        test[j] = int(test[j][6:])
        j += 1

    j = 0
    temp = Get_Map_Information("data.csv")[1]
    for i in test:
        X[j] = temp[i][0]
        Y[j] = temp[i][1]
        Z[j] = temp[i][2]
        j += 1
    # plt.plot(X, Y)
    # print(Z)
    # plt.plot(X, Y, Z)
    # plt.show()

Draw_Route("out-problem1.txt")