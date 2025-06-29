from sqlalchemy.orm import Session
from app.models.history import History
from typing import List


# salva um novo registro no historico

async def save_history(db: Session, cep: str, response_time: str, source: str) -> None:
    history = History(
        cep=cep,
        response_time=response_time,
        source=source
    )
    db.add(history)
    db.commit()

# retorna todos os registros do historico
def get_history(db: Session) -> List[History]:
    return db.query(History).order_by(History.timestamp.desc()).all()
