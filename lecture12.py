import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
points = np.arange(-5,5,0.01)
dx, dy = np.meshgrid(points, points)
dx
plt.imshow(dx) #数値の変化を色で表現
z = (np.sin(dx) + np.sin(dy))
plt.imshow(z)
plt.imshow(z)
plt.colorbar()
plt.title('Plot for sin(x)+sin(y)')
A = np.array([1,2,3,4])
B = np.array([1000,2000,3000,4000])
condition = np.array([True, True, False, False])
answer = np.where(condition, A, B) #trueの場合を第二引数にとり、falseは第三引数
from numpy.random import randn
arr = randn(5,5)
np.where(arr < 0,0,arr) #0より小さければ0をそうでないときは元の値を取る
arr.sum() #足し算
arr.sum(0) #行方向の足し算なので列ごとの計算
arr.mean() #平均値
arr.std() #標準偏差
arr.var() #分散 varience
bool_arr = np.array([True, False,True])
bool_arr.any() #どれか一つがTrue
bool_arr.all() #すべてTrue
arr.sort() #小さい順に並ぶ
countries = np.array(['France', 'Japan', 'USA', 'Russia', 'Mexico', 'Japan'])
print(countries)
countries.sort() #小さい順に並べる
np.unique(countries) #複数あるやつは一つにする
print(countries)
np.in1d(['France', 'USA', 'Sweden'], countries) #countriesの中にこれらが入っているかをT or Fで返す
