import numpy as np
from numpy.random import randn
from scipy import stats
import seaborn as sns
data1 = randn(100)
data2 = randn(100) + 2
sns.distplot(data1)#ヒストグラムとカーネル密度推定の両方を描く
sns.distplot(data2)
sns.boxplot(data = [data1, data2])#二つの箱ひげ図を描く(外れ値は外したもの)
sns.boxplot(data = [data1, data2], whis = np.inf)#外れ値も含んだ箱ひげ図を描く(whisはひげのshisker)
sns.boxplot(data = [data1, data2], orinent = 'h')#horizonのh(平行)
data3 = stats.norm(0,5).rvs(100)#rvs=random variates(確率変数),norm(normal distribution=正規分布)
#↑平均が０、標準偏差が5の正規分布に従うサンプルをを100個生成
data4 = np.concatenate([stats.gamma(5).rvs(50)-1, -1 * stats.gamma(5).rvs(50)])
sns.boxplot(data = [data3, data4])
sns.villinplot(data = [data3, data4])#バイオリンプロットを表示
sns.violinplot(data = data4, bw = 0.01])#band widthも指定できる
sns.violinplot(data = data3, inner = 'stick')#中にrugplotを入れる
