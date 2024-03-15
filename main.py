from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from repository import SessionLocal
import schema, service

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/items/", response_model=schema.Item)
async def create_item(item: schema.ItemCreate, db: Session = Depends(get_db)):
    return service.create_item(db, item)


@app.get("/items/{item_id}", response_model=schema.Item)
async def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = service.get_item(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@app.get("/process/{item_id}", response_model=schema.Item)
async def process_get_request(item_id: int, db: Session = Depends(get_db)):
    updated_item = service.process_get_request(db, item_id)
    if updated_item:
        return updated_item
    else:
        raise HTTPException(status_code=404, detail="Item not found")
