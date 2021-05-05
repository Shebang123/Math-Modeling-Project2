import linecache
import tools

count=0
f = open("out-problem1.txt","r")
for line in f.readlines():
    count = count+1

temp = [""] * int((count - 1) / 5)
test = [""] * int((count - 1) / 5)
X = [""] * int((count - 1) / 5)
Y = [""] * int((count - 1) / 5)
Z = [""] * int((count - 1) / 5)
j = 0
for i in range(6, count + 1, 5):
    temp[j] = linecache.getline("out-problem1-test.txt", i)
    for nn in temp[j]:
        if nn == ',':
            break
        else:
            test[j] = test[j] + nn
    test[j] = int(test[j][6:])
    j += 1

j = 0
temp = tools.Get_Map_Information("data.csv")[1]
for i in test:
    X[j] = temp[i][0]
    Y[j] = temp[i][1]
    Z[j] = temp[i][2]
    j += 1
print(X)
