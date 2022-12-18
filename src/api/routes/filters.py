from typing import List, Text

from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from ...db import Course
from ..utils import get_db

filters_router = APIRouter()


@filters_router.get("/categories/", response_model=List[Text])
async def get_categories(db: Session = Depends(get_db)):
    return db.exec(select(Course.category).distinct()).all()


@filters_router.get("/areas/", response_model=List[Text])
async def get_areas(db: Session = Depends(get_db)):
    return db.exec(select(Course.fg_area).distinct()).all()


@filters_router.get("/formats/", response_model=List[Text])
async def get_formats(db: Session = Depends(get_db)):
    return db.exec(select(Course.format).distinct()).all()
