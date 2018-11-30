import numpy as np
from pandas import DataFrame
dframe = DataFrame(np.arange(12).reshape((3,4)),
                    index = ['NY','LA','SF'],
                    columns = ['A','B','C','D'])
str.lower('A')#小文字化
dframe.index.map(str.lower)
dframe.index = dframe.index.map(str.lower)#indexを小文字化
dframe.index = dframe.index.map(str.upper)#大文字化
str.title('udemy is good')
dframe.rename(index = str.title, columns = str.lower)
dframe.rename(index = {'NY':'NEW YORK'},
              columns = {'A':'ALPHA'}, inplace = True)
print(dframe)
