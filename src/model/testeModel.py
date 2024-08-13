from pydantic import BaseModel, Field
from enum import Enum
from typing import Literal

# Create ENUM
class Periodo(str, Enum):
    period_1 = "1_2022"
    period_2 = "2_2022"
    period_3 = "1_2023"
    period_4 = "2_2023"
    period_5 = "1_2024"


class ItemModel(BaseModel):
    nome: float = Field(..., description="Nome do Produto", json_schema_extra="Sabonete")
    preco: float = Field(..., description="Preço do Produto", json_schema_extra=15.99)
    period: Periodo = Field(..., description="Period do item", json_schema_extra="1_2022")


class ItemModelResponse(BaseModel):
    nome: float = Field(..., description="Nome do Produto", json_schema_extra="Sabonete")
    preco: float = Field(..., description="Preço do Produto", json_schema_extra=15.99)
    period: Periodo = Field(..., description="Period do item", json_schema_extra="1_2022")


