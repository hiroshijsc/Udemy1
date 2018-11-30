import numpy as np
from numpy.random import randn
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
tips = sns.load_dataset('tips')
sns.lmplot('total_bill', 'tip', tips)#x軸にtotal_bill,y軸にtipをとったscatterPlotとregression lineを描く
sns.lmplot('total_bill', 'tip', tips,
          scatter_kws = {'marker':'o','color':'indianred'},
          line_kws = {'linewidth': 1,'color':'blue' })
sns.lmplot('total_bill', 'tip', tips, order = 6,
          scatter_kws = {'marker':'o','color':'indianred'},
          line_kws = {'linewidth': 1,'color':'blue' })#orderを指定すると回帰直線の次数、（滑らかな関数）を描ける
sns.lmplot('total_bill','tip', tips, fit_reg = False)#回帰直線をなくすことが出来る
tips['tip_pect'] = 100* (tips['tip']/tips['total_bill'])
print(tips.head())
sns.lmplot('size', 'tip_pect',tips)
sns.lmplot('size','tip_pect', tips, x_jitter = 0.2)#スキャタープロットの点の幅を広げて点の重なりをなくす
sns.lmplot('size', 'tip_pect',tips, x_estimator = np.mean)#平均をとった棒のグラフが描ける、平均の幅でグラフの外形を確認できる
sns.lmplot('total_bill', 'tip_pect', tips, hue = 'sex', markers = ['x','o'])#男と女をxとoで分けてプロットした図を描く
sns.lmplot('total_bill', 'tip_pect', tips, hue = 'day')#日ごとに色を分けてプロットする、hueで注目するカラムを決める
sns.lmplot('total_bill', 'tip_pect', tips, lowess = True, line_kws = ['color':'red'])#分布の平均を取り、曲線を描く（局所回帰）
sns.regplot('total_bill', 'tip_pect', tips)
fig, (axis1, axis2) = plt.subplots(1,2, sharey = True)#サブプロット（空っぽの図）を取得する、y軸は共有,figは図という意味、1行2列⇒横並びの図
sns.regplot('total_bill', 'tip_pect', tips, ax = axis1)#左(axis1)の図にregplotを描く
sns.violinplot(y = 'tip_pect', x = 'size', data = tips.sort_values('size'))#右（axis2）にviolinplotを
