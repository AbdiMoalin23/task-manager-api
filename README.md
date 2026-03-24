# Task Manager API

A RESTful API built with FastAPI for managing tasks with secure user authentication.

This project demonstrates backend skills including API design, JWT authentication, database relationships, and protected routes.

## Tech Stack

* Python
* FastAPI
* SQLAlchemy
* SQLite
* JWT Authentication
* Pydantic

## Features 

* User registration and login
* Password hashing with bcrypt
* JWT authentication
* CRUD operations for tasks
* One-to-many relationship between users and tasks

## Setup & Installation

1. Clone the repository:
    git clone https://github.com/AbdiMoalin23/task-manager-api.git
    cd task-manager-api

2. Create Virtual environment:
    python -m venv venv

    #Mac/Linux
    source venv/bin/activate

    #Windows
    venv\Scripts\activate

3. Install dependencies:
    pip install -r requirements.txt

4. Run the server:
    uvicorn app.main:app --reload

## API Usage

    Open Swagger UI: http://127.0.0.1:8000/docs

    Authentication Flow:
    1.Register a user 
    2.Login 
    3.Click Authorize in Swagger
    4.Enter:    
        username = your email
        password = your password
    5.You can now access protected endpoints like /tasks

    Auth
        POST/register -> create user
        POST/login -> get access token

    Tasks(Protected)
        GET/tasks -> get all tasks for current user
        POST/tasks -> create task
        GET/tasks/{id} -> get a single task
        PUT/tasks/{id} -> update tasks
        DELETE/tasks/{id} -> delete task



## Project Structure

```
task-manager-api
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── auth.py
│   └── routes/
│       ├── users.py
│       └── tasks.py
│
├── requirements.txt
└── README.md
```

