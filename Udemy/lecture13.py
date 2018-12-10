import numpy as np
arr  = np.arange(5)
print(arr)
np.save('my_array', arr) #バイナリデータとして保存
arr = np.arange(10)
print(arr)
np.load('my_array.npy') #バイナリデータを読み込む
arr1 = np.load('my_array.npy')
print(arr1)
arr2 = np.arange(10)
np.savez('ziparrays.npz', x=arr1, y=arr2) #zipにして保存
archive_array = np.load('ziparrays.npz')
print(archive_array)
print(archive_array['x']) #arr1を表示
arr = np.array([[1,2,3,4],[4,5,6,7]])
print(arr)
np.savetxt('my_test_text.txt',arr, delimiter = ',') #arrをテキストで保存　区切り文字はカンマを使用
arr = np.loadtxt('my_test_text.txt', delimiter=',')
print(arr)
