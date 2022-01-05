from fastapi import FastAPI

app = FastAPI(
    title='image-resize-api',
    version='1.0.0',
)

from app.main.routes import *