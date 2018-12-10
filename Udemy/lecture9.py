import numpy as np
arr = np.arange(0,11)
print (arr)
print(arr[8])
print(arr[1:5])
arr[0:5] = 100
print(arr)
arr = np.arange(0,11)
slice_arr = arr[0:6]
slice_arr[:] = 99
print(slice_arr)
print(arr) #arrayのsliceは参照なので、元のarrayも変更されてしまう
arr_copy = arr.copy()
arr_copy[:] = 50
print(arr_copy)
print(arr)
arr_2d = np.array([[5,10,15],
                   [20,25,30],
                   [35,40,45]])
print(arr_2d)
print(arr_2d[1][0])
print(arr_2d[1,0])
print(arr_2d[:2,1:])
print(arr_2d[2,:])
arr2d = np.zeros((10,10))
print(arr2d)
arr_length = arr2d.shape[1]
print(arr_length)
for i in range(arr_length):
    arr2d[i] = i
    print(arr2d[i])
print(arr2d[[2,4,6,8]])
print(arr2d[[6,4,3,8]])
