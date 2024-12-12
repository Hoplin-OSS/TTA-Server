import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import http_router, ws_router

app = FastAPI(title="TTA Server", version=os.getenv("VERSION", "Unknown"))
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Routers
app.include_router(http_router)


# WebSocket Routers
app.include_router(ws_router)
