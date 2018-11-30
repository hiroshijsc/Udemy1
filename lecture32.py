import numpy as np
import pandas as pd
from pandas import Series, DataFrame
ser1 = Series([2,np.nan,4,np.nan,6,np.nan], index = ['q','r','s','t','u','v'])
ser2 = Series(np.arange(len(ser1), dtype = np.float64), 
                                            index = ['q','r','s','t','u','v'])
Series(np.where(pd.isnull(ser1), ser2, ser1), 
                index = ser1.index)#ser1の値がnullのところはser2,そうでないところはser1の値を入れる
ser1.combine_first(ser2)#ser1がnullのところはser2の値を代入
dframe_odds = DataFrame({'x':[1, np.nan,3,np.nan],
                         'y':[np.nan, 5, np.nan,7],
                        'z':[np.nan, 9, np.nan,11]})
dframe_even = DataFrame({'x':[2,4, np.nan,6,8],
                         'y':[np.nan,10,12,14,16]})
dframe_odds.combine_first(dframe_even)#dframe_oddsがnullのところはdframe_evenの値を
