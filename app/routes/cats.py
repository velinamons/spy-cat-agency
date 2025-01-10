from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db

router = APIRouter()


@router.post("/", response_model=schemas.Cat)
def create_cat(cat: schemas.CatCreate, db: Session = Depends(get_db)):
    return crud.create_cat(db=db, cat=cat)


@router.get("/", response_model=list[schemas.Cat])
def get_cats(db: Session = Depends(get_db)):
    return crud.get_cats(db=db)


@router.get("/{cat_id}", response_model=schemas.Cat)
def get_cat(cat_id: int, db: Session = Depends(get_db)):
    db_cat = crud.get_cat(db=db, cat_id=cat_id)
    if db_cat is None:
        raise HTTPException(status_code=404, detail="Cat not found")
    return db_cat


@router.put("/{cat_id}", response_model=schemas.Cat)
def update_cat(cat_id: int, cat: schemas.CatUpdate, db: Session = Depends(get_db)):
    db_cat = crud.update_cat(db=db, cat_id=cat_id, cat=cat)
    if db_cat is None:
        raise HTTPException(status_code=404, detail="Cat not found")
    return db_cat


@router.delete("/{cat_id}")
def delete_cat(cat_id: int, db: Session = Depends(get_db)):
    db_cat = crud.delete_cat(db=db, cat_id=cat_id)
    if db_cat is None:
        raise HTTPException(status_code=404, detail="Cat not found")
    return {"message": "Cat deleted successfully"}
