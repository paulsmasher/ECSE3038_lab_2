from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://ecse-week3-demo.netlify.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

fake_database = []


@app.get("/todos")
async def root():
    return fake_database

@app.post("/todos")
async def create_todo(request:Request):
    todo = await request.json()
    fake_database.append(todo)
    return todo

@app.patch("/todos/{id}")
async def update_todo_by_id(id: int, todo_data: Request):
    todo_update = await todo_data.json()
    for todo in fake_database: 
        if todo['id'] == id:
            todo.update(todo_update)
            return todo_update, 200
    return None, 404

@app.delete("/todos/{id}")
async def delete_todo(id:int):
    fake_database.pop(id)
    return{"message":"Todo delete"}



    




