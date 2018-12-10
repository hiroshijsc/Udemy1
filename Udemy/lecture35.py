from pandas import DataFrame
dframe = DataFrame({'key1':['A']*2 + ['B'] * 3,
                    'key2':[2,2,2,3,3]})
dframe.duplicated()#かぶっている要素をTrue、違うのをFalseを表示
dframe.drop_duplicates()#かぶっている要素を取り出してデータフレームを作成
dframe.drop_duplicates(['key1'])#key1の要素に関して、かぶっているものを取り出しデータフレームを作成
dframe.drop_duplicates(['key1', keep = 'last'])#かぶっている要素の最後を取り出してデータフレームを作成
