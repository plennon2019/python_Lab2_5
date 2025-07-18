from fastapi import FastAPI, HTTPException
from schemas import User

app = FastAPI()   # create a FastAPI instance
users = []

@app.get("/api/users")
def get_users():
    return users

@app.get("/api/user/{user_id}")
def get_user(user_id: int):
    for i, u in enumerate(users):
        if u.user_id == user_id:
            return users[i]
    raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/api/users", status_code=201)
def add_user(user: User):
    users.append(user)
    return user

@app.put("/api/users/{user_id}")
def update_user(user_id: int, user: User):
    for i, u in enumerate(users):
        if u.user_id == user_id:
            users[i] = user
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/api/users/{user_id}")
def delete_user(user_id: int):
    for i, u in enumerate(users):
        if u.user_id == user_id:
            return users.pop(i)
    raise HTTPException(status_code=404, detail="User not found")

