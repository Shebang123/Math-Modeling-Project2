import pandas as pd

survivor_state = 0 #生或死
survivor_satiety = 0 #饱食度
survivor_comfortability = 0 #舒适度
survivor_torch = 0 #火把数量

#判断人物生死
def Dead_or_Alive(state): #1表示生，0表示死
    if state == 1:
        print("I am alive OvO, and my state is:\n", 
        "Satiety:", survivor_satiety, "\n"
        " Confortability:", survivor_comfortability, "\n"
        " Torch:", survivor_torch)
    elif state == 0:
        print("I am dead QAQ")

#初始化人物状态
def Initialize_Survivor_State(state, satiety, comfortability, torch):
    global survivor_state, survivor_satiety, survivor_comfortability, survivor_torch
    survivor_state = state
    survivor_satiety = satiety
    survivor_comfortability = comfortability
    survivor_torch = torch
    print(survivor_state, survivor_satiety, survivor_comfortability, survivor_torch)

#获取坐标、食物和篝火信息
def Get_Map_Information(file):
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

if __name__ == "__main__":
    Initialize_Survivor_State(1, 10, 10, 0)
    Get_Map_Information("data.csv")
    Dead_or_Alive(survivor_state)