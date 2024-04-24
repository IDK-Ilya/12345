import uvicorn
from fastapi import FastAPI

app = FastAPI(title="App test")


fake_users = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "investor", "name": "John"},
    {"id": 3, "role": "trader", "name": "Matt"},
]

@app.get("/")
def one():
    return "Какой-то бред"

@app.get("/users/{user_id}")
def get_user(user_id):
    return user_id

if __name__=="__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)