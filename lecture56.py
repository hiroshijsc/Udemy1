import pandas as pd
from pandas import Series, DataFrame
titanic_df = pd.read_csv('train.csv')
titanic_df.head()
titanic_df.info()
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.countplot('Sex', data = titanic_df)#Sexのmale,femaleを数えて棒グラフを描く
sns.countplot('Sex', data = titanic_df, hue = 'Pclass')#hueでPclassごとに分けたSexを描く
sns.countplot('Pclass', data = titanic_df, hue = 'Sex')
def male_female_child(passenger):
    age, sex = passenger
    if age < 12:
        return 'child'
    else:
        return sex
titanic_df['person'] = titanic_df[['Age','Sex']].apply(male_female_child, axis = 1)#applyで12歳以下の時childを返す
print(titanic_df[0:10])
sns.countplot('Pclass', data = titanic_df, hue = 'person')
titanic_df['Age'].hist(bins = 70)#binを狭くして年齢のヒストグラムを作成
titanic_df['person'].value_counts()#personの要素ごとの数を表示する

fig = sns.FacetGrid(titanic_df, hue = 'Sex', aspect = 4)#FacetGridでグラフを一気に書くことが出来る、Sexで分ける
fig.map(sns.kdeplot, 'Age', shade = True)#Sexごとで分けたAgeのグラフを表示
oldest = titanic_df['Age'].max()
fig.set(xlim = (0, oldest))#x軸を0からAgeの最大値までにする
fig.add_legend()

fig = sns.FacetGrid(titanic_df, hue = 'person', aspect = 4)#FacetGridでグラフを一気に書くことが出来る、Sexで分ける
fig.map(sns.kdeplot, 'Age', shade = True)#personごとで分けたAgeのグラフを表示
oldest = titanic_df['Age'].max()
fig.set(xlim = (0, oldest))#x軸を0からAgeの最大値までにする
fig.add_legend()

fig = sns.FacetGrid(titanic_df, hue = 'Pclass', aspect = 4)#FacetGridでグラフを一気に書くことが出来る、Sexで分ける
fig.map(sns.kdeplot, 'Age', shade = True)#Pclassごとで分けたAgeのグラフを表示
oldest = titanic_df['Age'].max()
fig.set(xlim = (0, oldest))#x軸を0からAgeの最大値までにする
fig.add_legend()

deck = titanic_df['Cabin'].dropna()#飛行機の座席番号のnanを取り除いたものを代入
levels = []
for level in deck:
    levels.append(level[0])#からのarrayにCabinの値を格納（先頭のアルファベットだけを取り出す）
cabin_df = pd.DataFrame(levels)
cabin_df.columns = ['Cabin']
sns.countplot('Cabin', data = cabin_df, palette = 'winter_d', order = sorted(set(levels)))#set()で重複なしの要素の順番で並び替えている
cabin_df.columns = ['Cabin']
cabin_df = cabin_df[cabin_df.Cabin ! = 'T']#外れ値Tを削除する
sns.countplot('Cabin', data = cabin_df, palette = 'winter_d', order = sorted(set(levels)))
sns.countplot('Embarked', data = titanic_df, hue = 'Pclass')#港ごとで、グレードに違いがあるかを調べる
import collections import Counter
Counter(titanic_df.Embarked)#要素ごとの数を数えて、アレイで渡す
titanic_df.Embarked.value_counts()
titanic_df['Alone'] = titanic_df.Parch + titanic_df.SibSp#家族、兄弟で来ている人の合計を取り、独り身は0と表示させるようにする
titanic_df['Alone'].loc[titanic_df['Alone'] > 0] = 'With Family'#条件に応じて値を代入
titanic_df['Alone'].loc[titanic_df['Alone'] == 0] = 'Alone'
sns.countplot('Alone', data = titanic_df, palette = 'Blues')
titanic_df['Suvivor'] = titanic_df.Suvivor.map([0:'no', 1:'yes'])#map()は演算を適応してくれる
sns.countplot('Suvivor', data = titanic_df)
sns.factorplot(x = 'Pclass', y = 'Suvivor', data = titanic_df, order = [1,2,3])#種別比較図を書く,グレードごとに死亡率を比較
sns.factorplot(x = 'Pclass', y = 'Suvivor', data = titanic_df, hue = 'person', aspect = 2)#さらにpersonごとに分ける
sns.lmplot('Age', 'Suvivor', data = titanic_df)#年齢ごとの生存率を散布図と直線のグラフでざっくり確かめる
sns.lmplot('Age', 'Suvivor', hue = 'Pclass',data = titanic_df, hue_order = [1,2,3])#年齢ごとの生存率を散布図と直線のグラフでざっくり確かめる
generations = [10,20,30,40,50,60,80]
sns.lmplot('Age', 'Suvivor', hue = 'Pclass', 
            data = titanic_df, hue_order = [1,2,3], x_bins = generations)#x軸のbinを10代、20代…として幅を調べている1
generations = [10,20,30,40,50,60,80]
sns.lmplot('Age', 'Suvivor', hue = 'Sex',
            data = titanic_df, x_bins = generations)

