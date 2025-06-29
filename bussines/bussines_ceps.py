import asyncio
from fastapi import HTTPException
from sqlalchemy.orm import  Session

from app.client.client_ceps import fetch_cep_from_api, fetch_from_brasilapi
from app.repository.history_repository import save_history
from app.schemas.cep_response import CepResponse

async def get_cep_data(cep: str, db:Session) -> CepResponse:
    tasks= [
        fetch_cep_from_api(cep),
        fetch_from_brasilapi(cep)
    ]
    done, _ = await  asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    for task in done:
        result = task.result()
        if result and not result.get("erro", False):
            # Gravar histórico no banco
            await save_history(
                db=db,
                cep=cep,
                response_time=result["response_time"],
                source=result["source"]
            )
            return CepResponse(**result)
            # Nenhuma API retornou resultado válido
        raise HTTPException(status_code=404, detail="CEP não encontrado em nenhuma fonte.")
