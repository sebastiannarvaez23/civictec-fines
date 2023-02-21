# CITATION CIVICTEC

## What is this project about?
This project aims to manage information related to fines, employees, and agencies of CIVICTEC. The program has interfaces for reading, editing, creating and deleting information. Additionally, it has functions to maintain privacy according to the access role of each user, as well as filters to facilitate the location of stored information generated through the use of this application.

## How is this project built?
This project is constructed using the Django framework, HTML, CSS, and JavaScript. It employs the Django (model-view-controller) architecture, which ensures optimal performance, scalability, and the ability to add more functionality. It also features a small SQLite3 database, allowing for portability and easy access to information without the need for a separate database server. The application implements class-based views, reuses and extends pre-defined objects from the framework, resulting in cleaner, more maintainable code with fewer lines of code.

## Initial configuration to start the server
Initially I left the sqlite database with some test records to test the application in a more practical way, and not have to perform additional configurations.
### Steps to raise the project
1. Create a PYTHON3 virtual environment to host the dependencies with the command `$ python -m venv venv`.
2. Install the dependencies listed in the requirements.txt with the `$ pip install -r requirements.txt` command. It should be noted that you must be on the root path of the project.
3. start the development server by running the manage.py file accompanied by the runserver statement `$ python manage.py runserver`.
4. Rectify that the server is brought up by port 8000.
5. Open a browser by accessing the path `http://localhost:8000/`

Within the environment variables (file .env), leave some test credentials that you can use, which have different permission roles to do the information access tests.

## Endpoints
To review the documentation of the endpoints, you must enter `http://localhost:8000/docs/` or visit `http://localhost:8000/redocs/` in these pages you will find the documentation and the consumption of the endpoint of citations, and with this manage to create the citations. The first referenced link shows an interface which allows you to test the api without using postman or the browser. It should be noted that the server must be running for access to these links to be effective.

## Interfaces

#### Main interface without authentication

![image](https://user-images.githubusercontent.com/88569352/213793339-0e13fed0-e3a9-4e36-981e-a047ed46564c.png)

#### Login authentication

![image](https://user-images.githubusercontent.com/88569352/213793571-dfcf1308-82ea-4a4e-afeb-e0fcc6255871.png)

#### Authenticated main interface with admin role

![image](https://user-images.githubusercontent.com/88569352/213793764-47b54d08-5be6-4b90-8144-c075a12acd6b.png)

#### Interface that allows to manage the officials

![image](https://user-images.githubusercontent.com/88569352/213793855-1fec29ef-107b-43f0-9f06-ccfeb1152a86.png)

#### Interface to create an officer

![image](https://user-images.githubusercontent.com/88569352/213794014-f394af30-e34b-4f27-8797-b4ee68bc438e.png)

#### Admin panel interface

![image](https://user-images.githubusercontent.com/88569352/213794179-1b8e26ef-ba3c-4d59-a7b5-f794be459f54.png)

#### End Point Documentation

![image](https://user-images.githubusercontent.com/88569352/213794523-befee29d-24a6-4416-8b07-41b1678be92b.png)

![image](https://user-images.githubusercontent.com/88569352/213794677-a62c619c-8c29-46c5-9701-17a8b1975957.png)
