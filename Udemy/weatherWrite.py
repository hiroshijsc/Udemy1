import requests
import numpy as np
from bs4 import BeautifulSoup
import pandas as pd
from pandas import Series, DataFrame
url = 'http://www.jma.go.jp/jp/amedas_h/today-44132.html'
response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')
soup.prettify()
tdTags = soup.find_all("td",{"class": "block middle"})
dateTags = soup.find_all("td", {"class": "td_title"})
date = dateTags[0].string
nineTemp = tdTags[56].string
ninePressure = tdTags[62].string
twelveTemp = tdTags[77].string
twelvePressure = tdTags[83].string
arr2d = [[nineTemp, ninePressure],[twelveTemp,twelvePressure]]
dframe = pd.read_csv("気温と気圧.csv", encoding = "shift_jis", engine = 'python')
df1 = pd.DataFrame([[nineTemp,ninePressure],[twelveTemp,twelvePressure]], columns = ['気温','気圧'])
df2 = dframe.append(df1)
print(df2)
