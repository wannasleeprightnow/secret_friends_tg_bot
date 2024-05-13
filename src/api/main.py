import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.routers import apiv1
from settings import Settings

app = FastAPI(title="secret_friends_tb_bot_api")
logger = logging.getLogger(__name__)

app.include_router(apiv1)
app.add_middleware(
    CORSMiddleware,
    allow_origins=Settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
