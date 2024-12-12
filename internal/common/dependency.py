from typing import Annotated

from fastapi import Depends
from sqlmodel import Session

from internal.database.connector import SessionLocal


def database_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Dependency Injection
DatabaseSession = Annotated[Session, Depends(database_session)]
