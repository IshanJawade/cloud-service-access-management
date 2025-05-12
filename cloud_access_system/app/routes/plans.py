from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db

router = APIRouter(prefix="/plans", tags=["Plans"])

@router.post("/", response_model=schemas.SubscriptionPlanOut)
def create_plan(plan: schemas.SubscriptionPlanCreate, db: Session = Depends(get_db)):
    if db.query(models.SubscriptionPlan).filter_by(name=plan.name).first():
        raise HTTPException(status_code=400, detail="Plan name already exists.")
    db_plan = models.SubscriptionPlan(**plan.dict())
    db.add(db_plan)
    db.commit()
    db.refresh(db_plan)
    return db_plan

@router.put("/{plan_id}", response_model=schemas.SubscriptionPlanOut)
def update_plan(plan_id: int, updated: schemas.SubscriptionPlanCreate, db: Session = Depends(get_db)):
    plan = db.query(models.SubscriptionPlan).get(plan_id)
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found.")
    for key, value in updated.dict().items():
        setattr(plan, key, value)
    db.commit()
    db.refresh(plan)
    return plan

@router.delete("/{plan_id}")
def delete_plan(plan_id: int, db: Session = Depends(get_db)):
    plan = db.query(models.SubscriptionPlan).get(plan_id)
    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found.")
    db.delete(plan)
    db.commit()
    return {"message": "Plan deleted"}
