# Garage_Application


This is a Django REST Framework server program that can receive HTTP requests with a JSON formatted body payload.  To install and test the program please follow the steps below.

## Building

```sh
$ mkdir Garage_Application
$ cd Garage_Application
$ python3 -m venv env
$ git clone https://github.com/jakeMulhern/Garage_Application.git
$ source venv/bin/activate
$ cd Garage_Application
$ pip install -r requirements.txt
```
Next, in the garage_application directory create a new file called config.py.
Inside of this file include set SECRET_KEY equal to the secret key that was provided to you earlier.
If you will be pushing any commits to GitHub create a .gitignore file and include config.py.

To confirm that the application was built correctly you may:
```sh
$ python manage.py runserver
```
Then visit `http://localhost:8000` to view the app.

Since this application is currently set up to utilize a JWT authentication
scheme you will see this:
![Root API View](Garage_Application/garage_inventory/static/garage_inventory/images/API_Root.png)


## Testing
To run the automated tests run:

```sh
$ python manage.py test
```
You should notice in the terminal that 30 tests pass.

-The automated tests are located in Garage_Application/garage_inventory/tests.py
-The tests are designed to test each path in the server application.  They also include seperate tests for each path to ensure that every path is protected from anonymous usage thanks to the JWT authentication scheme.


## Testing the JWT Authentication Scheme:

Using HTTPie:

run the following commands in the terminal:
```sh
$ pip install httpie
$ http post http://127.0.0.1:8000/api/token/
```
You should notice a 400 Bade Request response and should see that password and username are required.

Now run:
```sh
$ http post http://127.0.0.1:8000/api/token/ username=admin password=password123
```
and now you should notice that the "access" and "refresh" tokens are now available to you.


Using curl:
```sh
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "password123"}' \
  http://localhost:8000/api/token/
```
