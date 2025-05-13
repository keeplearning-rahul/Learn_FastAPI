from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

import math

# FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
# It is easy to use and allows for automatic generation of OpenAPI documentation.
app = FastAPI(title="Advanced Calculator API")

# Middleware to handle CORS
# This is important for allowing requests from different origins, especially in development
# environments where the frontend and backend might be running on different ports.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development only, restrict in production
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CalculationRequest(BaseModel):
    num1: float
    num2: float
    operation: str  # "+", "-", "*", "/", "^", "%"

@app.post("/calculate")
def calculate(request: CalculationRequest):
    num1 = request.num1
    num2 = request.num2
    operation = request.operation

    result = None
    error = None

    try:
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                raise HTTPException(status_code=400, detail="Division by zero is not allowed!")
            result = num1 / num2
        elif operation == "^":
            result = math.pow(num1, num2)
        elif operation == "%":
            result = num1 % num2
        else:
            raise HTTPException(status_code=400, detail="Invalid operation! Use '+', '-', '*', '/', '^', or '%'.")
        
        return {"result": result}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))