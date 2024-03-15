from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import models
import schema
from models import Base

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)


def create_item(db: SessionLocal, item: schema.ItemCreate):
    db_item = models.Item(name=item.name, stock=item.stock, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_item(db: SessionLocal, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()
