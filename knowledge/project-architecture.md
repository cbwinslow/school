# 🏗️ Project Architecture Knowledge Base

## Overview
This knowledge file contains patterns and best practices for designing software project architectures. Reference this when creating projects or helping with architecture questions.

---

## 🎯 Architecture Principles

### SOLID Principles
- **S**ingle Responsibility: Each class/module has one job
- **O**pen/Closed: Open for extension, closed for modification
- **L**iskov Substitution: Subtypes must be substitutable for base types
- **I**nterface Segregation: Many specific interfaces > one general interface
- **D**ependency Inversion: Depend on abstractions, not concretions

### DRY (Don't Repeat Yourself)
- Extract common code into reusable functions/classes
- Use configuration over duplication
- Leverage inheritance and composition

### KISS (Keep It Simple, Stupid)
- Prefer simple solutions
- Avoid over-engineering
- Write readable code

---

## 📁 Project Structure

### Python Project Structure
```
my-project/
├── src/
│   └── mypackage/
│       ├── __init__.py
│       ├── main.py
│       ├── models/
│       │   ├── __init__.py
│       │   └── user.py
│       ├── services/
│       │   ├── __init__.py
│       │   └── user_service.py
│       ├── utils/
│       │   ├── __init__.py
│       │   └── helpers.py
│       └── config.py
├── tests/
│   ├── __init__.py
│   ├── test_models/
│   └── test_services/
├── docs/
├── pyproject.toml
├── requirements.txt
├── README.md
└── .gitignore
```

### TypeScript Project Structure
```
my-project/
├── src/
│   ├── index.ts
│   ├── models/
│   │   └── user.ts
│   ├── services/
│   │   └── user-service.ts
│   ├── utils/
│   │   └── helpers.ts
│   └── types/
│       └── index.ts
├── tests/
│   ├── models/
│   └── services/
├── dist/
├── package.json
├── tsconfig.json
├── README.md
└── .gitignore
```

---

## 🏗️ Design Patterns

### MVC (Model-View-Controller)
```
┌──────────┐     ┌────────────┐     ┌──────────┐
│   View   │────▶│ Controller │────▶│   Model  │
└──────────┘     └────────────┘     └──────────┘
      ▲                                   │
      └───────────────────────────────────┘
```

```python
# Model
class User:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

# Controller
class UserController:
    def __init__(self, model: User):
        self.model = model
    
    def get_user(self, user_id: int) -> User:
        return self.model.find(user_id)

# View (template or API response)
def render_user(user: User) -> dict:
    return {"id": user.id, "name": user.name}
```

### Repository Pattern
```python
from abc import ABC, abstractmethod

class Repository(ABC):
    @abstractmethod
    def find_by_id(self, id: int): pass
    
    @abstractmethod
    def save(self, entity): pass
    
    @abstractmethod
    def delete(self, id: int): pass

class UserRepository(Repository):
    def __init__(self, db):
        self.db = db
    
    def find_by_id(self, id: int) -> User:
        return self.db.query(User).filter_by(id=id).first()
    
    def save(self, user: User):
        self.db.session.add(user)
        self.db.session.commit()
```

### Dependency Injection
```python
# Without DI - tightly coupled
class UserService:
    def __init__(self):
        self.repository = UserRepository()  # Hard dependency

# With DI - loosely coupled
class UserService:
    def __init__(self, repository: Repository):
        self.repository = repository  # Injected dependency

# Usage
repo = UserRepository(db)
service = UserService(repo)
```

### Observer Pattern
```typescript
type Listener<T> = (data: T) => void;

class EventEmitter<T> {
  private listeners: Map<string, Listener<T>[]> = new Map();

  on(event: string, listener: Listener<T>): () => void {
    if (!this.listeners.has(event)) {
      this.listeners.set(event, []);
    }
    this.listeners.get(event)!.push(listener);
    
    return () => {
      const listeners = this.listeners.get(event)!;
      const index = listeners.indexOf(listener);
      listeners.splice(index, 1);
    };
  }

  emit(event: string, data: T): void {
    this.listeners.get(event)?.forEach(listener => listener(data));
  }
}
```

---

## 🔧 API Architecture

### RESTful API Design
```
GET    /api/users          - List users
GET    /api/users/:id      - Get user
POST   /api/users          - Create user
PUT    /api/users/:id      - Update user
DELETE /api/users/:id      - Delete user
```

### API Response Format
```json
{
  "success": true,
  "data": {
    "id": 1,
    "name": "John"
  },
  "meta": {
    "timestamp": "2026-03-19T10:00:00Z",
    "version": "1.0"
  }
}
```

### Error Response Format
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid email format",
    "details": {
      "field": "email",
      "value": "not-an-email"
    }
  }
}
```

### Middleware Pattern
```python
from functools import wraps

def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token:
            return {"error": "Unauthorized"}, 401
        # Validate token
        return f(*args, **kwargs)
    return decorated

@app.route("/api/users")
@auth_required
def get_users():
    return {"users": []}
```

---

## 📊 Database Architecture

### Connection Pooling
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "postgresql://user:pass@localhost/db",
    pool_size=10,
    max_overflow=20,
    pool_timeout=30
)

Session = sessionmaker(bind=engine)
```

### Migration Strategy
```python
# Alembic migration
"""Create users table

Revision ID: 001
"""
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(100), nullable=False),
        sa.Column("email", sa.String(255), unique=True)
    )

def downgrade():
    op.drop_table("users")
```

---

## 🚀 Deployment Architecture

### Docker Configuration
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Docker Compose
```yaml
version: "3.8"

services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:pass@db/db
    depends_on:
      - db

  db:
    image: postgres:15
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
      - POSTGRES_DB=db
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

### CI/CD Pipeline
```yaml
# GitHub Actions
name: CI/CD

on:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: "3.11"
      - run: pip install -r requirements.txt
      - run: pytest

  deploy:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: docker build -t myapp .
      - run: docker push myapp
```

---

## ⚠️ Common Pitfalls

### Tight Coupling
```python
# Bad - tightly coupled
class OrderService:
    def create_order(self, data):
        db = PostgreSQL()  # Hard dependency on specific DB
        db.insert(data)

# Good - loosely coupled
class OrderService:
    def __init__(self, repository: Repository):
        self.repository = repository
    
    def create_order(self, data):
        self.repository.save(data)
```

### God Objects
```python
# Bad - does too much
class UserManager:
    def create_user(self): pass
    def send_email(self): pass
    def generate_report(self): pass
    def process_payment(self): pass
    def log_activity(self): pass

# Good - single responsibility
class UserService:
    def create_user(self): pass

class EmailService:
    def send_email(self): pass

class ReportService:
    def generate_report(self): pass
```

### Missing Error Handling
```python
# Bad
def get_user(id):
    return db.query(User).get(id)  # What if not found?

# Good
def get_user(id) -> User:
    user = db.query(User).get(id)
    if not user:
        raise NotFoundError(f"User {id} not found")
    return user
```

---

## 📚 Quick Reference

### HTTP Status Codes
- 200: OK
- 201: Created
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found
- 500: Internal Server Error

### Database Indexes
```sql
-- Single column
CREATE INDEX idx_users_email ON users(email);

-- Composite
CREATE INDEX idx_users_name_email ON users(name, email);

-- Unique
CREATE UNIQUE INDEX idx_users_email ON users(email);
```

### Caching Strategies
- **Cache-aside**: App manages cache
- **Write-through**: Write to cache and DB
- **Write-behind**: Write to cache, async to DB
- **Read-through**: Cache fetches from DB on miss

---

**Knowledge Version**: 1.0  
**Last Updated**: March 2026