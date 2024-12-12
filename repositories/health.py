from sqlmodel import Session, text


def database_health(session: Session):
    try:
        session.execute(text("SELECT 1"))
        return True
    except Exception as e:
        return False
