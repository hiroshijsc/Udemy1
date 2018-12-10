import numpy as np
import pandas as pd
from pandas import DataFrame, Series
animals = DataFrame(np.arange(16).reshape((4,4)),
                    columns = ['w','x','y','z'],
                    index = ['dog','cat','bird','mouse'])
animals.ix[1:2, ['w','y']] = np.nan#1行目のw、y列をnullにする
behavior_map = {'w':'bad','x':'good','y':'bad','z':'good'}
animals_col = animals.groupby(behavior_map, axis = 1)#列をまとめた辞書型を引数にとり、列方向のw、x、y、zをbadとgoodでグループを作る
animals_col.count()
behavior_series = Series(behavior_map)#辞書型からシリーズを作成
animals.groupby(behavior_series, axis = 1).count()#シリーズからグループを作る
keys = ['A','B','A','B']
print(animals.groupby([len, keys]).max())#関数lenとアレイを引数に取ることが出来る
