from typing import List

from fastapi import Depends, FastAPI, HTTPException

from sqlalchemy.orm import Session

from db import crud, models, schemas, database
from db.database import SessionLocal, engine

todo_app_api = FastAPI()

# todo_list = [
#     {
#         "id": 1,
#         "task": "Do the dishes",
#         "isDone": False
#     }
# ]

models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@todo_app_api.get("/todos", response_model=List[schemas.TodoBase])
async def return_all_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    todos = crud.get_todos(db, skip=skip, limit=limit)
    return todos  

@todo_app_api.get("/todo/{id}", response_model=schemas.TodoBase)
async def return_specific_todo(id: int, db: Session = Depends(get_db)):
    db_todo = crud.get_todo(db, todo_id=id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

@todo_app_api.post("/todo/add")
async def add_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db=db, todo=todo)

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
async def update_todo(id: int, updated_todo: schemas.TodoBase):
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

