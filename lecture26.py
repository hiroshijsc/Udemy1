json_obj = """
{ "zoo_animal": "Lion",
  "food":["Meat","Veggies","Honey"],
  "fur":"Golden",
  "clothes":null,
  "diet":[{"zoo_animal":"Gazelle","food":"grass","fur": "Brown"}]
  }
  """
import json
data = json.loads(json_obj)
type(data)#Pythonの辞書にする
data['diet']#dietにアクセス
json.dumps(data)#jsonにもどる
json.dump(data, open('data.json','w'))#data.jsonというファイルを生成
json.load(open('data.json'))#既存のファイルから読み込む
