from sqlalchemy.orm import Session
from app.models import Cat, Mission, Target
from app.schemas import CatCreate, CatUpdate, MissionCreate, TargetUpdate


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


def create_mission(db: Session, mission: MissionCreate):
    db_mission = Mission(cat_id=mission.cat_id)
    db.add(db_mission)
    db.commit()
    db.refresh(db_mission)

    for target in mission.targets:
        db_target = Target(
            mission_id=db_mission.id,
            name=target.name,
            country=target.country,
            notes=target.notes,
        )
        db.add(db_target)

    db.commit()
    return db_mission


def get_mission(db: Session, mission_id: int):
    return db.query(Mission).filter(Mission.id == mission_id).first()


def list_missions(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Mission).offset(skip).limit(limit).all()


def delete_mission(db: Session, mission_id: int):
    mission = db.query(Mission).filter(Mission.id == mission_id).first()
    if not mission.cat_id:
        db.delete(mission)
        db.commit()
        return True
    return False


def complete_mission(db: Session, mission_id: int):
    db_mission = db.query(Mission).filter(Mission.id == mission_id).first()
    if not db_mission:
        return None

    db_mission.complete = True
    db.commit()
    db.refresh(db_mission)
    return db_mission


def complete_target(db: Session, target_id: int):
    db_target = db.query(Target).filter(Target.id == target_id).first()
    if not db_target:
        return None

    db_target.complete = True
    db.commit()
    db.refresh(db_target)
    return db_target


def update_target_notes(db: Session, target_id: int, target_update: TargetUpdate):
    db_target = db.query(Target).filter(Target.id == target_id).first()
    if not db_target:
        return None

    if db_target.complete:
        return None

    if db_target.mission and db_target.mission.complete:
        return None

    if target_update.notes is not None:
        db_target.notes = target_update.notes

    db.commit()
    db.refresh(db_target)
    return db_target
