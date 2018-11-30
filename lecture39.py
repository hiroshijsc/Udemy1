#ビニング（データの分類）
import pandas as pd
years = [1990,1991,1992,2008,2012,2015,1987,1969,2013,2008,1999]
decade_bins = [1960,1970,1980,1990,2000,2010,2020]
decade_cut = pd.cut(years, decade_bins)#yearsをdecade_binsで年代ごとに分ける
decade_cut
decade_cut.categories#分けられたカテゴリーを調べる
pd.value_counts(decade_cut)#カテゴリーごとの値の数を出力
two_cut_data = pd.cut(years, 2)#yearを2つに分ける
