import numpy as np
import pandas as pd
from pandas import Series, DataFrame
arr1 = np.arange(9).reshape((3,3))
np.concatenate([arr1, arr1], axis = 1)#列方向に結合
np.concatenate([arr1, arr1], axis = 0)#行方向に結合
ser1 = Series([0,1,2], index = ['t','u','v'])
ser2 = Series([3,4], index = ['x','y'])
pd.concat([ser1,ser2])#行方向に結合
pd.concat([ser1,ser2], axis = 1)#列方向に結合
pd.concat([ser1,ser2], keys = ['cat1','cat2'])#ser1にcat1,ser2にcat2のindexが入る
pd.concat([ser1,ser2], axis = 1, keys = ['cat1','cat2'])#カラムにcat1,cat2が入る
dframe1 = DataFrame(np.random.randn(4,3), columns = ['x','y','z'])
dframe2 = DataFrame(np.random.randn(3,3), columns = ['y','q','x'])
pd.concat([dframe1, dframe2])
pd.concat([dframe1, dframe2], ignore_index = True)#indexを無視して新しくindexをつける
