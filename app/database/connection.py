from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , declarative_base


engine = create_engine("sqlite:///app/database/warehouse.db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base = declarative_base()

