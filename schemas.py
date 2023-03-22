from pydantic import BaseModel

class Post(BaseModel):
    title: str
    body: str

class User(BaseModel):
    name: str
    email: str
    password: str


class ShowPost(BaseModel):
    title: str
    body: str
    class Config():
        orm_mode = True

class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    class Config():
        orm_mode = True
