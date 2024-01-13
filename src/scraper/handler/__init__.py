from fastapi import APIRouter
from src.scraper.services import ScraperServices

services = ScraperServices()
scraper_router = APIRouter(prefix='/scraper')


@scraper_router.get('/all-battles')
async def get_all_battles():
    await services.get_all_rappers_battles()