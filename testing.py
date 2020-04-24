import requests,json

url = 'http://127.0.0.1:5000/sql_generate'


with open('main.json', encoding='utf-8') as fh:
    da = json.load(fh)

x = requests.post(url, json = da)

#print(da,'\n\n')

print('hello')
