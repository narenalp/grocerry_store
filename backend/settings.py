from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List
import os

class Settings(BaseSettings):
    """Application settings loaded from environment variables"""
    
    # Database
    # local postgresql://postgres:123456@localhost/grocery_pos

    DATABASE_URL: str = "postgresql://postgres.ytvrindkjcirsuntzazw:RadheShyam2315@aws-1-ap-southeast-1.pooler.supabase.com:5432/postgres"
    
    # JWT Security
    SECRET_KEY: str = "grocery_pos_super_secret_key_2024_change_in_production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    
    # CORS
    CORS_ORIGINS: List[str] = [
        "http://localhost:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:5174",
        "http://localhost:3000"
    ]
    
    # Environment
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    
    # Server
    HOST: str = "127.0.0.1"
    PORT: int = 8000

    model_config = SettingsConfigDict(
        env_file=".env", 
        extra="ignore",
        case_sensitive=True
    )

# Create settings instance
settings = Settings()
