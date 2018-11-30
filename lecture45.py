import numpy as np
import pandas as pd
from pandas import Series, DataFrame
dfraem_wine = pd.read_csv('winequality-red.csv', sep = ';')#CSVを読み込む
dfraem_wine.sort_values('alcohol', ascending = False, inplace = True)#alcoholの値が大きい順に並べ替える
def ranker(df):
    df['alc_content_rank'] = np.arange(len(df)) + 1#引数に取ったデータフレームのalc_content_rankに（１～データフレームの長さ）までの配列を入れる
    return df#alcoholの値が大きい順に並んでいるから、大きい順に1，2，3、と番号が振られる
print(dfraem_wine.head())
dframe_wine = dfraem_wine.groupby('quality').apply(ranker)#qualityでまとめ、まとめて作られたデータフレームの数を調べ上から順に１，２、と振っている⇒alcoholが大きい順にならんでいるから、アルコールの強い順に順位を振っている
print(dframe_wine.head())
num_of_qual = dframe_wine['quality'].value_counts()#そのグループに入っている数を返す
print(num_of_qual)
