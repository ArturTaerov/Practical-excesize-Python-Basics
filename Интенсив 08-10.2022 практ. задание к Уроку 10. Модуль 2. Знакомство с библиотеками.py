import pandas as pd
data = pd.read_csv("D:/202205-divvy-tripdata.csv", index_col = 0)
data.head()
data.tail()

data.end_station_id
data.iloc(3) # не работает, выдает ошибку: ValueError: No axis named 3 for object type DataFrame

data.info()
data.describe()

import numpy as np

arr = np.zeros((1, 3))
print (arr)

arr2 = np.full(10, 5.8)
print(arr2)

arr3 = np.empty((1, 27))
arr = arr3.reshape(3, 3, 3)
print(arr.shape)

arr4 = np.zeros((1, 64))
print(arr4.shape)
for i in range(0, 8, 2):
    for j in range (0, 64, 16):
        arr4[0][i+j] += 1
        arr4[0][i+j+9] += 1
print(arr4)
arr = arr4.reshape(8,8)
print(arr)

arr5 = np.random.sample((16))
print(arr5)
arr = arr5.reshape(4,4)
print(arr)

from scipy import integrate 
import math
f1 = lambda x: math.sin(x)*x**2
print(integrate.quad(f1,-3,10))

from scipy import linalg 
print(linalg.det(arr))
print(linalg.inv(arr))
print(linalg.eig(arr))

import matplotlib.pyplot as plt
lag = 0.1
x = np.arange(0.0, 2*np.pi, lag)
y = np.sin(x)
fig = plt.figure()
plt.plot(x, y)
y2 = np.cos(x)
plt.plot(x, y, '-g', x, y2, ':m')
plt.grid()
plt.title("График sin(x) и cos(x)")
plt.xlabel("ось x")
plt.ylabel("ось y")

plt.figure(figsize = (20, 10))
plt.subplot(1,2,1)
plt.plot(x,y,"-")

plt.subplot(1,2,2)
plt.plot(x,y2,":")
