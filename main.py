from fastapi import FastAPI

app = FastAPI()

users=[{"id":1,"name":"John Doe","email":"john@example.com","age":28,"city":"Hyderabad"},{"id":2,"name":"Alice Smith","email":"alice@example.com","age":25,"city":"Bangalore"},{"id":3,"name":"David Lee","email":"david@example.com","age":31,"city":"Chennai"},{"id":4,"name":"Sarah Johnson","email":"sarah@example.com","age":29,"city":"Mumbai"}]

@app.get("/")
async def read_root():
    return {"message": "Welcome to my portfoliooo!"}


@app.get("/dataa")
async def read_data():
    return users