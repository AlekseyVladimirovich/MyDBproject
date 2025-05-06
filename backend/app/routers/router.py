import os
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.auth import UserCreate, UserRead
from app.models.models import User
from app.database import get_db
from passlib.context import CryptContext
import jwt

router = APIRouter(prefix="/rout", tags=["rout"])

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

@router.get("/router")
def register():
    return "router"
