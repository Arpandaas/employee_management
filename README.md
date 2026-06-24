# Employee Management System

A FastAPI-based REST API application for managing employees and departments with authentication and authorization.

## Project Overview

This is a modern Python web application built with **FastAPI** that provides a comprehensive employee and department management system. The project follows best practices with:
- Layered architecture (routers, services, repositories)
- JWT-based authentication
- Database migrations using Alembic
- Comprehensive error handling
- Logging utilities

## Features

- ✅ User authentication with JWT tokens
- ✅ Employee management (CRUD operations)
- ✅ Department management
- ✅ Password hashing with bcrypt
- ✅ Role-based access control
- ✅ Database migrations with Alembic
- ✅ Custom exception handling
- ✅ Request logging

## Prerequisites

- Python 3.12+
- pip (Python package manager)
- Virtual environment support

## Installation

### 1. Clone the Repository
```bash
cd employee_management
```

### 2. Create and Activate Virtual Environment
```bash
# Create virtual environment
python3 -m venv venv1

# Activate virtual environment
# On Linux/Mac:
source venv1/bin/activate

# On Windows:
venv1\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

If `requirements.txt` doesn't exist, install the required packages:
```bash
pip install fastapi uvicorn sqlalchemy alembic bcrypt python-jose cryptography email-validator
```

### 4. Environment Configuration

Create a `.env` file in the project root:
```env
DATABASE_URL=sqlite:///./employee_management.db
# For PostgreSQL: postgresql://user:password@localhost/db_name

SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 5. Database Setup

Run Alembic migrations:
```bash
alembic upgrade head
```

## Running the Application

### Start the Development Server
```bash
uvicorn app.main:app --reload
```

The API will be available at: `http://localhost:8000`

### Access Interactive Documentation
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Project Structure

```
employee_management/
├── app/
│   ├── main.py                 # Application entry point
│   ├── config/
│   │   └── database.py         # Database configuration
│   ├── core/
│   │   └── logger.py           # Logging setup
│   ├── dependencies/
│   │   └── auth_dependency.py  # Authentication dependencies
│   ├── exceptions/
│   │   ├── custom_exception.py # Custom exceptions
│   │   └── handlers.py         # Exception handlers
│   ├── models/
│   │   ├── user_model.py       # User database model
│   │   └── department_model.py # Department database model
│   ├── repository/
│   │   ├── user_repository.py       # User data access layer
│   │   └── department_repository.py # Department data access layer
│   ├── routers/
│   │   ├── home_router.py      # Home endpoints
│   │   ├── user_router.py      # User endpoints
│   │   └── department_router.py # Department endpoints
│   ├── schemas/
│   │   ├── user_schema.py      # User request/response schemas
│   │   └── department_schema.py # Department request/response schemas
│   ├── services/
│   │   ├── user_service.py     # User business logic
│   │   └── department_service.py # Department business logic
│   ├── utils/
│   │   ├── hash_utils.py       # Password hashing utilities
│   │   └── jwt_utils.py        # JWT token utilities
│   └── static/                 # Static files
├── alembic/                    # Database migrations
├── .gitignore                  # Git ignore file
└── alembic.ini                 # Alembic configuration
```

## API Endpoints

### Authentication
- `POST /login` - User login (returns JWT token)
- `GET /users/me` - Get current user info

### Users
- `GET /users/` - List all users
- `POST /users/` - Create new user
- `GET /users/{user_id}` - Get user by ID
- `PUT /users/{user_id}` - Update user
- `DELETE /users/{user_id}` - Delete user

### Departments
- `GET /departments/` - List all departments
- `POST /departments/` - Create new department
- `GET /departments/{dept_id}` - Get department by ID
- `PUT /departments/{dept_id}` - Update department
- `DELETE /departments/{dept_id}` - Delete department

## Usage Example

### 1. Create a Department
```bash
curl -X POST http://localhost:8000/departments/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Engineering", "description": "Engineering Department"}'
```

### 2. Create a User
```bash
curl -X POST http://localhost:8000/users/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "password123",
    "department_id": 1
  }'
```

### 3. Login
```bash
curl -X POST http://localhost:8000/login \
  -H "Content-Type: application/json" \
  -d '{"username": "john_doe", "password": "password123"}'
```

## Troubleshooting

### Virtual Environment Issues
```bash
# If activate doesn't work, try:
python3 -m venv venv1
source venv1/bin/activate
```

### Database Issues
```bash
# Reset database (warning: deletes all data):
rm employee_management.db

# Recreate tables:
alembic upgrade head
```

### Port Already in Use
```bash
# Use a different port:
uvicorn app.main:app --reload --port 8001
```

## Development

### Creating New Migrations
```bash
alembic revision --autogenerate -m "Description of changes"
alembic upgrade head
```

### Running Tests
```bash
pytest
```

## Security Notes

- **Never** commit `.env` files with real secrets
- Change `SECRET_KEY` in production
- Use strong passwords for database
- Enable HTTPS in production
- Validate all user inputs
- Use environment variables for sensitive data

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, please create an issue in the repository or contact the development team.
