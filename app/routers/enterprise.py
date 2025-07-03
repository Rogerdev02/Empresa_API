from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database.connection import SessionLocal
from app.models.enterprise_model import Enterprise
from app.schemas.enterprise_schema import EnterpriseCreate, EnterpriseOut

router = APIRouter(
    prefix="/enterprise",
    tags=["Enterprise"]
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=EnterpriseOut, status_code=status.HTTP_201_CREATED)
def create_enterprise(enterprise: EnterpriseCreate, db: Session = Depends(get_db)):
    existing = db.query(Enterprise).filter(Enterprise.cnpj == enterprise.cnpj).first()
    if existing: 
        raise HTTPException(status_code=400, detail="CNPJ already registered")
    
    new_enterprise = Enterprise(**enterprise.model_dump())
    db.add(new_enterprise)
    db.commit()
    db.refresh(new_enterprise)
    return new_enterprise


@router.get("/", response_model=List[EnterpriseOut])
def list_enterprises(db: Session = Depends(get_db)):
    return db.query(Enterprise).all()


@router.get("/{enterprise_id}", response_model=EnterpriseOut)
def get_enterprise(enterprise_id: int, db: Session = Depends(get_db)):
    enterprise = db.query(Enterprise).filter(Enterprise.id == enterprise_id).first()
    if not enterprise:
        raise HTTPException(status_code=404, detail="Enterprise not found")
    return enterprise


@router.put("/{enterprise_id}", response_model=EnterpriseOut)
def update_enterprise(enterprise_id: int, update_data: EnterpriseCreate, db: Session = Depends(get_db)):
    enterprise = db.query(Enterprise).filter(Enterprise.id == enterprise_id).first()
    if not enterprise:
        raise HTTPException(status_code=404, detail="Enterprise not found")

    for key, value in update_data.model_dump().items():
        setattr(enterprise, key, value)

    db.commit()
    db.refresh(enterprise)
    return enterprise


@router.delete("/{enterprise_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_enterprise(enterprise_id: int, db: Session = Depends(get_db)):
    enterprise = db.query(Enterprise).filter(Enterprise.id == enterprise_id).first()
    if not enterprise:
        raise HTTPException(status_code=404, detail="Enterprise not found")

    db.delete(enterprise)
    db.commit()
    return None
