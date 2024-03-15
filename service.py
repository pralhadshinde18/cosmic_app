from sqlalchemy.orm import Session
from domain import create_item as domain_create_item, get_item as domain_get_item, \
    process_get_request as domain_process_get_request
import schema


def create_item(db: Session, item: schema.ItemCreate):
    return domain_create_item(db, item)


def get_item(db: Session, item_id: int):
    return domain_get_item(db, item_id)


def process_get_request(db: Session, item_id: int):
    return domain_process_get_request(db, item_id)
