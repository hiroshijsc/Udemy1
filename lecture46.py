import pandas as pd
from io import StringIO#ただの文字をファイルのように扱える
data = '''Sample Animal Intelligence
1 Dog Dumb
2 Dog Dumb
3 Cat Smart
4 Cat Smart
5 Dog Smart
6 Cat Smart'''
dframe = pd.read_table(StringIO(data), sep = '\s+')#空白で区切りってデータフレームとして取り込む
print(dframe)
dframe1 = pd.crosstab(dframe.Animal, dframe.Intelligence)
print(dframe1)
print(pd.crosstab(dframe.Animal, dframe.Intelligence, margins = True))#合計がも表示される
