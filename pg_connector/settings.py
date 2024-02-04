from dotenv import dotenv_values


class DBConfig:
    def __init__(self, env_file=".env"):
        config = dotenv_values(env_file)
        self.user = config.get("POSTGRES_USER")
        self.password = config.get("POSTGRES_PASSWORD")
        self.host = config.get("POSTGRES_HOST")
        self.port = config.get("POSTGRES_PORT")
        self.database = config.get("POSTGRES_DATABASE")
