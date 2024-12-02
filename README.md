# fastapi-clean-example

## Description


This Project showcases Repository Pattern in Hexagonal Architecture _(also known as Clean Architecture)_. Here we have two Entities - Todos and Stats, Where Todos is the main CRUD endpoint in REST with Stats tracking the numbers and statistics about the Todos CRUD endpoint in REST under OpenAPI standard.


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


