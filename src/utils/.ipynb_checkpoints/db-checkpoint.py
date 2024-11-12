import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv


load_dotenv()

def get_engine():
    username = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    host = "localhost"
    port = 5433
    database = os.getenv("POSTGRES_DB")

    engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            print("Verbindung erfolgreich")
    except Exception as e:
        print("Fehler beim Verbinden zur Datenbank:", e)
    
    return create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}')


def get_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()

