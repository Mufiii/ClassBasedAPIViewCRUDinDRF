import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id = None) :
  data = {}
  if id is not None :
    data = {'id':id}
  
  json_data = json.dumps(data) # The data dictionary is serialized into a JSON-formatted string 
  headers = {'content-type':'application/json'}
  r = requests.get(url = URL, headers=headers , data=json_data)
  data = r.json()
  print(data)
  
# get_data(2)

def post_data():
  data = {
    'name': 'Muhammed yassin',
    'roll': 123,
    'city': 'malappuram'
  }
  headers = {'content-type': 'application/json'}
  json_data = json.dumps(data)
  response = requests.post( url=URL , headers=headers, data=json_data)
  data = response.json()
  print(data)
  
# post_data()


def update_data():
  data = {
    'id':1,
    'name': 'Muhammed FARHAN',
    'roll': 125,
  }
  headers = {'content-type': 'application/json'}
  json_data = json.dumps(data)
  response = requests.put( url=URL ,headers=headers, data=json_data)
  data = response.json()
  print(data)
  
update_data()

def delete_data():
  data = {'id':4}
  
  headers = {'content-type': 'application/json'}
  json_data = json.dumps(data)
  response = requests.delete( url=URL ,headers=headers, data=json_data)
  data = response.json()
  print(data)
  
# delete_data()