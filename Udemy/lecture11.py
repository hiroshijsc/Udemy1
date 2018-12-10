import numpy as np
arr = np.arange(11)
print(arr)
print(np.sqrt(arr)) #平方根
print(np.exp(arr)) #eの累乗
A = np.random.randn(10) #平均が０、分散が１の標準正規分布からランダムに値を返す
print(A)
B = np.random.randn(10)
print(np.add(A,B))
print(np.maximum(A,B))
#jupyter notebookのHelpの中のNumpyにリファレンスが入っている
