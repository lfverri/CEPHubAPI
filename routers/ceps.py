from fastapi import APIRouter, Depends, Header, HTTPException, status
from sqlalchemy.orm import  Session
from typing import List

from watchfiles import awatch

from app.schemas.cep_response import CepResponse, HistoryResponse
from app.bussines.bussines_ceps import get_cep_data
from app.repository.history_repository import get_history
from app.database import SessionLocal
from app.core.config import TOKEN_API

router = APIRouter()

# Dependência para obter uma sessão do banco

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Middleware manual para validar token

def validate_token(x_token: str = Header(...)):
    if x_token != TOKEN_API:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")

# Rota: Buscar CEP
@router.get("/cep/{cep}", response_model=CepResponse)
async def get_cep(
        cep: str,
        db: Session = Depends(get_db),
        _: None = Depends(validate_token)
):
    return await get_cep_data(cep, db)

# Rota: Ver histórico
@router.get("/historico", response_model=List[HistoryResponse])
def listar_historico(
    db: Session = Depends(get_db),
    _: None = Depends(validate_token)
):
    return get_history(db)
