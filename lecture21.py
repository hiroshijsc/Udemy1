import numpy as np
import pandas as pd
from pandas import Series, DataFrame
ser1 = Series(range(3), index=['C','A','B'])
ser2 = ser1.sort_index()
print(ser2)
print(ser1.order())
from numpy.random import randn
ser3 = Series(randn(10))
print(ser3.rank())
print(ser3.sort())
