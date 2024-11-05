from typing import Optional
from pydantic import BaseModel, Field

class Task(BaseModel):
    name: str = Field(..., max_length=100)  
    description: Optional[str] = Field(None)  

class STaskAdd(BaseModel):
    name: str = Field(..., max_length=100)
    description: Optional[str] = Field(None)  

class STask(STaskAdd):
    id: int

class STaskId(BaseModel):
    ok: bool = True
    task_id: int