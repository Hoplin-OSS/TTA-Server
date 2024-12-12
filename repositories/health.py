from sqlmodel import text
from sqlmodel import Session

def database_health(session:Session):
    try:
        session.execute(text("SELECT 1"))
        return True
    except Exception as e:
        return False