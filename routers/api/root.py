from fastapi import APIRouter

import routers.api.health as health_router

router = APIRouter()
router.include_router(health_router.router)
