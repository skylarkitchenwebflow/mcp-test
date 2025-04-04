# Task Manager API

A simple Flask-based REST API for managing tasks.

## Features

- Create, read, update, and delete tasks
- SQLite database with SQLAlchemy ORM
- RESTful API endpoints
- Environment configuration

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/skylarkitchenwebflow/mcp-test.git
   cd mcp-test
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your configurations
   ```

5. Run the application:
   ```bash
   python run.py
   ```

## API Endpoints

### Get all tasks
```
GET /tasks
```

### Create a task
```
POST /tasks
Content-Type: application/json

{
    "title": "Task title",
    "description": "Task description"
}
```

### Update a task
```
PUT /tasks/<task_id>
Content-Type: application/json

{
    "title": "Updated title",
    "description": "Updated description",
    "completed": true
}
```

### Delete a task
```
DELETE /tasks/<task_id>
```

## Testing

You can test the API using curl or any API testing tool like Postman.

Example curl command:
```bash
curl -X POST http://localhost:5000/tasks \
    -H "Content-Type: application/json" \
    -d '{"title": "My first task", "description": "This is a test task"}'
```

## License

MIT License