import numpy as np
import pandas as pd
from pandas import DataFrame
dframe1 = DataFrame({'key':['x','z','y','z','x','x'], 'data_set_1': np.arange(6)})
dframe2 = DataFrame({'key':['q','y','z'], 'data_set_2':[1,2,3]})
pd.merge(dframe1,dframe2) #keyの共通部分だけのデータフレームが出力される
pd.merge(dframe1, dframe2, on='key')#keyの共通部分だけのデータフレームが出力される
pd.merge(dframe1, dframe2, on = 'key', how = 'left')#dframe1に合わせてデータフレームを作成
pd.merge(dframe1, dframe2, on = 'key' , how = 'outer')#両方に合わせたデータフレームを作成
dframe3 = DataFrame({'key': ['x','x','x','y','z','z'],
                    'data_set3': range(6)})
dframe4 = DataFrame({'key': ['y','y','x','x','z'],
                    'data_set4':range(5)})
pd.merge(dframe3, dframe4, on = 'key', how = 'outer')
df_left = DataFrame({'key1':['SF','SF','LA'],
                    'key2':['one','two','one'],
                    'left_data':[10,20,30]})
df_right = DataFrame({'key1':['SF','SF','LA','LA'],
                    'key2':['one','one','one','two'],
                    'right_data':[10,20,30]})
pd.merge(df_left, df_right, on = ['key1','key2'], how = 'outer')#両方に合わせたデータフレームを作成
pd.merge(df_left, df_right, on = 'key1') #どっちのkey1かわからなくなるので、suffixesをつけてくれる
pd.merge(df_left, df_right, on = 'key1', suffixes = ['_left','_right'])#suffixesを指定する
