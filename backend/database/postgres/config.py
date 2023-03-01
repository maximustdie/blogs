from dataclasses import dataclass
from os import getenv

from sqlalchemy.engine import URL


@dataclass
class PG:
    ip: str
    port: int
    name: str
    user: str
    password: str

    def construct_url(self) -> URL:
        return URL.create(
            drivername="postgresql+asyncpg",
            username=self.user,
            password=self.password,
            host=self.ip,
            database=self.name,
            port=self.port
        )


@dataclass
class Config:
    pg: PG


def load_config():
    return Config(
        pg=PG(
            ip=getenv("POSTGRES_HOST"),
            port=int(getenv("POSTGRES_PORT") or 5432),
            user=getenv("POSTGRES_USER"),
            password=getenv("POSTGRES_PASSWORD"),
            name=getenv("POSTGRES_DB"),
        )
    )


config = load_config()
