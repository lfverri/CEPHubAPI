from pydantic import  BaseModel
from typing import Optional
from datetime import  datetime

class CepResponse(BaseModel):

    cep: str
    logradouro: Optional[str]
    bairro: Optional[str]
    localidade: Optional[str]
    uf: Optional[str]
    ibge: Optional[str]
    gia: Optional[str] = None
    ddd: Optional[str] = None
    siafi: Optional[str] = None
    source: str
    response_time: str

class HistoryResponse(BaseModel):
    id: int
    cep: str
    response_time: str
    source: str
    timestamp: datetime

    class Config:
        orm_mode = True