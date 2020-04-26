import requests,json
  
# defining the api-endpoint  
API_ENDPOINT = "http://localhost:5000/sql_generator"
  
# your API key here 
#API_KEY = "XXXXXXXXXXXXXXXXX"
  
 
with open('output.json', encoding='utf-8') as fx:
        data = json.load(fx)
        
# sending post request and saving response as response object 
r = requests.post(url = API_ENDPOINT, data = data) 
  
# extracting response text  
print(r.text)
