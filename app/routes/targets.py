from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter()


@router.patch("/{target_id}/complete", response_model=schemas.Target)
def target_complete(target_id: int, db: Session = Depends(get_db)):
    completed_target = crud.complete_target(db, target_id)
    if not completed_target:
        raise HTTPException(status_code=404, detail="Target not found")
    return completed_target


@router.patch("/{target_id}", response_model=schemas.Target)
def target_notes_update(target_id: int, target_update: schemas.TargetUpdate, db: Session = Depends(get_db)):
    updated_target = crud.update_target_notes(db, target_id, target_update)
    if not updated_target:
        raise HTTPException(status_code=400, detail="Cannot update notes for a completed target")
    return updated_target
