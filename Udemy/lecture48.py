from numpy.random import randn
import matplotlib.pyplot as plt
import seaborn as sns
dataset1 = randn(100)
plt.hist(dataset1)
dataset2 = randn(80)
plt.hist(dataset2, color='indianred')
plt.hist(dataset1, normed = True)#ヒストグラムの全部の面積を積分したら１になるように標準化する

plt.hist(dataset1, normed = True, alpha = 0.5, bins = 20)#二つのグラフを比較する
plt.hist(dataset1, normed = True, alpha = 0.5, bins = 20, color = 'indianred')
data1 = randn(1000)
data2 = randn(1000)
sns.jointplot(data1, data2)#同時分布（ジョイントプロット）、ヒストグラムと散布図を表示
sns.jointplot(data1, data2, kind = 'hex')#散布図を六角形で表す