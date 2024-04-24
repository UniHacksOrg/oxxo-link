from pydantic import BaseModel

class CreatePostSchema(BaseModel):
    title: str
    content: str
    image: bytes

class RetrievePostSchema(BaseModel):
    id: str
    title: str
    content: str
    image_url: str