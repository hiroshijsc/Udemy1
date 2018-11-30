import pandas as pd
import numpy as np
from pandas import DataFrame
df_left = DataFrame({'key':['x','y','z','x','y'],
                    'data':range(5)})
df_right = DataFrame({'group_data':[10,20]}, index = ['x','y'])
pd.merge(df_left, df_right, left_on = 'key', right_index = True)#df_leftはkey,df_rightはindexでマージする
pd.merge(df_left, df_right, left_on = 'key', right_index = True, how = 'outer')
df_left_hr = DataFrame({'key1':['SF','SF','SF','LA','LA'],
                        'key2': [10,20,30,20,30],
                        'data_set':np.arange(5)})
df_right_hr = DataFrame(np.arange(10).reshape((5,2)),
                        index = [['LA','LA','SF','SF','SF'],
                                 [20,10,10,10,20]],
                        columns = ['col_1','col_2'])
print(df_right_hr)
print(df_left_hr)
pd.merge(df_left_hr, df_right_hr, left_on = ['key1','key2'], right_index = True, how = 'outer')#onとindexのマージが複数になっただけ
df_left.join(df_right)#mergeと同じだがよく使われるのはjoin
