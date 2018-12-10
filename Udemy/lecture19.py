import numpy as np
import pandas as pd
from pandas import Series, DataFrame
ser1 = Series(np.arange(3), index=['A', 'B', 'C'])
ser1[['A', 'B']]
ser1[ser1>3]
ser1[ser1>3] = 10
print(ser1)
dframe = DataFrame(np.arange.(25).reshape((5,5)), index= ['a','b','c','d','e'], columns = ['1','2','3','4','5'])
dframe.ix['a'] #aの行を取り出せる
dframe.ix[1] #1番目（2番目）の行を取り出す