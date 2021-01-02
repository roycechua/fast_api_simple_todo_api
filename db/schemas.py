from pydantic import BaseModel
from typing import Optional

class TodoBase(BaseModel):
    id: int
    task: str
    isDone: Optional[bool] = False

    class Config:
        orm_mode = True

class TodoCreate(BaseModel):
    task: str
    
    class Config:
        orm_mode = True


