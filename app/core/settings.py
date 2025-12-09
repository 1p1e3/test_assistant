from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    model_config = {
        'env_file': '.env'
    }

    SECRET_KEY: str
 
    ALGORITHM: int

    ACCESS_TOKEN_EXPIRE_MINUTES: int

    REFRESH_TOKEN_EXPIRE_DAYS: int

    MYSQL_HOST: str

    MYSQL_PORT: int

    MYSQL_USER: str

    MYSQL_PASSWORD: int

    MYSQL_DB_NAME: str

    REDIS_HOST: str

    REDIS_PORT: int