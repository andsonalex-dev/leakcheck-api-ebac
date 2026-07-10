import httpx

from app.core.config import settings


class LeakCheckClient:

    async def search(self, query: str):

        async with httpx.AsyncClient(timeout=20) as client:

            response = await client.get(
                settings.LEAKCHECK_URL,
                params={
                    "check": query
                }
            )

            response.raise_for_status()

            return response.json()