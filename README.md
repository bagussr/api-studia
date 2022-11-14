# API for studia

## Introduction

## Installation & Usage

```
# Install dependencies
$ poetry install

# Run the app
$ poetry run start

# Run the tests
$ poetry run test

# Run the migration
$ poetry run migrate
```

## Directory structure

```

api-studia
├── README.md
├── pyproject.toml
├── alembic.ini
├── __init__.py
├── .gitignore
├── alembic
├── api_studia
│   ├── models
│   ├── routes
│       ├── admin
│       ├── api
│       ├── controller
│   ├── service
│   ├── __init__.py
│   ├── app.py
│   ├── modules.py
├── public
│   ├── templates
│   ├── asset
│       ├── javascript
│       ├── css
│       ├── images
├── tests

```

## Dependencies

- Python ^3.10
  - FastAPI
  - SQLAlchemy
  - Alembic
  - Pytest
  - fastapi-jwt-auth
  - bcrypt
  - uvicorn
  - Jinja2
  - psycopg2
