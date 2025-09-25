# FastAPI Codebase

A REST API built with FastAPI, MySQL, and Alembic for coupon management system.

## Tech Stack

- **FastAPI** - Modern web framework
- **SQLAlchemy** - ORM
- **Alembic** - Database migration tool
- **MySQL** - Database
- **Pydantic** - Data validation
- **Docker** - Containerization

## Project Structure

```
fastapi_codebase/
├── app/
│   ├── api/
│   │   └── v1/
│   │       └── coupon.py
│   ├── models/
│   │   └── coupon.py
│   ├── repositories/
│   │   └── coupon_repository.py
│   ├── schemas/
│   │   └── coupon.py
│   └── services/
│       └── coupon_service.py
├── core/
│   ├── config.py
│   ├── dependence.py
│   ├── response.py
│   └── database.py
├── main.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── .env
```

## Installation & Setup

### With Docker (Recommended)

```bash
# Clone repository
git clone https://github.com/longaodai/fastapi_codebase.git
cd fastapi_codebase

# Run with Docker Compose
docker-compose up -d

# API will be available at http://localhost:8000
```

### Local Installation

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Setup environment variables
cp .env.example .env
# Edit .env with your database configuration

# Run migrations
alembic upgrade head

# Start development server
uvicorn main:app --reload
```

## Database Migration

```bash
# Create new migration
alembic revision -m "create coupons table"

# Apply migrations
alembic upgrade head

# Rollback migration
alembic downgrade -1
```

## API Documentation

After running the application, visit:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Environment Configuration

Create a `.env` file by copy from .env.example
