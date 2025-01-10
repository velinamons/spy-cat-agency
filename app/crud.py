from sqlalchemy.orm import Session
from app.models import Cat
from app.schemas import CatCreate, CatUpdate


def create_cat(db: Session, cat: CatCreate):
    db_cat = Cat(
        name=cat.name,
        years_of_experience=cat.years_of_experience,
        breed=cat.breed,
        salary=cat.salary,
    )
    db.add(db_cat)
    db.commit()
    db.refresh(db_cat)
    return db_cat


def get_cats(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Cat).offset(skip).limit(limit).all()


def get_cat(db: Session, cat_id: int):
    return db.query(Cat).filter(Cat.id == cat_id).first()


def update_cat(db: Session, cat_id: int, cat: CatUpdate):
    db_cat = db.query(Cat).filter(Cat.id == cat_id).first()
    if db_cat:
        if cat.years_of_experience is not None:
            db_cat.years_of_experience = cat.years_of_experience
        if cat.salary is not None:
            db_cat.salary = cat.salary
        db.commit()
        db.refresh(db_cat)
    return db_cat


def delete_cat(db: Session, cat_id: int):
    db_cat = db.query(Cat).filter(Cat.id == cat_id).first()
    if db_cat:
        db.delete(db_cat)
        db.commit()
    return db_cat
