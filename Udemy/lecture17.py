import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from numpy.random import randn
ser1 = Series([1,2,3,4], index =['A', 'B', 'C', 'D'])
ser2 = ser1.reindex(['A', 'B', 'C', 'D','E'])
ser1
ser2
ser2.reindex(['A', 'B', 'C', 'D','E', 'F', 'G'], fill_value = 0)
ser3 = Series(['USA', 'Mexico', 'Canada'], [0,1,20])
print(ser3.reindex(range(20), method = 'ffill'))
dframe = DataFrame(randn(25).reshape((5,5)), index = ['a', 'b','c','d','e'], columns = ['col1', 'col2', 'col3', 'col4', 'col5'])
dframe
new_index = ['a','b','c','d','e']
dframe2 = dframe.reindex(new_index)
print(dframe2)
new_columns = ['dfkjdklf','fdjh', 'col3','jf','jfldjfldkj']
dframe3 = dframe2.reindex(columns = new_columns)
print(dframe3)
