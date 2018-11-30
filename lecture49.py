import numpy as np
from numpy.random import randn
import pandas as pd

from scipy import stats

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
dataset = randn(25)
sns.rugplot(dataset)
plt.hist(dataset, alpha = 0.3)#ヒストグラムを透明度を持たせて作成
sns.rugplot(dataset)#rugplotで実際のデータがどこにあるのかを表示
#ここから
sns.rugplot(dataset)
x_min = dataset.min() - 2
x_max = dataset.max() + 2
x_axis = np.linspace(x_min, x_max, 100)

bandwidth = ((4*dataset.std()**5)/(3*len(dataset)))**0.2

kernel_list = []
for data_point in dataset:
    kernel = stats.norm(data_point, bandwidth).pdf(x_axis)
    kernel_list.append(kernel)
    
    kernel = kernel / kernel.max()
    kernel = kernel *0.4
    plt.plot(x_axis, kernel, color = 'gray', alpha = 0.5)
plt.ylim(0,1)
#ここまではカーネル密度関数をseabornを使わないで実装する方法
sns.kdeplot(dataset)#カーネル密度推定を書く
sns.distplot(dataset)#カーネル密度推定とヒストグラムを作成

#バンド幅（band width）⇒データ（標本）一つ一つをどれくらい左右に曲げるのかを
sns.rugplot(dataset, color = 'black')
for bw in np.arange(0.5, 2.0, 0.25):
    sns.kdeplot(dataset, bw = bw, label = bw)

kernel_options = ['biw', 'cos','epa','gau','tri','triw']#ガウス分布などその他の分布を指定できる
for kern in kernel_options:
    sns.kdeplot(dataset, kernel = kern, label = kern)#一つ一つの分布を表示
sns.kdeplot(dataset, vertical = True)#グラフを垂直にする
plt.hist(dataset, cumulative = True)#累積密度関数をヒストグラムで作成（データをどんどん積み重ねたグラフ）⇒右上がり
sns.kdeplot(dataset, cumulative = True)#累積密度関数をカーネル密度推定を作成

mean = [0,0]#x,yの平均値を0，0で指定
cov = [[1,0],
       [0,100]]#共分散行列 [[0],[0]],[[1],[1]]がx,yの分散,[[0],[1]],[[1],[0]]が共分散
dataset2 = np.random.multivariate_normal(mean,cov, 1000)#平均と共分散行列にそったランダムな値を1000個生成する
dframe = pd.DataFrame(dataset2, columns = ['X','Y'])
sns.kdeplot(dframe)#二次元正規分布のカーネル密度推定を作成
sns.kdeplot(dframe.X, dframe.Y)#上と同じ
sns.kdeplot(dframe.X, dframe.Y, shade = True)#影有り
sns.kdeplot(dframe, bw = 1)
sns.kdeplot(dframe, bw = 'silverman')
sns.jointplot('X','Y',dframe, kind = 'kde')#x軸、y軸をcolumnsのｘ、yでkde(カーネル密度推定)でジョイントプロットを作成
