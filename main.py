from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class Numbers(BaseModel):
    num1:int
    num2:int
@app.post("/add")
async def add_numbers(numbers:Numbers):
        return {"result":numbers.num1+numbers.num2+2}
