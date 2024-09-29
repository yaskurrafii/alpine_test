"""
db.py

File for interaction with db, Connecting, getting session, etc

"""

from sqlmodel import create_engine, Session, SQLModel

# Should change user, pass and port that connected to your database 
Database_url = "mysql+pymysql://{user}:{pass}@localhost:{port}/alpine"

engine = create_engine(Database_url)

def create_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session