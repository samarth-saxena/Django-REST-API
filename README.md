## Setup
Start virtual environment:

```
python3 -m venv taskenv
source taskenv/bin/activate
```

 
Install requirements:
```
pip install -r requirements.txt
```

Start server:
```
python manage.py runserver
```
The server is started at http://127.0.0.1:8000/.

## Description
There is one model, Fish containing all the necessary attributes. All those attributes have been serialised. 

I have defined the following endpoints, to get the records and create new records.  

Using the Django REST API that I have created, all the records can be accessed in JSON format. They are ordered by date (newest first).  
Get all records at http://127.0.0.1:8000/. 

One can also send a POST request in JSON format to add a new record.  
Create record at http://127.0.0.1:8000/create
