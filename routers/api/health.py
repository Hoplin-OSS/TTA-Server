from fastapi import APIRouter, Request
import services.health as health_service
from internal.common.dependency import DatabaseSession

router = APIRouter(
    prefix="/health"
)
router_tags = ["health"]


@router.get("/", tags=router_tags)
async def health(session: DatabaseSession,request: Request):
    database_status = await health_service.database_health(session)
    return {
        "status": "ok",
        "database": database_status
    }