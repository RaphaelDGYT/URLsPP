from fastapi import APIRouter, HTTPException
from schemas.link_schemas import LinkPost, LinkGet

router = APIRouter()

links = []


@router.post("/links/")
async def create_link(link: LinkPost):
    """
    Cria um novo link.
    - link: Objeto LinkPost contendo o título e a URL do link.
    """
    for existing_link in links:
        if existing_link.title == link.title and existing_link.url == link.url:
            raise HTTPException(status_code=400, detail="Link already exists")
    links.append(link)
    return {"message": "Link created successfully"}


@router.get("/links/{link_name}")
async def read_link_with_name(link_name: str):
    """
    Lê um link pelo nome.
    - link_name: Nome do link a ser lido.
    """
    for link in links:
        if link.title == link_name:
            return link
    raise HTTPException(status_code=404, detail="Link not found")


@router.get("/links/")
async def read_all_links():
    """
    Lê todos os links.
    """
    return links
