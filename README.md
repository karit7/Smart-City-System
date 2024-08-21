# Smart City System web application

## Table of contents
- [Smart City web application](#smart-city-web-application)
  - [Table of contents](#table-of-contents)
  - [General info](#general-info)
  - [Screenshots](#screenshots)
  - [Technologies](#technologies)
  - [Setup](#setup)
  - [Code Examples](#code-examples)
  - [Features](#features)
    - [Authentication service](#authentication-service)
    - [Ledger app:](#ledger-app)
    - [To-do list:](#to-do-list)
    - [Where Machine Learning goes in?](#where-machine-learning-goes-in)
  - [API endpoints](#api-endpoints)
    - [Ledger API endpoints](#ledger-api-endpoints)
  - [Status](#status)
  - [References used to create this project](#references-used-to-create-this-project)
  - [Contact](#contact)

## General info
This project was developed using Python/Django and consists in a system to manage smart cities. It integrates the concept of Internet of Things and Machine Learning to fully automate devices and services in cities.

## Screenshots


## Technologies

* Python 3.8.6
* Django 3.1.4
* Django Cors Headers (to integrate backend and frontend)
* django-filter (for filtering the URL)
* Django Rest API 3.12.2

## Setup
This consists in a regular Django project, so first create a superuser:

```
python manage.py createsuperuser
```

For testing purposes, the database can be filled with some initial data by running

```
python manage.py shell < populate_db.py
```

To reset the database (remove all the data) use:

```
python manage.py flush
```

Finally, run the server.

```
python manage.py runserver
```

One the server is running the API endpoints can be accessed through a frontend or any other URL request.


## Code Examples
<!--Show examples of usage:
`put-your-code-here`-->
Up to now only the **ledger** app is fully functional. You can run the tests using

```
python manage.py test ledger.tests
```

To keep the same database for every test:
```
python manage.py test ledger.tests --keepdb
```

To run one specific test:
```
python manage.py test ledger.tests.TransactionTestCase
```

Tests can also be made using **jupyter notebook** and the requests library, as shown in the examples at the notebook folder.

## Features
The system currently has the following working features

General:

### Authentication service

By default API endpoints can only be accessed by authenticated users.

**Authentication on ledger**
Accounts can only be viewed by a superuser, since it contains sensitive information.

Transactions can be read-only even by guest, but it can only be created/updated/deleted by a superuser. This can be seen by accessing the endpoint through a non-superuser and trying to modify a transaction.

Users can only be viewed by a superuser.

### Ledger app:

* Create/retrieve/update/delete (CRUD) an account
* CRU(not D) a transaction
* process a transaction (so that balance is transferred from the payer to the receiver account)
* filter the transactions by status, payer (account id) or receiver (account id)


### To-do list:
* iot API endpoints
* people API endpoints

### Where Machine Learning goes in?
* Face recognition system
* Biometric recognition system
* Audio transcription
* Image transcription (not sure exactly how this will work)
* and probably more...

## API endpoints

Once the server is running (e.g port 8000), one can authenticate through:

```
http://localhost:8000/api-auth/login/
```

### Ledger API endpoints

List of accounts:

```
http://localhost:8000/api/v1/accounts/
```

Details of account id 1

```
http://localhost:8000/api/v1/accounts/1
```

List of transactions:

```
http://localhost:8000/api/v1/transactions/
```

List of processed transactions:

```
http://localhost:8000/api/v1/transactions/?status=processed
```

Details of transaction id 1

```
http://localhost:8000/api/v1/transactions/1
```

Process transaction id 1:

```
http://localhost:8000/api/v1/transactions/1/process
```

List of users:

```
http://localhost:8000/api/v1/users/
```

Details of user id 1

```
http://localhost:8000/api/v1/users/1
```

Most have CRUD functionalities (e.g transaction can not be destroyed), as shown in the **notebooks** folder


## Status
Project is: _in progress_,<!-- _finished_, _no longer continue_ and why?-->

## References used to create this project

* Django for APIs
* Django Official documentation