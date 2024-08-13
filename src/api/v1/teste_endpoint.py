from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from conf.settings import settings, logger
from src.model.testeModel import ItemModel, ItemModelResponse

router = APIRouter()


# Create (Criar)
@router.post("/items/", response_model=ItemModel)
async def create_item(item: ItemModel):
    """
    Aqui é a descrição da função em Markdown 
    # h1
    ## h2 

    - item: ItemModel: Modelo do item a ser criado
    """
    logger.info(f"Item: {item.dict()}")
    response = item
    return JSONResponse(content={"data": response.dict(), "variavel_settings": settings.VARIAVEL_GLOBAL}, status_code=201)

# Read (Ler)
@router.get("/items/{item_id}", response_model=ItemModel)
async def read_item(item: ItemModel, item_id:int):
    logger.warning('Teste Log Warning')
    response = item
    return JSONResponse(content={"data": response.dict(), "id":item_id }, status_code=201)


# Update (Atualizar)
@router.put("/items/{item_id}", response_model=ItemModel)
async def read_item(item: ItemModel, item_id:int):
    logger.error('Teste Log Error')
    response = item
    return JSONResponse(content={"data": response.dict(), "id":item_id }, status_code=201)


# Delete (Deletar)
@router.delete("/items/{item_id}", response_model=ItemModel)
async def read_item(item: ItemModel, item_id:int):
    logger.debug('Teste Log Debug')
    response = item
    return JSONResponse(content={"data": response.dict(), "id":item_id }, status_code=201)
