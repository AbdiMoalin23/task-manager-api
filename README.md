# Task Manager API

A simple backend API for managing tasks with user authentication.

This project demonstrates core backend development skills including API design, authentication, database modeling, and CRUD operations.

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
* Create, read, update, and delete tasks
* One-to-many relationship between users and tasks

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

