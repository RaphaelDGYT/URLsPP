from fastapi import FastAPI
from api.link_routes import router as link_router

app = FastAPI()
mensagem_inicial = """Bem-vindo à aplicação FastAPI! Esta é a rota raiz.
Você pode acessar a documentação da API em /docs ou /redoc."""


@app.get("/")
async def root():
    return {"message": f"{mensagem_inicial}"}


app.include_router(link_router, prefix="/api", tags=["links"])


# @app.delete("/items/{item_name}")
# async def delete_item(item_name: str):
#     global produtos
#     produtos = [item for item in produtos if item.name != item_name]
#     return {"message": "Item deleted successfully"}

# @app.put("/items/{item_name}")
# async def update_item(item_name: str, updated_name: str, updated_price: float):
#     """
#     Atualiza um item existente com um novo nome e preço.
#     - item_name: Nome do item a ser atualizado.
#     - updated_name: Novo nome do item.
#     - updated_price: Novo preço do item.
#     """
#     for i in produtos:
#         if i.name == item_name:
#             i.name = updated_name
#             i.price = updated_price
#             return "Ok"
#     return {"message": "Item not found"}
