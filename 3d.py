<<<<<<< HEAD
from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

file = "D:/Shebang/data.csv"
cow_X = pd.read_csv(file, usecols = [1])
cow_Y = pd.read_csv(file, usecols = [2])
cow_Z = pd.read_csv(file, usecols = [3])
cow_X = cow_X.values.tolist()
cow_Y = cow_Y.values.tolist()
cow_Z = cow_Z.values.tolist()
num = len(cow_X)
X = Y = Z = []
for i in range(num):
    X = X + cow_X[i]
    Y = Y + cow_Y[i]
    Z = Z + cow_Z[i]
ax = plt.subplot(projection = "3d")
ax.scatter(X, Y, Z, c = 'r')
ax.set_xlabel('X')  # 设置x坐标轴
ax.set_ylabel('Y')  # 设置y坐标轴
ax.set_zlabel('Z')  # 设置z坐标轴
=======
from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

file = "D:/Shebang/data.csv"
cow_X = pd.read_csv(file, usecols = [1])
cow_Y = pd.read_csv(file, usecols = [2])
cow_Z = pd.read_csv(file, usecols = [3])
cow_X = cow_X.values.tolist()
cow_Y = cow_Y.values.tolist()
cow_Z = cow_Z.values.tolist()
num = len(cow_X)
X = Y = Z = []
for i in range(num):
    X = X + cow_X[i]
    Y = Y + cow_Y[i]
    Z = Z + cow_Z[i]
ax = plt.subplot(projection = "3d")
ax.scatter(X, Y, Z, c = 'r')
ax.set_xlabel('X')  # 设置x坐标轴
ax.set_ylabel('Y')  # 设置y坐标轴
ax.set_zlabel('Z')  # 设置z坐标轴
>>>>>>> c21321c828ecc66cf154792cd2ef82c55449e6e2
plt.show()