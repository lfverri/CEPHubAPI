from turtledemo.penrose import start

import httpx
from typing import Optional
import time

async def fetch_cep_from_api(url: str, source_name: str) -> Optional[dict]:
    start = time.perf_counter()
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response: await client.get(url)
            duration = time.perf_counter() - start
            if response.status_code == 200:
                data = response.json()
                data["source"] = source_name
                data["response_time"] = f"{duration:2.f}s"
                return data
            return None
    except Exception:
        return None

async def fetch_from_viacep(cep: str) -> Optional[dict]:
    url =  f"https://viacep.com.br/ws/{cep}/json/"
    return await fetch_cep_from_api(url, "via_cep")

async def fetch_from_brasilapi(cep: str) -> Optional[dict]:
    url = f"https://brasilapi.com.br/api/cep/v1/{cep}"
    return await fetch_cep_from_api(url, "brasil_api")