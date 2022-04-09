# Todo_api
This is a simple and CRUD based Web Api. This is a todo management application Api.This project is created using backend as Django ,RESTapi  with that also used SQLite database.


## Deployment

This project is deployed and tested on local machine.


### Source code :

Get the code here : [https://github.com/mrGain/Todo_api](https://github.com/mrGain/Todo_api)



  
## Run Locally

Clone the project

```bash
  $ git clone https://github.com/mrGain/Todo_api.git
```

Go to the project directory

```bash
  $ cd Todo_api
```

### Install dependencies


- First install all the requirements to run this project.You will get all the required packages from **requirements.txt** file.

  STEP - 1
```bash
  $ pip3 install -r requirements.txt
```
  - *Note : Before installing all the requirements make sure you are on the directory where requirements.txt is located .*



After installation of required dependencies you can run and tested the project with following routes.

STEP - 2

```bash
  $ python3 manage.py makemigrations
```
STEP - 3

```bash
  $ python3 manage.py migrate
```
#### Now run
STEP - 4

```bash
  $ python3 manage.py runserver
```
## Routes

- Route - 1(default route to check it's running)

  ```bash
  localhost:8000/api/
  ```
- Route - 2 ( Add todo item )

  ```bash
  localhost:8000/api/add-todo-item/
  ```
- *Note : than provide the required field*
<br> i.e, -
```json
{
     "todo_title":"Anything here",
     "todo_description":"Any description here. "
}
```
- Route - 3 ( List all todo item )

  ```bash
  localhost:8000/api/list-all-todo-item/
  ```
- Route - 4 ( Update todo item )

  ```bash
  localhost:8000/api/update-todo-item/
  ```
- *Note : Than provide the required id to update the existing todo.*
<br>
i.e, -

```json
{
    "id": 2,
    "todo_description": "things to be update"
}
```
With id you can provide any updated field.



  

  
## Documentation

- Learn more about Django RESTapi [here](https://www.django-rest-framework.org/) .
- Get official documentationth of the Django [here](https://www.djangoproject.com/) .
- To learn more about SQLite database visit [Documentation](https://www.sqlite.org/) .
