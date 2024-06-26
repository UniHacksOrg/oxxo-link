from sqlalchemy import Column, Integer, String, Text
from .base_model import BaseModelClass

class PostModel(BaseModelClass):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    content = Column(Text, nullable=False)
    image_url = Column(String(500))
    number_of_reactions = Column(Integer, default=0)