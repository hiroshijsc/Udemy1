import pandas as pd
import numpy as np
from pandas import DataFrame
import pandas.util.testing as tm
tm.N = 3

def unpivot(frame):
    N,K = frame.shape
    data = {'value': frame.values.ravel('F'),
            'variable': np.asarray(frame.columns).repeat(N),
            'date': np.tile(np.asarray(frame.index),K)}
    return DataFrame(data, columns = ['date','variable','value'])

dframe = unpivot(tm.makeTimeDataFrame())
dframe_piv = dframe.pivot('date', 'variable','value')#1つ目の引数が行に、2つ目が列にくるピボットテーブルを作成
