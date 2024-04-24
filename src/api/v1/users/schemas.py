from pydantic import BaseModel

class RequestFavorSchema(BaseModel):
    user_name: str
    client: str
    latitude: float
    longitude: float
