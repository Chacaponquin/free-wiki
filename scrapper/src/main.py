from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.app.handler import app_router


app = FastAPI()

# router
app.include_router(app_router)

# cors
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



