from fastapi import APIRouter
from src.scraper.handler import scraper_router

app_router = APIRouter(prefix='/api')
app_router.include_router(scraper_router)