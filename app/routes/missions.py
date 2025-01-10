from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import get_db

router = APIRouter()


@router.post("/", response_model=schemas.Mission)
def create_mission(mission: schemas.MissionCreate, db: Session = Depends(get_db)):
    mission = crud.create_mission(db, mission)
    if not mission:
        raise HTTPException(
            status_code=404,
            detail=f"Cat with this id not found"
        )
    return mission


@router.get("/{mission_id}", response_model=schemas.Mission)
def read_mission(mission_id: int, db: Session = Depends(get_db)):
    mission = crud.get_mission(db, mission_id)
    if not mission:
        raise HTTPException(
            status_code=404,
            detail="Mission not found"
        )
    return mission


@router.get("/", response_model=List[schemas.Mission])
def list_missions(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.list_missions(db, skip=skip, limit=limit)


@router.delete("/{mission_id}")
def delete_mission(mission_id: int, db: Session = Depends(get_db)):
    if not crud.get_mission(db, mission_id):
        raise HTTPException(
            status_code=404,
            detail="Mission not found"
        )

    if not crud.delete_mission(db, mission_id):
        raise HTTPException(
            status_code=400,
            detail="Mission is assigned to a cat and cannot be deleted"
        )
    return {"message": "Mission deleted successfully"}


@router.patch("/{mission_id}/complete", response_model=schemas.Mission)
def mission_complete(mission_id: int, db: Session = Depends(get_db)):
    completed_mission = crud.complete_mission(db, mission_id)
    if not completed_mission:
        raise HTTPException(
            status_code=404,
            detail="Mission not found"
        )
    return completed_mission

