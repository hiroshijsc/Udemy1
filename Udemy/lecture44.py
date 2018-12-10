import numpy as np
import pandas as pd
from pandas import Series, DataFrame
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/'
dframe_wine = pd.read_csv("winequality-red.csv", sep = ';')#CSVからデータフレームに
dframe_wine.head()
dframe_wine['alcohol'].mean()
def max_to_min(arr):
    return arr.max() - arr.min()#最大値から最小値を引いた値を返すメソッド
wino = dframe_wine.groupby('quality')#qualityカラムでグループ化
wino.describe()#平均などを出力
#agg()は集合を出力する関数である
wino.agg(max_to_min)#値がmax-minになっているデータフレームを出力する
wino.agg('mean')#値を平均値にしたデータフレームを出力する
dframe_wine['qual/alc ratio'] = dframe_wine['quality'] / dframe_wine['alcohol']#qualityをalcoholで割った値が入るカラムを作る
dframe_wine.head()
dframe_wine.plot(kind = 'scatter', x = 'quality', y = 'alcohol')#xはx軸で散布図を書く
dframe_wine.plot(kind = 'box', x = 'quality', y = 'alcohol')#箱ひげ図を書く
dframe_wine.plot(kind = 'scatter', x = 'quality', y = 'alcohol')#xはx軸で散布図を書く
