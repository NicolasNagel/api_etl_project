from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # PostgreSQL Database Enviroment
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int

    # PGAdmin4 Enviroment
    PGADMIN_DEFAULT_EMAIL: str
    PGADMIN_DEFAULT_PASSWORD: str

    # APIFootball Enviroment
    API_KEY: str

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8'
    )

    @property
    def database_url(self) -> str:
        return (
            f'postgresql://'
            f'{self.POSTGRES_USER}:'
            f'{self.POSTGRES_PASSWORD}@'
            f'{self.POSTGRES_HOST}:'
            f'{self.POSTGRES_PORT}/'
            f'{self.POSTGRES_DB}'
        )
    
settings = Settings()