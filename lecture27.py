import pandas as pd
url = 'https://www.fdic.gov/bank/individual/failed/banklist.html'
dframe_list = pd.io.html.read_html(url)
dframe = dframe_list[0]#dframeの0番目に格納されている
dframe.columns#カラムにもアクセスできる
