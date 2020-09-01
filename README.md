# events-rest-api

# Quick start

### setup environment:
```
virtualenv -p python3.7 .venv
source .venv/bin/activate
pip install -r requirements.txt
```
## Prepare db
Put your xlsx file into root directory

run
```
flask create-db
```
and
```
flask store-into-db
```
## Run app
```
flask run or python wsgi.py
```

# Usage
```
get
http://localhost:5000/ap/info

get 
http://localhost:5000/ap/timeline?startDate=2008-01-01&endDate=2020-01-01&Grouping=monthly


```
