
## Endpoints:
* Api documentation http://127.0.0.1:8000/swagger/
* To get access to the api is necessary the token: post http://127.0.0.1:8000/api/token/ and including the token in the authentication bearer and token
* Users : list of users http://127.0.0.1:8000/users/
* User: user/{id} user detail http://127.0.0.1:8000/users/id
* http methods : patch to update the title and content, post to create a user, and delete to exclude a user.


install the necessary packages


```
pip  install -r requirements.txt
```

create the database with user, database name, password, port and host in the settings.py
commands:

 to create database migration
```
python manage.py makemigrations
```

applying  the migration
```
python manage.py migrate
```
start the server
```
python manage.py runserver
```


  
