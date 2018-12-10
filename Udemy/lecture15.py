import numpy as np
import pandas as pd
from pandas import Series, DataFrame
frame = pd.read_clipboard() #Excelのような形式のファイルをコピーするだけでとってこれる
frame.columns #カラム名全てを取得
frame['Rank'] #カラムを取得
rank = frame.Rank #カラムを取得
rank
frame.ix[3] #indexで取得が出来る
print(frame.ix[3])
print(frame[['Rank', 'Team']]) #複数取得
DataFrame(frame, columns = ['Team, Rank', 'Stadium']) #新しく作ることが出来る
print(frame.head(3)) #最初の３行を表示、引数なしだと5行
print(frame.tail(3)) #最初の３行を表示、引数なしだと5行
frame['Stadium'] = "soccer stadium" #カラムに情報を代入
print(frame)
# frame['Stadium'] = np.arange(3) #Stadiumカラムに0~5までを代入
print(frame)
stadiums = Series(['soccer stadium', 'baseball stadium'], index = [4,0]) #indexを指定してシリーズを作成
print(stadiums)
frame['Stadium'] = stadiums #インデックスに応じて値が代入される
print(frame)
del frame['Stadium'] #Stadiumの列を消す
print(frame)
data = {'City':['SF', 'LA', 'NYC'], 'Population': [837000, 0, 8373897]} #辞書作成
print(data)
city_frame = DataFrame(data)
print(city_frame)
