from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas

router = APIRouter(prefix="/subscriptions", tags=["Subscriptions"])

@router.post("/", response_model=schemas.UserSubscriptionOut)
def create_subscription(sub: schemas.UserSubscriptionCreate, db: Session = Depends(get_db)):
    existing = db.query(models.UserSubscription).filter(models.UserSubscription.user_id == sub.user_id).first()
    if existing:
        raise HTTPException(status_code=400, detail="User already subscribed.")
    subscription = models.UserSubscription(**sub.dict())
    db.add(subscription)
    db.commit()
    db.refresh(subscription)
    return subscription

@router.get("/{user_id}", response_model=schemas.UserSubscriptionOut)
def get_user_subscription(user_id: int, db: Session = Depends(get_db)):
    sub = db.query(models.UserSubscription).filter(models.UserSubscription.user_id == user_id).first()
    if not sub:
        raise HTTPException(status_code=404, detail="No subscription found.")
    return sub

@router.put("/{user_id}", response_model=schemas.UserSubscriptionOut)
def update_user_subscription(user_id: int, sub: schemas.UserSubscriptionCreate, db: Session = Depends(get_db)):
    existing = db.query(models.UserSubscription).filter(models.UserSubscription.user_id == user_id).first()
    if not existing:
        raise HTTPException(status_code=404, detail="Subscription not found.")
    existing.plan_id = sub.plan_id
    db.commit()
    db.refresh(existing)
    return existing
