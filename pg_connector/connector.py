import asyncpg
from asyncpg.pool import Pool

from pg_connector.settings import DBConfig


class DBConnector:
    def __init__(self, pool: Pool):
        self.pool = pool

    async def execute_query(self, query: str, *args):
        async with self.pool.acquire() as connection:
            return await connection.execute(query, *args)

    async def fetch_data(self, query: str, *args):
        async with self.pool.acquire() as connection:
            return await connection.fetch(query, *args)


async def create_pool(user: str, password: str, database: str, host: str, port: int):
    return await asyncpg.create_pool(user=user, password=password, database=database, host=host, port=port)


class DatabaseConnector:
    _pool = None

    @classmethod
    async def get_connector(cls, db_config) -> DBConnector:
        if cls._pool is None:
            cls._pool = await create_pool(user=db_config.user, password=db_config.password,
                                          database=db_config.database, host=db_config.host, port=db_config.port)
        return DBConnector(pool=cls._pool)


async def get_database_connector() -> DBConnector:
    db_config = DBConfig()
    return await DatabaseConnector.get_connector(db_config)
