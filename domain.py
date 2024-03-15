from sqlalchemy.orm import Session
from repository import create_item as repo_create_item, get_item as repo_get_item
from schema import ItemCreate


def create_item(db: Session, item: ItemCreate):
    return repo_create_item(db, item)


def get_item(db: Session, item_id: int):
    return repo_get_item(db, item_id)


def process_get_request(db: Session, item_id: int):
    item = repo_get_item(db, item_id)
    if item:
        item.stock = item.stock - 1
        db.commit()
        db.refresh(item)
        return item
    return None
