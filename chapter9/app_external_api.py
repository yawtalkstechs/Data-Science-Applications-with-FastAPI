from typing import Any

import httpx
from fastapi import FastAPI, Depends

app = FastAPI()

class ExternalAPI:
    def __init__(self) -> None:
        self.client = httpx.AsyncClient(base_url="https://dummyjson.com")

    async def __call__(self) -> dict[str, Any]:
        async with self.client as client:
            response = await client.get("/products")
            return response.json()
        
external_api = ExternalAPI()

@app.get("/products")
async def external_products(products: dict[str, any] = Depends(external_api)):
    return products