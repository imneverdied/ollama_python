import requests
import json

def call_llava(prompt):
  # 設定要 POST 的 URL 和資料
  url = 'http://localhost:11434/api/generate'
  data = {
      "model": "llava",
      "prompt": "用繁體中文與我對話，" + prompt
  }
  # 將資料轉換為 JSON 格式
  json_data = json.dumps(data)
  # 發送 POST 請求並取得回應
  response = requests.post(url, data=json_data)
  # 檢查回應是否成功
  if response.status_code == 200:
      # 印出回傳值
      response_json_list=response.text
      # 将JSON数据转换为字典列表
      json_list = [json.loads(line) for line in response_json_list.split('\n') if line.strip()]
      # 提取每个字典中的"response"字段内容
      responses = [item['response'] for item in json_list]
      print(''.join(responses) , end='') #印出
      print("\n")
  else:
      print('POST 請求失敗，狀態碼：', response.status_code)



call_llava("早安")
call_llava("造一個20字的詩")




