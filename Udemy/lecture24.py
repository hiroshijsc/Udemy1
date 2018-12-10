import numpy as np
from pandas import Series, DataFrame
import pandas as pd
from numpy.random import randn
ser = Series(np.random.randn(6), index=[[1,1,1,2,2,2],['a','b','c','a','b','c']])
ser[2]
print(ser[:,'a'])
dframe = ser.unstack()#Seriesのindexを使ってデータフレームにする
dframe.T.unstack() #データフレームからシリーズに
dframe2 = DataFrame(np.arange(16).reshape((4,4)),
                    index = [['a','a','b','b'],[1,2,1,2]],
                    columns = [['NY','NY','LA','SF'],['cold','hot','hot','cold']])
dframe2.index.names = ['INDEX_1','INDEX_2']#行方向のindexに名前をつける
dframe2.columns.names = ['Cities','Temp']#カラムの名前をつける
dframe2.swaplevel('Cities','Temp',axis = 1)#行方向のIndexを入れ替える
dframe2.sortlevel(1)#2列目のindexをソートする（並べ替える）
dframe2.sum(level = 'Temp', axis = 1)#Tempに注目して都市名を無視して合計を計算してくれる
