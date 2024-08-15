from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException
from config import engine, SessionLocal
from sqlalchemy.orm import Session
from pydantic import BaseModel
import models

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class UserBase(BaseModel):
    name: str
    email: str
    designation: str

class DesignationBase(BaseModel):
    designation_text: str
    salary: int 

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/createUser/")
async def create_user(user: UserBase, db:db_dependency):
    # Check if user already exists
    existing_user = db.query(models.Users).filter(models.Users.email == user.email).all()
    if existing_user:
        return HTTPException(status_code=409, detail="User already exists", headers={
            "Content-Type": "application/json",
            "X-Error-Reason": "User with email already exists",
            "Cache-Control": "no-store",
        })

    db_designation = db.query(models.Designations).filter(models.Designations.designation_text == user.designation).first()
    if not db_designation:
        # create new designation
        db_designation = models.Designations(designation_text=user.designation, salary=100)
        db.add(db_designation)
        db.commit()
        db.refresh(db_designation)

    db_user = models.Users(name=user.name, email=user.email, designation=db_designation.id)
    db.add(db_user)
    db.commit()

@app.get("/usersByDesignation/{designation_id}")
async def get_user(designation_id: int, db:db_dependency):
    users = db.query(models.Users).filter(models.Users.designation == designation_id).all()
    if not users:
        raise HTTPException(status_code=404, detail="User is not found!")
    return users

@app.get("/users/")
async def get_all_users(db:db_dependency):
    users = db.query(models.Users).all()
    if not users:
        raise HTTPException(status_code=404, detail="No registered users.")
    return users

@app.get("/designations/")
async def get_all_designations(db:db_dependency):
    designations = db.query(models.Designations).all()
    if not designations:
        raise HTTPException(status_code=404, detail="No registered designations.")
    return designations