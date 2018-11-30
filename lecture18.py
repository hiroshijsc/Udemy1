import numpy as np
import pandas as pd
from pandas import Series, DataFrame
ser1 = Series(np.arange(3), index = ['a', 'b', 'c'])
ser1.drop('b')#bのindexの行を削除
print(ser1.drop('b'))
dframe = DataFrame(np.arange(9).reshape((3,3)), index=['SF', 'LA', 'NY'], columns = ['pop', 'size', 'year'])
print(dframe)
dframe.drop('year', axis=1) #行は０、列は1を指定する