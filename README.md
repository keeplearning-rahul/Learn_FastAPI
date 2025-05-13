# FastAPI Calculator API

A simple REST API built with FastAPI that performs arithmetic calculations (addition, subtraction, multiplication, division, power, and modulus).

## Features

- 🧮 Basic arithmetic operations: `+`, `-`, `*`, `/`, `^` (power), `%` (modulus)
- ✅ Input validation
- 🚫 Error handling (e.g., division by zero)
- 📚 Automatic interactive documentation
- 🐳 Docker support

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/calculate` | POST | Accepts two numbers and an operation, returns result |

## Request Format
```json
{
  "num1": 10,
  "num2": 5,
  "operation": "+"
}
```
## Response Format
```json
{
    "result": 15
}
```
### Error response:
```json
{
    "detail": "Error message"
}
```
## Getting Started

### Prerequisites
- Python 3.7+
- pip

### Installation
1. Clone the repository
```bash
git clone https://github.com/yourusername/fastapi-calculator.git
cd fastapi-calculator
```
2. Install dependencies
```bash
pip install -r requirements.txt
 ```
## Running Without Docker
1. Start the server
```bash
uvicorn main:app --reload
```
2. The API will be available at:
```bash
http://localhost:8000
```
## Running With Docker
1. Build the Docker image

```bash
docker build -t fastapi-calculator .
```
2. Run the container

```bash
docker run -d -p 8000:80 --name calculator fastapi-calculator
```

## Accessing the API

### Interactive Documentation
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Example API Request
```bash
curl -X POST "http://localhost:8000/calculate" \
  -H "Content-Type: application/json" \
  -d '{"num1":10, "num2":5, "operation":"+"}'
```



