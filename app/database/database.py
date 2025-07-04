"""PostgreSQL connect module"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import settings

DATABASE_URL = (
    "postgresql://"
    f"{settings.database_id}"
    ":"
    f"{settings.database_pw}"
    "@"
    f"{settings.database_url}"
    ":"
    f"{settings.database_port}"
    "/"
    f"{settings.database_db}"
)

engine = create_engine(url=DATABASE_URL, echo=False)
SessionLocal = sessionmaker(
    bind=engine,
    expire_on_commit=False,
)

Base = declarative_base()


def get_db():
    """database connection session

    Yields
    ------
    session
        SQLAlchemy session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
