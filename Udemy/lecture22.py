import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import pandas_datareader.data as pdweb
import datetime
arr = np.array([[1,2,np.nan],[np.nan,3,4]])
dframe1 = DataFrame(arr, index=['A','B'], columns=['One','Two','Three'])
dframe1.sum()#列の足し算
dframe1.sum(axis=1)#行の足し算
dframe1.min()
dframe1.idxmin()
dframe1.cumsum()
dframe1.describe()#分散など多くのものを返してくれる※重要

pd.core.common.is_list_like = pd.api.types.is_list_like #これを入れないとエラーが出る
end = datetime.date.today()
start = end - datetime.timedelta(days = 1000)
pd_data = pdweb.DataReader('SNE','iex',start, end)
rets = pd_data.pct_change() #その前のデータの伸び率をパーセント表示する
end = datetime.datetime(1970, 10,13)
start = datetime.datetime(2018,10,13)
nikkei225 = pdweb.DataReader("NIKKEI225", "fred", start,end)
%matplotlib inline#プロットを表示できるようにする
nikkei225.plot()#プロットする
rets.corr()#データの相関を表示
import seaborn as sns
import matplotlib.pyplot as plt
sns.heatmap(rets.corr())#相関を色で分かるように図に表す
ser1 = Series(['w','w','x','y','z','w','a','a','z'])
ser1.unique()#かぶっているのを削除する
ser1.value_counts()#個数を表示する⇒かぶっているのが一目でわかる
