import requests
import numpy as np
from bs4 import BeautifulSoup
import pandas as pd

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
print(date)
print("9時　 気温：" + nineTemp + "°C、 気圧：" + ninePressure + "hPaです。")
print("12時　気温：" + twelveTemp + "°C、 気圧：" + twelvePressure + "hPaです。")
arr = np.array([[nineTemp, ninePressure],[twelveTemp,twelvePressure]]).reshape((2,2))
dframe = pd.DataFrame(arr, index=['9時','12時'], columns = ['気温','気圧'])
filename = "気温と気圧.csv"
dframe.to_csv(filename, index = ['9時', '12時'], encoding = "shift_jis")
