import pandas as pd
import tools

# 求生者属性
class Survivor:
    state = 1  # 1表示生，0表示死
    satiety = 10  # 饱食度
    comfortability = 10  # 舒适度
    torch = 0  # 火把数量,只在篝火点可以制作

# 地图资源点属性
class Map:
    # number表示序号，coordinate表示坐标
    # food_or_bonfire表示食物（1）或篝火（0），supply表示可提供的饱食度或舒适度
    # 共293个食物资源点，可补给1011点饱食度；共294个篝火资源点，可补给880舒适度
    number, coordinate, food_or_bonfire, supply = tools.Get_Map_Information("data.csv")
    origin = coordinate[0]  # 起点
    destination = coordinate[len(coordinate)-1]  # 终点


if __name__ == "__main__":
    # print(Map.destination)
    # draw.Draw_Roadmap("data.csv")
    # food = 0
    # bonfire = 0
    # count_food = 0
    # count_bonfire = 0
    # for i in range(len(Map.number)):
    #     if Map.food_or_bonfire[i] == 1:
    #         food += Map.supply[i]
    #         count_food += 1
    #     else:
    #         bonfire += Map.supply[i]
    #         count_bonfire += 1
    # print("food:", count_food, food)
    # print("bonfire:", count_bonfire, bonfire)
    tools.Draw_Resource_Node("data.csv")
