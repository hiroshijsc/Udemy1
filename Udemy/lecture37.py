import numpy as np
from pandas import Series
ser1 = Series(['1,2,3,4,1,2,3,4'])
ser1.replace(1, np.nan)
ser1.replace([1,4],[100,400])
ser1.replace([4: np.nan])#4が入っているところをnullにする
