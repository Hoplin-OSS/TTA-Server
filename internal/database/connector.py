import os
from load_dotenv import load_dotenv
from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy.orm import sessionmaker

load_dotenv(dotenv_path=".dev.env")

# Settings
database_debug = True if os.getenv("MODE","").lower() in ["dev","debug"] else False


# Engine Settings
connection_string = os.getenv("DATABASE_URL")
engine = create_engine(connection_string,echo=database_debug)
SQLModel.metadata.create_all(engine)

# Session
SessionLocal = sessionmaker(bind=engine,autoflush=False)


