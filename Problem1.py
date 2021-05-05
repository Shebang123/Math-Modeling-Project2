import pandas as pd
from pandas.testing import assert_frame_equal # 比较一致性
import numpy as np
import copy
import operator
import math # H2欧式距离计算平方根
import time # 对比不同的启发式使用的时间

# 地图资源点属性
# 共293个食物资源点，可补给1011点饱食度；共294个篝火资源点，可补给880舒适度
def Get_Map(map_path):
    '''
    # number表示序号，coordinate表示坐标
    # food_or_bonfire表示食物（1）或篝火（0）
    # supply表示可提供的饱食度或舒适度
    '''
    map = pd.read_csv(map_path)
    #print(map)
    return map


# 求生者属性
class Survivor:
    def __init__(self, coordinate):
        self.coordinate = coordinate # 题目中起点为[0,500,500]
        self.satiety = 10 # 饱食度
        self.comfortability = 10 # 舒适度
        self.alive = 20 # 存活指数 = 饱食度 + 舒适度
        self.g = 0 # 历史据点数之和
        self.distance = 0 # 历史路径之和
        self.h = 0 # 启发式函数
        self.f_g = 0 # 总代价 = 启发式 + 已经过据点数
        self.f_distance = 0 # 总代价 = 启发式 + 已经过距离
        self.father_node = None # 记录该状态的上一状态


def Close_Test(node_state, Close_List):
    for history_state in Close_List:
        if Goal_Test(node_state, history_state):
            return True

# 将坐标信息处理后，得到两点之间的平面距离、根据高度走势计算出的饱食度/舒适度降低值，以及2维平面坐标x、y
def Distance_Check(this_state, next_state):
    A = this_state.coordinate
    B = next_state.coordinate
    #print(A)
    x1 = A['X']
    y1 = A['Y']
    z1 = A['Z']
    x2 = B['X']
    y2 = B['Y']
    z2 = B['Z']
    coordinate_A = (x1, y1) # 只有2维
    coordinate_B = (x2, y2)
    distance = math.pow(((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)), 0.5)
    consume = 0
    if z1 < z2:
        consume = 0.06 * distance
    elif z1 > z2:
        consume = 0.04 * distance
    else:
        consume = 0.05 * distance
    return distance, consume, coordinate_A, coordinate_B


def Goal_Test(node_state, goal_state): # 一致时为True
    distance, consume, this_2D, goal_2D = Distance_Check(node_state, goal_state)
    if node_state.satiety - consume >= -3 and node_state.comfortability - consume >= -3:
        print('able to go to destination')
        return True
    return False

    '''
    if (node_state.coordinate == goal_state.coordinate).all():
        #print('Same')
        return True
    return False
    '''


def Actions(map, node_state, goal_state, heuristic, Open_List, Close_List): # node_state, goal_state都是Survivor类型的
    print("Actions")
    # 遍历map中的据点，并作出筛选
    for row in map.iterrows():
        #print(len(map))
        #print(len(row))
        #print(row[0])
        #print(row[1][0])
        if int(row[1]['Number']) >= len(map)-1:
            continue
        next_node_state = Survivor(row[1]['X':'Z'])
        temp_Food_or_bonfire = int(row[1]['Food_or_bonfire']) # 0-篝火，舒适度，comfortability | 1-食物，饱食度，satiety
        temp_Supply = row[1]['Supply'] # 供应量
        distance, consume, temp_2D, node_state_2D = Distance_Check(next_node_state, node_state)

        # 【约束1：减少搜索量】往回走的范围：x不得往回方向走
        if node_state_2D[0] >= temp_2D[0]: 
            #print('back too much')
            continue

        '''
        # 【约束2：不走重复点】下一个点与已经走过的点重复，上一个约束已经实现该目标，为简化先不考虑
        if Close_Test(next_node_state, Close_List):
            #print("Same with history state")
            continue
        '''

        # 【约束3：保证可存活】走到下一个点前，存活指数均降至-5以下
        #print('satiety: ', node_state.satiety - consume)
        #print('comfortability: ', node_state.comfortability - consume)
        if node_state.satiety - consume < -5 or node_state.comfortability - consume < -5:
            #print('die')
            continue
        
        # 给新Survivor结点赋值
        next_node_state.father_node = node_state # 记录该状态的上一状态

        if temp_Food_or_bonfire == 0: # Bonfire
            next_node_state.satiety = node_state.satiety - consume # 饱食度
            next_node_state.comfortability = node_state.comfortability - consume + temp_Supply # 舒适度
        elif temp_Food_or_bonfire == 1: # Food
            next_node_state.satiety = node_state.satiety - consume + temp_Supply # 饱食度
            next_node_state.comfortability = node_state.comfortability - consume # 舒适度
        next_node_state.alive = next_node_state.satiety + next_node_state.comfortability # 存活指数 = 饱食度 + 舒适度

        next_node_state.h = heuristic(next_node_state, goal_state) # 启发式函数
        next_node_state.g = node_state.g + 1 # 历史据点数之和
        next_node_state.f_g = next_node_state.h + next_node_state.g # 总代价 = 启发式 + 已经过据点数

        next_node_state.distance = node_state.distance + distance # 历史路径之和
        next_node_state.f_distance = next_node_state.h + next_node_state.distance # 总代价 = 启发式 + 已经过距离

        # 将新状态结点加入Open_List中
        print("Open_List Add")
        Open_List.append(next_node_state)
        print("length of Open_List: ", len(Open_List))
    #print('Actions:\t', Actions_store)
    #return 0


