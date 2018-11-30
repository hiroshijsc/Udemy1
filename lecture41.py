import numpy as np
from pandas import DataFrame
dframe = DataFrame(np.arange(4*4).reshape((4,4)))
blender = np.array([0,3,2,1])
dframe.take(blender)#blenderに従って、行を並び替える
dframe.take(blender, axis = 1)#列を並び替える
box = np.array(['A','B','C'])
shaker = np.random.randint(0,len(box), size =10)#boxの要素の数まで（０～２）を10回ランダムに取り出す
print(shaker)
hand_grabs = box.take(shaker)#0～2までのランダムな数を使って、要素を取り出す（０だったら[0]を取り出す）
print(hand_grabs)
print(box.take(0))
