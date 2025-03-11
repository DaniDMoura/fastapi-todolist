# Task Management API

A FastAPI-based Task Management API that allows users to create, list, and delete tasks.
Tasks are stored temporarily using Redis, with an expiration time based on the deadline.

## 🚀 Features

- ✅ Create tasks with an expiration time
- ✅ Retrieve all active tasks with remaining time
- ✅ Delete tasks by name
- ✅ Uses Redis for in-memory storage
- ✅ Fast and efficient, built with FastAPI

## 📌 Endpoints

| Method | Endpoint           | Description                     |
|--------|--------------------|---------------------------------|
| `POST` | `/Tasks/`          | Create a new task              |
| `GET`  | `/Tasks/`          | Retrieve all tasks             |
| `DELETE` | `/Tasks/{task_name}` | Delete a task by name        |

## ⚙️ Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/task-api.git
cd task-api
```

### 3️⃣ Run Redis (if not already running)
```bash
redis-server
```

### 2️⃣ Install dependencies using Poetry
```bash
poetry install
```

### 4️⃣ Start the API
```bash
poetry run fastapi dev src/main.py
```

5️⃣ Access the API documentation
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc