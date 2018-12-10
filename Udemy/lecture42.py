import numpy as np
import pandas as pd
from pandas import DataFrame
dframe = DataFrame({'key1': ['x','x','y','y','z'],
                    'key2': ['alpha','beta','alpha','beta','alpha'],
                    'dataset1': np.random.randn(5),
                    'dataset2': np.random.randn(5)})
group1 = dframe['dataset1'].groupby(dframe['key1'])#dataset1をkey1を元にグループ化する
group2 = dframe['dataset1'].groupby(dframe['key2'])
group1.mean()
cities = np.array(['NY','LA','LA','NY','NY'])
month = np.array(['JAN','FEB','JAN','FEB','JAN'])
print(dframe['dataset1'].groupby([cities, month]).mean())#NYのJAN、NYのFEB、LAのJAN、LAのFEBでグループ化する
print(dframe.groupby(['key1','key2']).mean())#key1とkey2でまとめる
dataset2_group = dframe.groupby(['key1','key2'])['dataset2']#key1とkey2でまとめ、dataset2だけを表示する
dataset2_group.mean()
dframe.groupby(['key1']).size()#key1でグループ化した行の数を出力する
for name, group in dframe.groupby('key1'):#nameにグループの名前、groupに内容が入る（要素が二つあるから）
    print('This is the {} group'.format(name))#大事！！！！！
    print(group)
    print("\n")
for (k1,k2), group in dframe.groupby(['key1','key2']):
    print('key1={} key2={}'.format(k1,k2))
    print(group)
    print("\n")
