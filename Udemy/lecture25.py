import pandas as pd
dframe = pd.read_csv('lec25.csv')
dframe = pd.read_csv('lec25.csv', header=None)
dframe = pd.read_table('lec25.csv', sep=',', header=None)#,で区切る（CSV形式）
pd.read_csv('lec25.csv', header=None, nrows=2)  #上から2行だけ取り出す
import sys
dframe.to_csv(sys.stdout)
dframe.to_csv(sys.stdout, sep='_')  #区切り文字を_に変更
dframe.to_csv(sys.stdout, sep = '\n')#区切り文字を改行に変更
dframe.to_csv(sys.stdout, columns = [0,1,2])
