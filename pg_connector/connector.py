import asyncpg
from asyncpg.pool import Pool


class DBConnector:
    def __init__(self, pool: Pool):
        self.pool = pool

    async def execute(self, query: str, *args):
        async with self.pool.acquire() as connection:
            return await connection.execute(query, *args)

    async def fetch(self, query: str, *args):
        async with self.pool.acquire() as connection:
            return await connection.fetch(query, *args)


async def create_pool(user: str, password: str, database: str, host: str):
    return await asyncpg.create_pool(user=user, password=password,
                                     database=database, host=host)
