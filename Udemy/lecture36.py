from pandas import DataFrame
dframe = DataFrame({'city': ['Alma', 'Brian Head', 'Fox Park'],
                    'altitude':[3158,3000,2752]})
state_map = {'Alma':'Colorado', 'Brian Head':'Utah', 'Fox Park':'Wyoming'}
print (dframe)
dframe['state'] = dframe['city'].map(state_map)#state_mapのcityに紐づいたデータの列が出来る
print (dframe)
dframe['key1'] = [0,1,2]#key1に0，1，2を追加
