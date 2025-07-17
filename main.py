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

@app.put("/api/users/{user_id}")
def update_user(user_id: int, user: User):
    if user_id < 0 or user_id >= len(users):
        raise HTTPException(status_code=404, detail="User not found")
    users[user_id] = user
    return user

@app.delete("/api/users/{user_id}")
def delete_user(user_id: int):
    if user_id < 0 or user_id >= len(users):
        raise HTTPException(status_code=404, detail="User not found")
    return users.pop(user_id)

