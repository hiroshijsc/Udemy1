import numpy as np
import pandas as pd
from pandas import Series, DataFrame
dframe1 = DataFrame(np.arange(8).reshape(2,4),
                    index = pd.Index(['LA','SF'], name = 'city'),
                    columns = pd.Index(['A','B','C','D'], name = 'letter'))
print (dframe1)
dframe_st = dframe1.stack()#Seriesをつくる
dframe_st.unstack()#letterが列のデータフレームをつくる
dframe_st.unstack(0)#cityが列のデータフレームをつくる
dframe_st.unstack('city')
ser1 = Series([0,1,2], index = ['q','x','y'])
ser2 = Series([4,5,6], index = ['x','y','z'])
series = pd.concat([ser1, ser2], keys = ['Alpha','Beta'])
dframe = series.unstack()
dframe.stack(dropna = False)#null値も表示させる