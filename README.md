# Django-MongoDB-CRUD-RESTAPI

Basic create, read, update and delete for students marks and total is here with super cool User Interface. MongoDB, A NoSQL database is used to store data.
A Restful web service for accessing the students details is created and deployed into a docker container for easy management of infrastructure

## Run application in docker container
1. Install Docker Desktop [here](https://www.docker.com/get-started)
2. Go to the project root folder and run the following commands  
    - `docker-compose build`
    - `docker-compose up`
3. Go to [127.0.0.1:8000](http://127.0.0.1:8000) to view the output

## Dependencies
- Django `pip install django`  
- Djongo `pip install djongo`  
- [MongoDB](https://fastdl.mongodb.org/windows/mongodb-windows-x86_64-4.4.2-signed.msi)  
- Django Rest Framework `pip install djangorestfamework`  

## Start the MongoDB server
First we need to create the db directory where the database files will live in. In your terminal navigate to the root of your system by doing `cd..` until you reach the top directory. You can create the directory by running `mkdir /data/db`. Now open a different tab in your terminal and run `mongod` to start the Mongo server.

## Run
Go to the project directory and run `python manage.py runserver`

## Access REST API
`/students` retrieves all student details  
`/students/<id>` retrieves details of that particular student

## Screenshot
![CRUD](https://github.com/rishi772001/django-mongodb-crud/blob/main/screenshots/Capture.PNG)
---
![REST API](https://github.com/rishi772001/django-mongodb-crud/blob/main/screenshots/Capture1.PNG)


