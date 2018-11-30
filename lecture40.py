import numpy as np
from pandas import DataFrame
print(np.random.seed(12345))
dframe = DataFrame(np.random.randn(1000,4))#1000行4列のデータフレームを作成
dframe.head()
dframe.tail()
dframe.describe()
col = dframe[0]#1列目をcolに代入する
np.abs(dframe) > 3#絶対値が3より大きいものをTrue表示する
col[np.abs(col) > 3]#colの中で3より大きいものを表示
dframe[(np.abs(dframe) > 3).any(1)]#絶対値が3より大きい値がある行を表示
np.sign(dframe)#値の符号を表示する
dframe[np.abs(dframe) > 3] = np.sign(dframe) * 3#絶対値が3より大きい値を外れ値として、3、－3とする
print(dframe.describe())
