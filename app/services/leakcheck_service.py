from app.clients.leakcheck_client import LeakCheckClient


class LeakCheckService:

    def __init__(self):

        self.client = LeakCheckClient()

    async def search_email(self, email: str):

        return await self.client.search(email)

    async def search_username(self, username: str):

        return await self.client.search(username)