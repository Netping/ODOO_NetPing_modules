import requests
import json

url = "odooexample.com/sqlhttpapi"

headers = {'Content-Type': 'application/json'}

# data params for sql query controller
data = {
    "params": {
        "db": "target_db_name",
        "login": "dbuser",
        "password": "dbpasswd",
        "sql": "select id, name from res_company", # this is example of target sql query
    }
}

# request to httpapi controller
session = requests.Session()
r = session.post(url=url, data=json.dumps(data), headers=headers)

print(r.json())
