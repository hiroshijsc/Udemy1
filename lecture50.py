from numpy.random import randn
import seaborn as sns
data = randn(100)
sns.distplot(data)#ヒストグラムとカーネル密度推定を表示
sns.distplot(data, rug = True, hist = False)#rugplotとhistのオプションを追加できる
sns.distplot(data, bins = 25,#binsとはデータ数のこと
            kde_kws = {'color':'indianred', 'label':'KDE PLOT'},
            hist_kws = {'color':'blue', 'label':'HISTGRAM'})#色やラベルも指定できる
from pandas import Series
ser1 = Series(data, name = 'MY_DATA')
print(ser1)
sns.distplot(ser1)#シリーズを使ってグラフを書ける
