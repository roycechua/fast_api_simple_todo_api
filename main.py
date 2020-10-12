from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

todo_app_api = FastAPI()

todo_list = [
    {
        "id": 1,
        "task": "Do the dishes",
        "isDone": False
    }
]

class todo(BaseModel):
    id: int
    task: str
    isDone: Optional[bool] = False

@todo_app_api.get("/todos")
async def return_all_todos():
    return {"todo_list": todo_list}    

@todo_app_api.get("/todo/{id}")
async def return_specific_todo(id: int):
    try:
        for existing_todo in todo_list:
            if(existing_todo["id"] == id):
                return existing_todo
    except Exception as err:
            return {"message": f"{err}"}
    return {"message": "No such todo exists"} 

@todo_app_api.post("/todo/add")
async def add_todo(todo: todo):
    try:
        todo_list.append(dict(todo))
    except Exception as err:
        return {"message": f"{err}"}
    return {"message": "Todo added"} 

@todo_app_api.delete("/todo/{id}")
async def delete_todo(id: int):
    try:
        for existing_todo in todo_list:
            if(existing_todo["id"] == id):
                todo_list.remove(existing_todo)
    except Exception as err:
        return {"message": f"{err}"}
    return {"message": f"Todo #{id} Deleted"}  
 
@todo_app_api.put("/todo/{id}")
async def update_todo(id: int, updated_todo: todo):
    try:
        for existing_todo in todo_list:
            if(existing_todo["id"] == id):
                todo_list.remove(existing_todo)
                todo_list.append(dict(updated_todo))
    except Exception as err:
        return {"message": f"{err}"}
    return {"message": f"Todo #{id} Updated"} 

@todo_app_api.put("/todo/toggle/{id}")
async def toggle_todo(id: int):
    try:
        for existing_todo in todo_list:
            if(existing_todo["id"] == id):
                temp = {
                    "id":existing_todo["id"],
                    "task":existing_todo["task"],
                    "isDone":not existing_todo["isDone"]
                }
                todo_list.remove(existing_todo)
                todo_list.append(temp)
    except Exception as err:
        return {"message": f"{err}"}
    return {"message": f"Todo #{id} Toggled"} 

