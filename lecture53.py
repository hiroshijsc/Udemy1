import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
flights_dframe = sns.load_dataset('flights')
flights_dframe = flights_dframe.pivot('month', 'year', 'passengers')#行を月、列を年とし、値を旅客者としたヒートマップを作成
sns.heatmap(flights_dframe)#ヒートマップを作成
sns.heatmap(flights_dframe, annot = True, fmt = 'd')#ヒートマップの中に値を入れる
sns.heatmap(flights_dframe, center = flights_dframe.loc['January',1955])#1955年の１月データを中心としたヒートマップを作成

f, (axis1, axis2) = plt.subplots(2,1)
yearly_flights = flights_dframe.sum(axis = 0)#行の値を全て足した（年ごとの）値を代入
years = pd.Series(yearly_flights.index.values)#index(yearの値)を代入,sumで足しているためyearしかない
years = pd.DataFrame(years)
flights = pd.Series(yearly_flights.values)#年ごとの旅客者数
flights = pd.DataFrame(flights)
year_dframe = pd.concat((years, flights), axis = 1)#列方向に結合させる
year_dframe.columns = ['Year','Flights']#カラムを追加
sns.barplot(x = 'Year', y = 'Flights', data = year_dframe, ax = axis1)#棒グラフ
sns.heatmap(flights_dframe, cmap = 'Blues', ax = axis2, cbar_kws = {'orientation':'horizontal'})#平行の方向のヒートマップを作成
sns.clustermap(flights_dframe)#クラスターマップを作成
sns.clustermap(flights_dframe, col_cluster = False)#カラムのクラスターを無くす（年の並びは同じ）
sns.clustermap(flights_dframe, standard_scale = 1)#月ごとの差を無くす
sns.clustermap(flights_dframe, standard_scale = 0)#年ごとの値の差を無くす
sns.clustermap(flights_dframe, z_score = 1)#年（列を固定して）z変換（標準化する）,平均が０、分散が1
#0は縦軸、１は横軸で適応する
