import requests,json,urllib

url = 'http://127.0.0.1:5000/sql_generate'


with open('main.json') as fh:
    da = json.load(fh)

da = json.dumps(da)
x = requests.post(url, params = da)

#print(da,'\n\n')

print(x.status_code)

