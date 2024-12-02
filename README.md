# fastapi-clean-example

# Todo Statistics API

This project is a simple API built with **FastAPI** for managing a todo list application. It includes functionality for creating, reading, updating, and deleting todo items, along with tracking statistics such as the total number of todos, modifications, deletions, and more.

## Features:
- **Todo Management**: CRUD operations for todos (create, read, update, delete).
- **Statistics Tracking**: Tracks overall stats like the number of todos, modifications, deletions, and more.
- **Background Tasks**: Uses background tasks to increment statistics on todo creation, deletion, and modification.
- **Pagination**: Allows pagination of the todo list for efficient data retrieval.
- **Database Integration**: Uses **SQLAlchemy** for database operations with a PostgreSQL database.
- **Database Migrations**: Uses **Alembic** for managing database schema changes and migrations.

## Technologies:
- **FastAPI**: High-performance API framework for building RESTful services.
- **SQLAlchemy**: ORM for interacting with the PostgreSQL database.
- **Pydantic**: Data validation and serialization.
- **PostgreSQL**: Relational database for storing todos and statistics.
- **Alembic**: Database migration tool for managing schema changes in a versioned manner.

This project is designed to help users manage todos while also providing insights into the overall statistics of the application. It can be easily extended to include more features or integrated into a larger application.

## Clone Repository:
```bash
git clone git@github.com:RayanZaki/Todo-App-Backend.git
cd Todo-App-Backend
```
## Installation (OPTION 1) -- Docker:

- First Check the `docker-compose.yml` where you will find the environment vars:

- Generate the database intialization script:
```bash
docker-compose up preprocessor
```

- Initalize the Database:
```bash
sudo docker-compose up -d mysql
```

- launch the rest of the app:
```bash
sudo docker-compose up
```
- migrate the database:
```bash
sudo docker exec -it python-backend-container pipenv run alembic upgrade head
```

- Open `localhost:8000/docs` for API Documentation

- You will have access to a php my admin portal on [localhost:8080](http://localhost:8080)
  - Username: `myuser`
  - Password: `mypassword`
  - Credentials are provided in the docker-compose file
- Your app is hosted on `localhost:8000/`
- You can test [localhost:8000/v1/todos](http://localhost:8000/v1/todos)


