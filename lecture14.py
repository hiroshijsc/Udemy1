import pandas as pd
obj = pd.Series([3,6,9,12]) #numpyのarrayと違う点は、indexをつけることが出来る点
obj.values #値を取り出す
obj.index #indexを取り出す
ww2_cas = pd.Series([8700000,4300000,3000000,2100000,400000], index =['USSR', 'Germany','China', 'Japan','USA'])
ww2_dict = ww2_cas.to_dict() #辞書（ハッシュ）をつくれる（紐づけ）
ww2_Series = pd.Series(ww2_dict) #ハッシュからシリーズを作ることが出来る
countries = ['USSR', 'Germany','USA','China', 'Japan', 'Arzentina']
obj2 = pd.Series(ww2_dict, index=countries)
pd.isnull(obj2)
pd.notnull(obj2)
print(ww2_Series + obj2) #シリーズを足すことも出来る
obj2.name = '第二次世界大戦の死傷者' #全体の名前をつける　※基本はローマ字で入力する
print(obj2)
obj2.index.name = 'Countries' #indexの名前をつける
print(obj2)
