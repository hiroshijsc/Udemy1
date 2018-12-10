import numpy as np
arr = np.arange(9).reshape((3,3))
print(arr)
print(arr.T) #転置
print(arr.transpose((1,0))) #上と同様に転置を表す
arr.swapaxes(0,1) #軸を入れ替える
print(np.dot(arr.T, arr)) #行列の掛け算
arr3d = np.arange(12).reshape((3,2,2)) #2x2の行列が3個積みあがっている
print(arr3d)
print(arr3d[0])
print(arr3d.transpose((0,2,1))) #（積み上がり,行,列）
