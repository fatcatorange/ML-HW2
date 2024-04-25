import requests
import json

url = 'http://127.0.0.1:8000/generate_response/'
headers = {'Content-Type': 'application/json'}

while(1) :
    user_input = input("輸入要跟 LLM 說的話：（b 退出）")
    if(user_input == ''):
        continue
    if(user_input == 'b'):
        break
    data = {'prompt': user_input}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    print(response.json())
