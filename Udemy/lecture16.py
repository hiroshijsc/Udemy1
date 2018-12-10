import numpy as np
import pandas as pd
from pandas import Series, DataFrame
my_ser = Series([1,2,3,4], index=['A', 'B', 'C', 'D'])
my_index = my_ser.index
my_index[0]
my_index[2:]
