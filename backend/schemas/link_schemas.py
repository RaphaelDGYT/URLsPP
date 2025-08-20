from pydantic import BaseModel
from datetime import datetime


class LinkPost(BaseModel):
    """
    Modelo de dados para um link post.
    - title: Titulo/Nome do link.
    - url: Url do link.
    """
    title: str
    url: str


class LinkGet(BaseModel):
    """
    Modelo de dados para um link get.
    - id: ID do link.
    - title: Titulo/Nome do link.
    - url: Url do link.
    - created_at: Data de criação do link.
    - updated_at: Data de atualização do link.
    """
    id: int
    title: str
    url: str
    created_at: datetime
    updated_at: datetime
