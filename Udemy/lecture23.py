import numpy as np
from pandas import Series, DataFrame
import pandas as pd
from numpy import nan
data = Series(['one', 'two','nan','four'])
data.isnull()
data.dropna()#nanのところを削除
dframe = DataFrame([[1,2,3],[nan,5,6],[7,nan,9],[nan,nan,nan]])
dframe.dropna()#nanの行を削除
dframe.dropna(how = 'all')#全てnanの行を削除
dframe.dropna(axis = 1)#nanの含まれる列を削除
dframe2 = DataFrame([[1,2,3,nan],[2,nan,5,6],[nan,7,nan,9],[1,nan,nan,nan]])
dframe2.dropna(thresh = 2)#nanでないものが2個以上ない行は削除
dframe2.fillna(1)#nanを1に置き換える
dframe2.fillna({0:0, 1:1,2:2,3:3})#nanを1列目は１、2列目は２…と代入する
dframe2.fillna(0, inplace = True)#nanを0に置き換えてそれをdframe2に代入
print(dframe2)
