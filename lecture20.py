import numpy as np
import pandas as pd
from pandas import Series, DataFrame
ser1 = Series(['0','1','2'], index = ['a','b','c'])
ser2 = Series(['0','1','2','3'], index = ['a','b','c','d'])
print(ser1 + ser2)
dframe1 = DataFrame(np.arange(4).reshape(2,2), columns= list('AB'), index=['NYC', 'LA'])
print(dframe1)
dframe2 = DataFrame(np.arange(9).reshape((3,3)), columns=list('ABC'),index= ['NYC', 'SF', 'LA'])
print(dframe2)
print(dframe1+dframe2)
dframe3 = dframe1.add(dframe2, fill_value = 0) #DataFrame同士を足し合わせて一つのDataFrameを作る
print(dframe3)
ser3 = dframe2.ix[0]
dframe4 = dframe2 - ser3
print(dframe5)