# 启发式2：当前状态与目标状态中各点相差的欧式距离之和
def H2(node_state, goal_state): 
    heuristic = 0
    distance, consume, temp_2D, node_state_2D = Distance_Check(node_state, goal_state)
    heuristic = distance
    print('H2:\t', heuristic)
    return heuristic


# 启发式3：当前状态与目标状态中各点相差的曼哈顿距离之和
def H3(node_state, goal_state): 
    heuristic = 0
    node_state_matrix = np.array(node_state.matrix)
    goal_state_matrix = np.array(goal_state.matrix)
    different_index = np.argwhere(node_state_matrix != goal_state_matrix)
    for index in different_index:
        goal_value = goal_state_matrix[index[0]][index[1]]
        current_index = [(ix,iy) for ix, row in enumerate(node_state_matrix) for iy, i in enumerate(row) if i == goal_value] # 输出格式：[(a,b)]，因此使用时需要两层索引
        heuristic += abs(index[0] - current_index[0][0])
        heuristic += abs(index[1] - current_index[0][1])
        #print(index)
        #print(current_index[0])
    #print('H3:\t', heuristic)
    return heuristic


#对节点列表按照估价函数的值的规则排序
def list_sort(Open_List, factor):
    '''
    self.g = 0 # 历史据点数之和
    self.distance = 0 # 历史路径之和
    self.h = 0 # 启发式函数
    self.f_g = 0 # 总代价 = 启发式 + 已经过据点数
    self.f_distance = 0 # 总代价 = 启发式 + 已经过距离
    '''
    cmp=operator.attrgetter(factor) #按照factor的值进行排序(factor:Survivor的属性，如g/distance)
    Open_List.sort(key=cmp)


# A*搜索算法
def A_Star_Search(map, initial_state, goal_state, heuristic):  # initial_state, goal_state都是Survivor类型的
    # 若有解
    Open_List = [initial_state]
    Close_List = []
    while(Open_List):
        #print("A_Star_Search While Open_List")
        current_state = Open_List[0]
        #print(current_state.coordinate)
        #print(goal_state.coordinate)

        if Goal_Test(current_state, goal_state): # 一致时为True
            #print('Goal_Test')
            return current_state

        Close_List.append(current_state)
        #print("Open_List Remove")
        Open_List.remove(current_state)
        #print("length of Open_List: ", len(Open_List))
        Actions(map, current_state, goal_state, heuristic, Open_List, Close_List)
        #print('Actions end')
        list_sort(Open_List, 'comfortability') # 'f_g', 'f_distance', 'alive'|'satiety'|'comfortability'
        #print(Open_List[0].f_g)
    return 0


# 获取路径
def Get_Result(final_state):
    global count, steps
    count = 0
    steps = ['总步数'] # 预先为第0项赋值，迭代过程中‘共x步’的字符只更新第0项
    if final_state == 0:
        return "无解"
    if final_state == None:
        return
    #print(final_state.coordinate)
    Get_Result(final_state.father_node)
    count += 1
    steps.append("第%d步" % (count)) # 每一步迭代输出‘第x步’，在列表最后增加一行
    steps.append(final_state.coordinate)
    steps[0] = "共%d步" % count # 每次迭代后更新第0项：‘共x步’
    return steps


# 打印路径
def Print_Result(final_state, out_txt_path):
    steps = Get_Result(final_state)
    #print(steps)
    out = open(out_txt_path, mode='w')
    for line in steps:
        #line = line.str()
        print(str(line))
        out.write(str(line)+'\n')
    out.close()


if __name__ == "__main__":
    #初始化Problem
    map_path = 'data.csv'
    out_path = 'out.txt'
    MAP = Get_Map(map_path)
    ORIGIN =  Survivor(MAP.loc[0,'X':'Z'])
    DESTINATION = Survivor(MAP.loc[MAP.shape[0]-1,'X':'Z'])
    #采用不同启发式的A*搜索算法
    #H2
    time1_start = time.time()
    result1 = A_Star_Search(MAP, ORIGIN, DESTINATION, H2)
    time1_end = time.time()
    
    Print_Result(result1, out_path)

    time1 = time1_end-time1_start
    #time1 = int(round((time1_end-time1_start) * 1000000000))
    print("H1 time(us): ", time1)

