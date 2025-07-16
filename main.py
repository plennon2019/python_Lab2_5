from fastapi import FastAPI, HTTPException
from schemas import User

app = FastAPI()   # create a FastAPI instance
users = []

@app.get("/api/users")
def get_users():
    return users

@app.post("/api/users", status_code=201)
def add_user(user: User):
    users.append(user)
    return user
