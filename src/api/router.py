from fastapi import APIRouter
#from src.api.sipremo import analise
from src.api.v1 import teste_endpoint

#from src.api.mnt import inmet

api_router = APIRouter()

api_router.include_router(teste_endpoint.router, prefix='/teste', tags=['EndPoint de Teste'])

