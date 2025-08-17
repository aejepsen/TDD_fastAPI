from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "Store API"
    ROOT_PATH: str = "/"

    DATABASE_URL: str

    model_config = SettingsConfigDict(
        env_file="/home/aejepsen/Documentos/"
        "TDD_fastAPI/TDDfastAPI/.env",
        extra='ignore')


settings = Settings()

print(f"DATABASE_URL carregada: {settings.DATABASE_URL}")
