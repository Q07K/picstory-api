from typing import List

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """애플리케이션 설정"""

    # JWT 설정
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    refresh_token_expire_days: int

    # API 설정
    api_v1_str: str
    project_name: str

    # CORS 설정
    backend_cors_origins: List[str] = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:8080",
        "http://127.0.0.1:8080",
    ]

    # 데이터베이스 설정
    database_id: str
    database_pw: str
    database_url: str
    database_port: str
    database_db: str

    # 스토리지 설정
    storage_url: str

    # 개발 모드
    DEBUG: bool = False

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8"
    )


# 전역 설정 인스턴스
settings = Settings()
